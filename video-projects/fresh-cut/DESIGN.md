# fresh-cut — Design Spec

**Project:** A DIY/woodworking build video — cutting trim pieces (1×2s) for a project,
measuring boards, planning 45° miter cuts. Tutorial / "build-with-me" tone.

## Style Prompt

Clean workshop documentary. Warm, grounded, precise. The motion graphics feel like a
blueprint laid over real footage: tidy mono labels, dimension lines, measurement callouts
that snap in exactly when a number is spoken. Restrained and confident — let the footage
breathe, the graphics annotate. No flashy social-media energy; this is a craftsperson
showing their work.

## Colors

| Token            | Hex       | Role                                                  |
| ---------------- | --------- | ----------------------------------------------------- |
| `--ink`          | `#0e1116` | Panel / scrim background (deep charcoal)              |
| `--paper`        | `#f4efe6` | Primary text (warm white)                             |
| `--amber`        | `#e8913c` | Accent — numbers, saw-blade warmth, emphasis          |
| `--blueprint`    | `#5cc6d6` | Technical labels, dimension lines, units              |
| `--muted`        | `#9aa3ad` | Secondary labels, de-emphasized text                  |

Five symbolic colors max. Amber = "the measurement that matters." Blueprint cyan =
"the technical annotation." Everything else is ink/paper/muted.

## Typography

- **Roboto Mono** (500/700) — all numbers, units, technical labels, callout cards.
- **Inter** (600/700) — caption body text.

`font-variant-numeric: tabular-nums` on every number so digits don't jitter.

## Motion

- Callouts: snap in with a short `power3.out` slide + scale-settle (~0.35s), hold ~2.2s,
  exit on a quick `power2.in` fade. Dimension line draws via `scaleX` from 0.
- Captions: fade + 12px rise, `power2.out`, ~0.22s in. One group at a time, hard kill at end.
- Title / outro: calm fades. Hold the outro 3–4s (breathing room).
- No hard cuts between graphic beats — graphics fade, the footage is continuous.

## What NOT to Do

1. No bright/playful "TikTok" caption pills or bouncy elastic word pops.
2. Don't cover the subject's face — callouts live in the upper-left, captions in the bottom band.
3. No full-screen linear gradients on the footage (H.264 banding) — use a bottom scrim only.
4. Don't animate the `<video>` element directly — wrap it.
5. No more than one measurement callout on screen at a time.
