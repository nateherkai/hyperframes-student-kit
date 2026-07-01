---
name: build-video-from-footage
description: >-
  Turn raw camera footage (talking-head, vlog, build/DIY clips) into a polished, graded
  Hyperframes motion-graphics film — cutting, word-synced captions, animated callouts,
  multi-clip "build-series" assembly, color grading, and self-hosted fonts. Use this WHENEVER
  the user has one or more recorded video files (e.g. IMG_*.mov, screen recordings, phone
  clips) and wants them edited into a finished video with captions, on-screen graphics, a
  LUT/color grade, section/chapter cards, or stitched into a series — even if they don't say
  "Hyperframes". This is the footage→film pipeline; the built-in /hyperframes skills only cover
  authoring a composition from scratch, not cutting real footage. Triggers: "edit this clip",
  "add captions to my video", "cut this down", "make these into one video", "add a LUT / color
  grade", "sync the transition to my clap", "stitch IMG_xxxx and IMG_yyyy together".
---

# Build a video from real footage (Hyperframes pipeline)

This skill captures the end-to-end workflow for turning raw recorded clips into a finished,
graded Hyperframes video. It complements the built-in `/hyperframes` skills: those teach you
how a composition is structured (the render contract, `window.__timelines`, `data-*` timing);
**this** teaches you how to take footage someone actually shot and build a real edit around it.

Read the `/hyperframes` and `/hyperframes-cli` skills (or `CLAUDE.md`) for the render contract.
Everything here sits on top of that.

## Environment note (this machine)

ffmpeg/ffprobe/brew are not on the agent's non-login shell PATH. Prefix shell commands with:

```
eval "$(/opt/homebrew/bin/brew shellenv)" && <command>
```

`npx hyperframes transcribe` and `render` shell out to ffmpeg, so they need the prefix too.
Avoid bare `rm -f foo*.png` / `ls foo*.png` in zsh — an unmatched glob aborts the whole command.

## The pipeline at a glance

```
re-encode → transcribe → CUT (segments) → assemble film → remap captions → build overlays → grade (LUT) → vendor fonts → render → verify frames
```

Most of the fiddly logic is in `scripts/`. Drive them from one config file so the whole edit is
reproducible and easy to re-run when the user sends the next clip.

## Step 1 — Prep the footage

Re-encode every raw clip to clean 1080p H.264 before referencing it (raw 4K `.mov` from phones
is heavy and can freeze frames mid-render):

```
eval "$(/opt/homebrew/bin/brew shellenv)" && \
ffmpeg -y -i IMG_xxxx.mov -vf "scale=1920:1080:flags=lanczos" -r 30 \
  -c:v libx264 -preset medium -crf 20 -c:a aac -b:a 192k -movflags +faststart out.mp4
```

Then transcribe each ORIGINAL clip's audio for word-level timestamps (English → `small.en`;
unknown language → `small` with no `.en`, because `.en` models *translate* instead of transcribe):

```
ffmpeg -y -i IMG_xxxx.mov -vn -c:a aac -b:a 192k IMG_xxxx-audio.m4a
npx hyperframes transcribe IMG_xxxx-audio.m4a --model small.en --json   # -> transcript.json
```

Read each transcript so you understand the content and can pick the beats. Save them as
`assets/IMG_xxxx-transcript.json` (one per clip).

## Step 2 — Decide the cut, then write the config

Look at the footage (extract a couple of frames with ffmpeg + Read them) so you know the framing —
where the subject is, so captions/callouts never cover the face. Pick segments to keep from each
clip. Two pacing modes the user will choose between:

- **Tight highlight** — drop tangents/dead air, ~50–60s per clip. Punchy.
- **Light trims (fuller)** — keep the walkthrough, drop only dead air + the messiest tails.

Write `build.config.json` (see `references/config-schema.md`) describing each clip's kept
`segments`, the per-section card text, and the measurement/spec `callouts`. This single file
drives the cut, the caption remap, and the overlay generation.

## Step 3 — Assemble the film

```
python3 scripts/build_film.py build.config.json
```

Builds each clip's cut (ffmpeg `trim`+`concat`), concatenates them into `assets/film.mp4`, and
writes `assets/build.state.json` with the **measured** per-section durations and film-timeline
offsets (needed because real cut durations drift a few frames from the segment math).

Gotcha: if you re-encode video with `-an`, the trimmed video has no audio stream — feed audio as
a second input and map `[0:v]`/`[1:a]`. `build_film.py` handles this by cutting from the
re-encoded clips that still carry audio.

## Step 4 — Captions: remap the CLEAN transcript onto the cut timeline

