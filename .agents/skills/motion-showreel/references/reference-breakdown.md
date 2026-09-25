# Reference breakdown: the Opus 5.5 "CLAUDE / MOTION REEL"

Source: a 15-second motion reel made by Opus 5.5 for Nate Herk (September 2026). 1920x1080, 60fps, 15.06s, 900 frames. Analyzed with `scripts/analyze-reference.mjs` (6fps contact sheets, per-frame luminance difference, audio RMS, and onsets).

## Measured facts

- **Tempo:** 128 BPM (beat = 0.469s). Onsets at 2.39, 2.86, 3.32, 4.25, 4.71, 5.20, 5.67, 6.13 ... are exactly one beat apart. Grid anchor about 0.51s.
- **Hard cuts land on beats:** 1.77 (flash), 4.23 (invert), 7.50 (iris flash), 11.25, 11.73, 12.20, 12.43 (half beat), 12.67, 12.93 (half beat), 13.13. Every one is within 2 frames of a grid line.
- **Pre-drop dip:** audio falls from about -12 dB to -25 dB at 7.25s, then the iris flash hits at 7.50s. One gap, one hit, at the midpoint.
- **Luminance rhythm (mean 0-255, every 0.5s):** 11, 11, 14, 219, 212, 224, 190, 65, 48, 14, 17, 97, 98, 71, 22, 22, 21, 54, 46, 37, 223, 95, 109, 40, 22, 31, 32. Dark, paper, dark, saturated, navy, paper, saturated flurry, black. Chapter changes flip value.
- **Audio level:** music bed at about -12 dB RMS the whole way. No voiceover. Fade out in the last 0.25s.

## Timeline

| Time | HUD label | What happens | Out-transition |
|---|---|---|---|
| 0.00-1.78 | 01 Squash & Stretch | One red dot drops onto a tick ruler and bounces. It stretches on the fall and squashes on contact, and a ground ellipse ripples. A leader line carries a live readout (POS, SCL, VEL). | The dot smears into a horizontal red laser, the laser blooms to white, and the white becomes the paper of the next chapter. |
| 1.78-4.23 | 02 Kinetic Type | "EVERY" letters drop in with bounce and overshoot. "FRAME" gets a red design-tool selection box (W 929, H 282, SX 100.0%) and a cursor that drags it bigger. "is a" arrives in red italic serif. "DECISION" letters land out of order with motion blur, then the word repeats into outline wallpaper. | The wallpaper rotates into diagonal bands, some bands fill red, and the whole frame inverts to black on a beat. |
| 4.23-5.30 | (02 continued) | White "DECISION" glows on black. Its letters turn into red dots one at a time. | Dots become a row of 8. |
| 5.30-7.40 | 03 Shape Language | The row of dots becomes a full-frame grid. A red wave ripples through it, circles morph to squares, squares to crosses, crosses to triangles, and the camera tilts and pushes into the grid. | The grid tunnels into a lens iris. |
| 7.40-9.30 | 04 Particle Systems | An iris ring flashes (the drop), a burst of red, white, and blue particles swirls on navy, and then it condenses into a thin ring. | The particle ring solidifies into a chrome torus. |
| 9.30-11.25 | 05 Lookdev / SDF | An iridescent chrome torus tilts, then SDF-smooth-unions into blobs, then a cube. A readout tracks it (SDF, SMOOTH UNION, MORPH 0.000 to 1.994, IOR 1.40, ROUGH 0.02). | The cube pushes into the lens. Hard cut. |
| 11.25-11.73 | 06 Easing | A cubic-bezier(0.83, 0, 0.17, 1) graph on paper. A red ball rides the curve and leaves onion-skin ghosts. | Cut on the beat. |
| 11.73-12.20 | Op Art | Red and black diagonal stripes behind a blue-and-white striped target. | Cut. |
| 12.20-12.43 | Glitch | "REEL" in white on electric blue with RGB split and slice displacement. | Cut on the half beat. |
| 12.43-12.67 | Isometric | Blue and white isometric block field on red. | Cut. |
| 12.67-12.93 | Symmetry | A kaleidoscope of red and blue circles and white triangles around a ring. | Black-to-blue wipe. |
| 12.93-13.13 | (noise) | Red, blue, and white pixel noise fills the frame. | The noise resolves into the wordmark. |
| 13.13-15.06 | 07 Fin | "CLAUDE" resolves from noise with bloom. A rule draws under it. "MOTION DESIGN" and "SHOWREEL 2026" type on with a red block cursor. The red dot falls in as the period with a squash and a ground ellipse. The tagline "EVERY FRAME WRITTEN IN CODE" fades in last, dim. | Hold, then fade. |

## Persistent HUD (every frame)

- Corner crop marks, 30px arms, inset about 36px.
- Top left: `CLAUDE  /  MOTION REEL`. Top right: `● 1920×1080 · 60P · 128 BPM`. The dot blinks like a REC light.
- Bottom left: `TC 00:00:02:36` running timecode. Bottom center: a tick ruler that fills as a progress bar. Bottom right: `02 · KINETIC TYPE` (the reel uses a dash between number and name).
- Mono, all caps, tracking about 0.2em, about 16px, 85% white on dark or 85% ink on paper. The HUD flips color with the background.
- A faint dot grid covers the dark frames.

## Why it works

1. **One protagonist, transformed.** The red dot is a ball, then a laser, then letters, dots, a grid, particles, a ring, a torus, and a cube, and at the end it is the period. Nearly every transition turns the current object into the next one. The viewer never has to reorient, so 15 seconds feel like one continuous thought.
2. **The reel narrates its own craft.** Chapter labels name the discipline on screen. Tool overlays (the physics readout, the selection box with a cursor, SDF parameters, a bezier graph) show the work behind the frame. It reads as a designer's reel, not an ad.
3. **A small palette, with one color held back.** Ink, paper, and one red carry the first 11 seconds. Electric blue appears only in the climax flurry, so the new color feels like the drop.
4. **Value flips on the beat.** Chapter changes swap dark and light or neutral and saturated. The flash, invert, and iris cuts are the punches, and they all land on grid lines.
5. **An accelerating cut curve with a held ending.** Chapter lengths run 1.8s, 3.5s (with an internal invert), 2.1s, 1.9s, 1.9s. Then six cuts come in 1.9s at one beat and half-beat spacing, and a 1.9s lockup lets the eye rest. That is roughly 75% development, 13% flurry, and 12% resolve.
6. **Density breathes.** One dot, then one word, then a wall of words, a grid of 100, thousands of particles, one object, the flurry, and one word again. Few and many alternate.
7. **Three type voices.** Heavy grotesk caps for statements, red italic serif for the human aside, and wide-tracked mono for the machine layer. Type also works as image: repeated into wallpaper, banded, and inverted.
8. **Physical finish.** Squash and stretch, motion blur on fast letters, bloom on white-on-black, slight chromatic fringing, grain, vignette, and a lens iris. It feels shot, not exported.
9. **Scale jumps.** Macro dot, full-frame pattern, cosmic particle field, object close-up, and a push through the object into the next cut. The camera move becomes the edit.
10. **A bookend.** The first object returns as the final punctuation, and the tagline arrives last at low opacity. The ending answers the opening.
