---
name: cut-mistakes
description: "Agent 2 of the video editing pipeline. Finds and removes spoken mistakes — stutters, repeated words, false starts, and retakes (re-recorded lines) — from a talking-head recording. Use after cut-silences, when asked to cut mistakes, remove stutters / repeats / filler restarts, clean up flubs, or keep the best take. Works review-gated: it proposes every cut with context and a reason for approval, then renders only the approved cuts via ffmpeg. Requires a word-level transcript."
---

# Cut Mistakes & Repeats (Pipeline Agent 2)

Second step of the automated edit, run after **cut-silences**. It removes the things a human editor cuts on a second pass: stutters ("the the", "I- I-"), immediately repeated words, false starts (an abandoned phrase that restarts), and retakes (a line re-recorded — keep the clean take, drop the botched one).

Deciding what counts as a mistake is **judgment, not a formula** — emphatic repetition ("never, never") and rhetorical doubling ("the first piece is, is this…") look identical to a stutter mechanically. So this agent is **review-gated by default**: it surfaces candidates with full context; the agent (and the user) decide; only approved cuts are rendered.

## When to use

- "cut the mistakes", "remove stutters / repeats", "clean up the flubs", "keep the best take", "cut false starts"
- As the second stage of the master edit workflow, on cut-silences' output.

## The three-part flow

### 1. Find candidates (mechanical)

```bash
node .claude/skills/cut-mistakes/scripts/find-cut-candidates.mjs \
  <silence-transcript.json> --out-dir video-projects/<slug>/assets
```

Input is normally Agent 1's `<stem>.silence-transcript.json`, so cuts land on the already-silenced timeline. Writes:

- `<stem>.cut-candidates.json` — structured candidates (type, confidence, proposed `cut` range, `removes`/`keeps` text, context, recommendation)
- `<stem>.cut-candidates.md` — readable proposal

Candidate types: `stutter` (immediate word repeat), `retake` (duplicate/near-duplicate segment via Jaccard similarity), `false_start` (short abandoned phrase that restarts).

### 2. Review (the gate — REQUIRED)

Read each candidate **in context** and decide keep-or-cut. The mechanical detector cannot tell intentional emphasis/rhetoric from a real flub, so do not trust `recommend` blindly — read `removes` + `context`. Common false positives: emphatic repetition ("it's never, never hands-off"), copula-then-question ("the piece is, is this…"), listing.

Present the candidates to the user with a recommendation per item; collect approvals. Write the approved cuts to a file:

```json
{ "cuts": [ { "start": 100.93, "end": 101.06, "reason": "I- false start" }, ... ] }
```

(`start`/`end` in seconds on the input transcript/video timeline. You can widen a candidate's range — e.g. for a retake, cut from the botched take's start to the clean restart.)

### 3. Apply approved cuts

```bash
node .claude/skills/cut-mistakes/scripts/apply-cuts.mjs \
  <silence-transcript.json> --cuts approved-cuts.json \
  --video video-projects/<slug>/assets/edited-silenced.mp4 \
  --output video-projects/<slug>/assets/edited-clean.mp4 --apply
```

Writes the EDL, a re-timed `<stem>.mistakes-transcript.json` (feeds the motion-graphics agent + `validate-beat-sync.mjs`), a decisions log, and — with `--apply` — the cut video (ffmpeg trim+concat, A/V in sync). Drop `--apply` for a dry run.

## Reviewing the result

Use the shared review tool to eyeball the cuts and spot-check boundaries:

```bash
node scripts/build-edl-review.mjs <stem>.mistakes-edl.json \
  --original video-projects/<slug>/assets/edited-silenced.mp4 \
  --edited   video-projects/<slug>/assets/edited-clean.mp4 \
  --output   video-projects/<slug>/assets/mistakes-review.html
npx serve . -p 8080 -n
```

## Known limitation: retimed-transcript precision (read before reusing timestamps downstream)

`apply-cuts.mjs` computes `<stem>.mistakes-transcript.json`'s word timings by
exact float subtraction, then feeds those same floats to ffmpeg's
`trim`/`atrim`. ffmpeg can only cut on real frame boundaries, so each cut's
actual rendered position can differ from the math by a fraction of a frame,
and — because this runs after `cut-silences`, which typically makes 100-300+
cuts of its own — the error compounds across two stages. The script now
snaps every cut boundary to the nearest real frame (via `ffprobe`'s
`r_frame_rate` when `--video` is given) before computing anything, which
substantially reduces drift, but testing found it does not fully eliminate
it on real camera footage (frame spacing isn't perfectly uniform) — expect
low-single-digit milliseconds of residual drift per cut, which can still add
up to a noticeable offset (measured: ~0.3s across 45 cuts on real footage)
on a file with many cuts.

**Practical rule**: if you need this transcript's timestamps to point at
exact words in the *rendered* video — for another cutting pass, a beat-sync
tool, or anything requiring frame-accurate timing — do not trust
`<stem>.mistakes-transcript.json` on its own once more than a few dozen cuts
have been applied (by this tool or by `cut-silences` before it). Re-transcribe
the actual rendered video directly for the region you need, and — before
calling any such downstream cut "done" — re-transcribe the *final render*
and diff it against the intended text. Frame strips / contact sheets alone
cannot catch this: a locked-off single-camera shot looks identical a second
early.

## Notes

- A very clean delivery may yield few or zero real cuts — that's a valid outcome; don't cut natural speech to hit a quota.
- Cuts between two spoken words are hard joins. They're usually clean for stutters/false starts; for tighter audio a 20-30ms fade can be added later.
- Hand the `mistakes-transcript.json` + the clean video to **Agent 3 (motion graphics / tiered cards)**.
