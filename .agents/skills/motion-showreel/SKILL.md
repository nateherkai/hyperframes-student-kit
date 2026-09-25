---
name: motion-showreel
description: Design and build a 10-30 second motion-design showreel or brand reel in the style of Nate's Opus 5.5 "CLAUDE / MOTION REEL": one brand motif transformed through labeled craft chapters, a persistent HUD, cuts locked to a 120-130 BPM grid, a sub-second flurry, and a held logo lockup that answers the opening. Use when asked for a showreel, sizzle reel, brand reel, motion reel, "a reel like the Opus one", "show off motion design for <brand>", a 15-second brand film cut to music, or to study why a reference reel works and rebuild that energy for another brand.
---

# Motion Showreel

A showreel promises that every frame was a decision. This skill turns that into a
repeatable build: pick one motif, push it through six or seven craft chapters that
each look nothing alike, cut on the beat, and end on the motif.

The style source is [the reference breakdown](references/reference-breakdown.md), a
measured second-by-second analysis of the reel this skill was built from. Read it first.
Techniques per chapter live in [the chapter library](references/chapter-library.md).

## The grammar

1. **One motif, transformed.** Pick the brand's most reduced element (a dot, a play
   triangle, a letter, a logo corner). It opens the reel, turns into each chapter's
   material, and closes the reel as punctuation in the lockup. Nearly every
   transition turns the current object into the next one. Hard cuts are reserved
   for the flurry.
2. **Labeled craft chapters.** Six or seven, each named in the HUD by the discipline
   it demonstrates (`01 · SQUASH & STRETCH`). Use the brand's own words when it has
   them (YouTube has "chapters" and an "end screen").
3. **Show the work.** Every chapter gets one tool overlay: a physics readout, a
   selection box with a cursor, a parameter panel, a bezier graph, or a brand-native
   equivalent (a search bar, a counter, a settings menu).
4. **Persistent HUD.** Corner crop marks, a title line top left, a spec line top
   right (`1920×1080 · 60P · 129 BPM`, blinking dot), timecode bottom left, a
   progress ruler with chapter gaps bottom center, and the chapter label bottom
   right. Mono caps, tracking 0.2em, about 16px. It flips ink/paper with the
   background. Start from [the HUD template](templates/hud.html).
5. **Ink, paper, one accent, and one held-back color.** The held-back color only
   appears in the climax flurry. Every chapter change flips value (dark/light) or
   saturation (neutral/full-bleed accent).
6. **Cut on the beat, animate on the off-beats.** 120-130 BPM. Every hard cut,
   flash, and invert lands within 2 frames of a grid line. One pre-drop gap (music
   ducked for half a beat) comes before the midpoint hit.
7. **Accelerate, then hold.** For 15s at about 129 BPM (32 beats): physics intro 4
   beats, type chapter 8 beats with an internal invert, three 4-beat chapters (drop
   in the middle), a flurry of about 6 cuts in 4 beats (one beat each, then half
   beats), then about 4 beats of lockup. Roughly 75% development, 13% flurry, and
   12% resolve.
8. **Density breathes.** One object, then a wall of type, a grid of 100, thousands
   of particles, one hero object, the flurry, and one word again.
