# Render-safe energy effects

The "keep them watching" layer: grain, vignette, progress bar, section ticker, transition flashes,
count-up numbers, word-pop captions, a slow push. These live in the root `index.html` timeline (or
in the caption/callout sub-comps). Tune them subtle for a tutorial/build video, stronger for a hype
edit — the user will tell you which.

## The one rule that breaks renders: seek-safety

Hyperframes renders by seeking the master timeline to each frame's time and reading the DOM — it
does **not** play in real time. This means:

- ✅ **Property tweens (`tl.to`/`tl.from`/`tl.fromTo`) and `tl.set`** apply on every seek. Use these.
- ✅ **`onUpdate`** fires when a tween renders during a seek — so the count-up (which sets
  `textContent` in `onUpdate`) works. Verified: a callout reads `48″` mid-count and `60″` settled.
- ❌ **`tl.call(...)` callbacks do NOT fire on seek.** Anything driven by `tl.call` (e.g. swapping
  text) will be missing in the render. To change discrete state over time, use **separate elements
  toggled by opacity tweens** instead (see the section ticker below), never `tl.call`.

Also keep it deterministic: no `Math.random()`, `Date.now()`, or `repeat: -1` (compute a finite
`repeat` count). These are general Hyperframes rules but easy to violate when adding "flair".

## z-index ordering (root composition)

```
video (0) < grain/vignette (10) < captions (20) < callouts (25) < progress/ticker (55) < flash (58) < section cards (60)
```

## Recipes

### Film grain + vignette (always-on texture)
```html
<div id="grade-layer"><div id="grain"></div><div id="vignette"></div></div>
```
```css
#grade-layer{position:absolute;inset:0;z-index:10;pointer-events:none;}
#vignette{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 46%,
  rgba(0,0,0,0) 52%, rgba(8,10,14,0.30) 84%, rgba(8,10,14,0.58) 100%);}
#grain{position:absolute;inset:-40%;width:180%;height:180%;opacity:0.07;mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  background-size:280px 280px;will-change:transform;}
```
```js
// marching grain — finite repeat, steps ease gives the shimmer
tl.to("#grain",{x:-34,y:-30,duration:0.5,ease:"steps(5)",repeat:Math.ceil(DUR/0.5),yoyo:true},0);
```

### Progress bar (scaleX, not width — cheaper + smoother)
```css
#progress{position:absolute;top:0;left:0;height:5px;width:100%;transform:scaleX(0);
  transform-origin:left center;background:#e8913c;z-index:55;box-shadow:0 0 12px rgba(232,145,60,0.6);}
```
```js
tl.fromTo("#progress",{scaleX:0},{scaleX:1,duration:DUR,ease:"none"},0);
```

### Section ticker (opacity-toggled spans — NOT tl.call)
```html
<div id="ticker"><span id="tk1">Build Log&nbsp;&nbsp;01 / 03</span>
  <span id="tk2">Build Log&nbsp;&nbsp;02 / 03</span><span id="tk3">Build Log&nbsp;&nbsp;03 / 03</span></div>
```
```js
tl.set(["#tk1","#tk2","#tk3"],{opacity:0},0);
tl.to("#tk1",{opacity:1,duration:0.5},3.0);  tl.to("#tk1",{opacity:0,duration:0.3},SEC2-0.4);
tl.to("#tk2",{opacity:1,duration:0.5},SEC2+3.2); tl.to("#tk2",{opacity:0,duration:0.3},CLAP-0.4);
tl.to("#tk3",{opacity:1,duration:0.5},CLAP+3.2); tl.to("#tk3",{opacity:0,duration:0.3},END-0.5);
```

### Transition flash (punch a cut — e.g. on a clap)
```css
#flash{position:absolute;inset:0;z-index:58;background:#fff;opacity:0;pointer-events:none;}
```
```js
tl.to("#flash",{opacity:0.55,duration:0.10,ease:"power2.out"},CLAP-0.08);
tl.to("#flash",{opacity:0,   duration:0.40,ease:"power2.in"}, CLAP+0.02);
```

### Slow push (Ken Burns on a locked shot)
```js
// animate the non-timed wrapper, never the <video> element itself
tl.fromTo("#video-wrapper",{scale:1.0},{scale:1.06,duration:DUR,ease:"none"},0);
```

### Count-up numbers (callouts) — see build_overlays.py
Parse `value` into prefix/digits/suffix, tween a proxy `{v:0}` to the number, and set
`textContent = pre + Math.round(v) + suf` in `onUpdate`. Snap the final value with the card so a
scrub past the count still shows the right number.

### Word-pop captions — see build_overlays.py
Set each word span `{opacity:0,y:16,scale:0.82}` then `tl.to(spans,{...,stagger:0.04,ease:"back.out(1.8)"})`
at the group's start. `.cap-word{display:inline-block}` is required for transforms on inline text.

## Section cards

Solid full-frame `.card` overlays (z 60). The intro card starts `opacity:1` (it covers frame 0 —
the linter's `gsap_fullscreen_overlay_starts_visible` flag is a known false-positive here, verified
fine in the render). Mid-film cards start hidden and fade in on the section beat / clap; give the
title a `back.out(1.4)` for a little snap. Only the final/outro card may animate elements OUT.