**Do NOT re-transcribe the cut.** Re-transcribing a chopped audio produces hallucinations
("Home Depot" → "Home Deep", "mark one side" → "dark mark"). Instead, take the clean original
transcript and mathematically remap each word's timestamp onto the assembled film timeline using
the segment boundaries + measured offsets. This is the single most important trick in the pipeline.

```
python3 scripts/build_overlays.py build.config.json
```

This remaps every clip's words, groups them into caption lines (breaking on segment seams,
sentence ends, long gaps, ≥5 words), and writes `compositions/captions.html` with a **word-by-word
pop** entrance. It also writes `compositions/callouts.html` with **count-up** numbers, both using
the locally-vendored fonts. See `references/render-safe-effects.md` for the animation patterns and
the seek-safety rules that make them render correctly.

## Step 5 — Color grade (LUT)

Generate a balanced cinematic 3D LUT and bake it into the footage. A `.cube` + ffmpeg `lut3d` is a
real, portable grade (better than CSS filters, which can't do a 3D LUT):

```
python3 scripts/make_lut.py --out assets/grade.cube           # tune flags for the look
eval "$(/opt/homebrew/bin/brew shellenv)" && \
ffmpeg -y -i assets/film.mp4 -vf "lut3d=assets/grade.cube" \
  -c:v libx264 -preset medium -crf 18 -c:a copy -movflags +faststart assets/film-graded.mp4
```

Point the composition's `<video>`/`<audio>` `src` at `film-graded.mp4`. Default grade neutralizes
warm casts, adds a gentle S-curve, rolls off highlights, slightly desaturates. Always show the
user a before/after frame — color is subjective.

## Step 6 — Self-host the fonts (offline + lint-clean)

Hyperframes auto-fetches Google Fonts at render time, but that leaves `google_fonts_import` /
`font_family_without_font_face` lint errors and a network dependency. Vendor them locally:

```
python3 scripts/vendor_fonts.py --out assets --families "Inter:500,600,700" "Roboto Mono:500,700"
```

Downloads every subset `.woff2` into `assets/fonts/`, writes `assets/fonts.css`, and the
overlay/root builders inline those `@font-face` rules. Verify the special glyphs your callouts use
(`″ ° ½ × ·`) still render — the inch-mark `″` (U+2033) lives in the `latin` subset's
`unicode-range`, so keep all returned subsets rather than trimming.

## Step 7 — Build the root composition (the energy layer)

The root `index.html` wires the graded video + audio + caption/callout sub-comps + section cards,
plus the "keep-them-watching" layer: film grain, vignette, a progress bar, a section ticker, and
transition flashes. All of it must be **render-safe** (animate via property tweens / `tl.set`,
which apply on frame-seek; never rely on `tl.call`, which does NOT fire during a seek render). See
`references/render-safe-effects.md` for copy-paste recipes and z-index ordering.

**Clap-synced transitions:** if the user claps at the end of a clip as a cut cue, fire the next
section card *on* the clap. Find it with `python3 scripts/detect_claps.py <audio> <clip_dur>`
(reports sharp-attack transients near the clip end) and **confirm visually** — extract frames
around the candidate and Read them to see hands coming together (audio peaks alone can't tell a
clap from a saw/board-drop). Map the clap's original time onto the film timeline via the offsets.

## Step 8 — Lint, render, verify (mandatory)

```
eval "$(/opt/homebrew/bin/brew shellenv)" && npx hyperframes lint        # only the known intro-card
                                                                          # overlay false-positive is OK
npx hyperframes render --quality draft --output renders/film-draft.mp4
```

**Always verify by reading frames** — lint passing ≠ design working. Pull frames at each section
card, each callout (catch one mid-count + one settled), the clap transition, and the outro; `Read`
every PNG. Check faces aren't covered, numbers count correctly, captions sync, glyphs render.
Use `npx hyperframes snapshot --at t1,t2,...` for fast spot-checks without a full render. Then
`--quality standard` for the final. Serve `renders/` via `npx serve renders -p 8080 -n` (range
support) so the user can scrub; `open -R renders/final.mp4` to hand it over.

## Reproducibility

Everything traces back to `build.config.json`. When the user sends the next clip in a series, add
it to the config and re-run Steps 3–8 — the captions, callouts, sections, and grade regenerate
consistently. Keep a `DESIGN.md` in the project for palette/typography so the look stays consistent
across episodes.

## References

- `references/config-schema.md` — the `build.config.json` schema with a worked example.
- `references/render-safe-effects.md` — grain, vignette, progress bar, ticker, flash, count-up,
  word-pop captions, the slow push; plus the GSAP seek-safety rules (why `tl.call` breaks renders).
- `scripts/` — `build_film.py`, `build_overlays.py`, `make_lut.py`, `vendor_fonts.py`,
  `detect_claps.py`. Each runs standalone; read its `--help`/header for args.