9. **Three type voices.** A heavy display face for statements, a contrasting accent
   voice (an italic serif, or the brand's UI face), and wide-tracked mono for the
   machine layer. Type also works as texture: repeated into wallpaper, banded, and
   inverted.
10. **Physical finish.** Squash and stretch, motion blur on fast moves, bloom on
    light-on-dark, slight chromatic fringe, grain, vignette, and a dot grid on dark
    frames. It should look photographed, not exported.
11. **Bookend.** The lockup resolves from noise, a rule draws, the subtitles type on
    with a block cursor, the motif lands as the final punctuation with a squash, and
    a quiet tagline arrives last.

## Workflow

Run the scripts from the kit root. They need Node 22+ and FFmpeg with ffprobe.

### 1. Study the reference (when one is given)

```sh
node .agents/skills/motion-showreel/scripts/analyze-reference.mjs path/to/reference.mp4 video-projects/my-reel/qa/reference --fps 6 --bpm 128
```

Read every contact sheet, then `report.txt` (cuts, luminance rhythm, RMS, onsets,
and cut offsets from the beat). Write the timeline down in the shape of the
reference breakdown.

### 2. Brand intake: `BRAND.md`

Collect exact colors (from the current logo file, not a blog), typography (the
proprietary face plus the closest free substitute), official logo SVGs, signature UI
and objects, and 3-5 verified facts with dates for kinetic type. Gather real
imagery the user owns or can use. Pick the motif and the held-back climax color.
Only use brand marks the user has the right to use for the intended purpose.

### 3. Chapter map: `STORYBOARD.md`

Create the project with `npm run new-video -- my-reel`, then fill in
[the storyboard template](templates/storyboard.md). For each chapter, record the
discipline label, the brand-native object, the tool overlay, the in-transform, the
out-transform, the value (dark/paper/accent), and the SFX. Before building:

- Freeze any frame in your head: does it read as the brand with the HUD covered?
- Does every transition transform the object, except the flurry cuts?
- Does the value flip at every chapter change?

### 4. Music and the beat grid

Read `docs/TOOLS-AND-API-KEYS.md` first. Music can be the user's own licensed track
or generated. Generation is a paid call, so confirm before running it:

```sh
node .agents/skills/motion-showreel/scripts/kie.mjs music --title "Reel" --style "punchy electronic showreel, instrumental, 128 bpm, starts instantly, riser into a big drop" --out video-projects/my-reel/assets/audio
node .agents/skills/motion-showreel/scripts/music-grid.mjs video-projects/my-reel/assets/audio/take-0.mp3 --bpm 128 --beats
```

`music-grid` prints the period, the **kick-band phase** (use it), and per-bar and
per-beat energy. The full-band phase can lock onto off-beat hats and put every
splice half a beat late; the script warns when the two disagree. In the per-beat
low-band column, find the riser, the drop (a jump of 10+ dB), the break, and the
return. Then splice 32 beats: intro and build (16, ending on the drop's downbeat),
drop (8), break (4, under the flurry), and the return hit plus a tail:

```sh
node .agents/skills/motion-showreel/scripts/splice-music.mjs take-0.mp3 --period 0.4644 --phase 0.085 --segments "4-28,48-56.7" --length 15 --gap 16 --out music-bed.wav
node .agents/skills/motion-showreel/scripts/music-grid.mjs music-bed.wav --bpm 129
node .agents/skills/motion-showreel/scripts/beatgrid.mjs --period 0.4644 --length 15 --chapters "01 Physics:4, 02 Type:8, 03 Grid:4, 04 Drop:4, 05 Lookdev:4, Flurry:4, 07 End:rest"
```

The re-measured bed's kick phase should be within about 25 ms of 0. Put the
measured BPM in the HUD (129, not 128). `beatgrid` prints the frame sheet for
`STORYBOARD.md`.

### 5. SFX and the mix

Generate a kit (paid, confirm first) with `scripts/sfx.mjs` (pops, clicks,
whooshes, glitch, ticks, shimmer, sub boom, final hit, and brand-native sounds), or
use the user's own library. Place cues on the beat sheet in an `events.json` and
premix:

```sh
node .agents/skills/motion-showreel/scripts/mix.mjs --bed music-bed.wav --events events.json --out master.wav
```

Use `master.wav` as the composition's single `<audio>` track. It targets -14 LUFS
and -1.2 dBTP.

### 6. Assets

- **Hero lookdev object.** Run `kie.mjs image --ref <logo.png>` (Seedream
  image-to-image keeps the silhouette), then `kie.mjs video --image <still>` for a
  5s Kling camera move. Both are paid calls. Kling returns 24fps: speed it up and
  re-encode at 60fps all-intra (the command is in the header of `kie.mjs`).
- **Fonts.** Download them into the project's `assets/fonts/` and use `@font-face`.
  Never rely on system fonts.

### 7. Build (HyperFrames)

Load `hyperframes` and `gsap` before writing HTML. Read `MOTION_PHILOSOPHY.md`
(showreel pacing is its fast sizzle mode) and `video-storytelling` for
persistent-world camera moves. Build one `index.html` with one paused GSAP timeline.
Chapters are timed `.clip` layers, and the HUD sits on top.

- Every time comes from the beat sheet: `const B = (n) => n * PERIOD`.
- Put a **per-frame driver** on the timeline and make it a pure function of time:
  `tl.fromTo(drv, {t:0}, {t:END, duration:END, ease:'none', onUpdate:() => frame(drv.t)}, 0)`.
  Draw canvas effects (particles, noise, big grids) there from seeded values, never
  from `Math.random()` at draw time. Drive the HUD from the same function.
- Tween only transforms and opacity. Never tween `left/top/width/height`. To morph
  a dot into a tile, draw the final tile and scale it down into a circle
  (`border-radius: 128px / 72px` on a 256x144 tile), then tween back to scale 1.
- A property animated by several tweens across the reel (a shared flash layer)
  can stick on a backward seek. Compute it in the per-frame driver instead, and
  do the same for class swaps like an invert.
- Measure layout (`getBoundingClientRect`) once, at the top of the build, before
  any `immediateRender` tween applies a transform. Never measure inside `onUpdate`.
- `<video data-start>` must not sit inside a timed `.clip`. Put videos in an
  untimed wrapper, which you can still scale for push-ins.
- Staggered phases must finish before their cut: latest completion = start + max
  delay + duration. Check it on paper, then in a render strip.
- `background-clip: text` renders invisible in capture. Use solid fills and
  `text-shadow` for bloom.

### 8. Verify before calling it done

- `npx hyperframes lint`, then Studio preview, then a draft render (`hyperframes-cli`).
- Run `analyze-reference.mjs` on your own render with `--bpm` and `--phase`: cut
  offsets must be within about 35 ms of a beat or half beat, luminance must
  alternate by chapter, and the audio must show the pre-drop dip.
- Extract 10-frame strips across every transition and look at them. Snapshots
  miss stuck or ghost layers:
  `ffmpeg -i render.mp4 -vf "select='between(n\,440\,449)',scale=384:-1,tile=layout=5x2" -frames:v 1 -fps_mode passthrough strip.png`
- Brand test: pick 6 random frames. Each must read as the brand with the HUD covered.
- Loudness is about -14 LUFS. HyperFrames re-encodes audio slightly quieter, so
  remux `master.wav` into the render (see the header of `mix.mjs`).
- Save the evidence in `VERIFY.md`.

## Example brief

The skill's first test was a 15s YouTube reel: the red scrubber dot bounces on a
progress bar, scrubs into a laser, types "broadcast yourself" into a rebuilt search
bar, becomes eight dots, then a feed of real thumbnails, and bursts from a like button
into particles that spell a verified stat. It becomes a lacquer play button and a
Silver Creator Award, runs a flurry of Subscribe, Shorts, LIVE, Skip, and "+10
seconds", and lands as the play icon in the logo. Use it as a model for mapping
chapters to a brand's native objects, not as a template to copy.
