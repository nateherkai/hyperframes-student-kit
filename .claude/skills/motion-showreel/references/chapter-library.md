# Chapter library

Each entry covers the technique, how the reference used it, how to build it seek-safe in HyperFrames (GSAP on one paused timeline), and brand swaps. Pick 5-7 and chain them so each one's out-transform is the next one's in-transform.

## Physics: squash and stretch
- **Reference:** a red dot falls onto a tick ruler and bounces three times, with a ground ellipse and a POS/SCL/VEL readout on a leader line.
- **Build:** hand-key the bounce from the beat sheet (a contact on each beat). Fall uses `power2.in`, rise uses `power2.out`. On contact, set `scaleX 1.35 / scaleY 0.7` for 2-3 frames, then `elastic.out(1, 0.5)` back. While falling fast, stretch to `scaleY 1.3`. Compute the readout text in an `onUpdate` from the dot's current `y` and velocity (the difference from the previous frame), formatted to one decimal.
- **Out-transform:** the dot accelerates sideways into a laser line (`scaleX` to 200, `height` 4px, glow), which blooms to a full-frame flash (a white layer at opacity 1 for 2 frames), then becomes the paper of the next chapter.
- **Swaps:** a video scrubber dot on a progress bar (YouTube), a cursor dot (a SaaS app), a drop of liquid (a drink brand), a pin (maps).

## Kinetic type
- **Reference:** letters drop in out of order with overshoot and motion blur. A red selection box with W/H/SX numbers and a cursor drags the word bigger. A red italic serif aside plays against heavy grotesk caps. The key word repeats into outline wallpaper, which turns diagonal with red bands, then the frame inverts.
- **Build:** split words into `<span>`s. Stagger `y: -120 -> 0` with `back.out(2)`, 1-frame offsets in a shuffled order. Fake motion blur by tweening `filter: blur(6px) -> 0` together with a `scaleY` stretch. For the selection box, an absolutely positioned div with 8 handle squares follows the word's box (read the width once after `document.fonts.ready`) and a cursor SVG moves along. For wallpaper, generate 12 rows of the word with `-webkit-text-stroke` (outline). Rotate the container -12deg, slide alternate rows in opposite directions, and fill 2 rows with the accent. For the invert, one `tl.set` swaps a background layer and the text colors on the beat.
- **Swaps:** a search bar that types the phrase (YouTube, Google), a chat input (AI products), a price tag, a headline from the brand's first slogan.

## Letters to dots to grid (shape language)
- **Reference:** letters of DECISION become red dots one by one, the dots line up in a row of 8, and the row becomes a full-frame grid. A red wave ripples, circles morph to squares, then crosses, then triangles, and the camera tilts and pushes in.
- **Build:** a grid of divs (for example 16x9) with `border-radius`. The wave is a function of time and distance from an origin: in `onUpdate`, for each cell, `phase = t*speed - dist`, then set its scale, color mix, and radius from `phase`. That is seek-safe because it is a pure function of `t`. Shape morphs are `border-radius` 50% to 8% and a `clip-path` polygon. The camera is a parent with `perspective` and `rotateX`/`rotateZ`.
- **Swaps:** a 16:9 thumbnail grid (YouTube) with real images fading into cells, app icons, product SKUs, a pixel mosaic of the logo.

## Particle system
- **Reference:** a lens iris flashes on the midpoint drop, particles burst in red, white, and blue on navy, swirl, and condense into a ring.
- **Build:** one `<canvas>` of 2,000-4,000 particles. Precompute seeded start positions and targets (any shape: a ring, a logo from sampled pixels of an image, a number). Draw every particle from `lerp(start, target, ease(clamp((t - t0)/d - delay_i)))` plus a curl offset `sin(i*1.7 + t*3)*amp*(1 - progress)`. Redraw in a proxy tween's `onUpdate` so the frame is a pure function of `tl.time()`. Use additive blending (`globalCompositeOperation = 'lighter'`) for glow.
- **Out-transform:** particles condense into the silhouette of the next chapter's hero object, then the real object crossfades in within 2-3 frames of a flash.
- **Swaps:** a like-button burst (social), confetti of product colors, data points, stars.

## Lookdev / hero object
- **Reference:** an iridescent chrome torus SDF-morphs into blobs and a cube, with a parameter readout (SDF, SMOOTH UNION, MORPH, IOR, ROUGH), and pushes into the lens.
- **Build:** a generated photoreal still (seedream i2i from the logo) plus a Kling camera move, sped up about 3x and re-encoded at 60fps all-intra. For a second material, cut or crossfade to another material of the same object (lacquer to chrome, silver to gold). Put a readout on a leader line with numbers that count up in `onUpdate`. The out push is `scale 1 -> 3` plus `blur 0 -> 20px` over the last half beat, with a hard cut on the beat.
- **Swaps:** a creator award plaque (YouTube), a bottle or can, a device, a logo sculpture.

## Easing graph
- **Reference:** a cubic-bezier(0.83, 0, 0.17, 1) curve on paper, with a ball riding it and leaving onion-skin ghosts.
- **Build:** an SVG path with `stroke-dasharray` draw-on. The ball position comes from evaluating the bezier at `ease(t)`, and the ghosts are 8 copies at earlier times with falling opacity.
- **Swaps:** a growth curve of a brand metric, a playback-speed curve.

## Flurry (4 beats, about 6 cuts)
- **Reference:** Easing, then Op Art (stripes plus target), Glitch ("REEL" RGB split), Isometric blocks, Symmetry (kaleidoscope), and pixel noise, cut on beats and then half beats, introducing the held-back blue.
- **Build:** each cut is a full-bleed layer shown by `tl.set` on its grid time with one internal move (a spin, slide, scale pop, or stutter). Glitch uses 3 copies of the text (red, cyan, and white) offset by a few px with `mix-blend-mode: screen`, plus 4-6 horizontal slices (`clip-path: inset()`) jittered on alternating frames. Noise is a canvas of big pixels in brand colors, seeded per frame.
- **Swaps:** each flurry frame is one brand signature UI moment at full bleed (YouTube: Subscribe click, a Shorts swipe, a LIVE badge, Skip Ad, a double-tap +10s, a 4K/HD badge).

## Lockup (end card)
- **Reference:** the wordmark resolves from noise with bloom, a rule draws beneath it, two mono subtitles type on with a red block cursor, the motif lands as the period with a squash and a ground ellipse, and the tagline fades in last at low opacity.
- **Build:** the noise canvas fades as the wordmark's `filter: blur(20px) -> 0` and `opacity` rise over 12 frames, and bloom is a `text-shadow` or `drop-shadow`. The rule is `scaleX 0 -> 1` from the left. For typing, reveal characters with a `steps()` tween on a width mask, or `tl.set` per character, and a blinking block via `tl.set` toggles every 16 frames. The motif fall reuses the physics chapter's contact keys.
- **Swaps:** the motif becomes the logo's own element (a scrubber dot becomes the play button, a dot becomes the i's tittle, a drop becomes the O).
