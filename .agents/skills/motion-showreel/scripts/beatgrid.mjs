#!/usr/bin/env node
// Lay chapters on a beat grid and print the cut sheet (seconds and frames).
//
// Usage:
//   node beatgrid.mjs --period 0.4644 --fps 60 --length 15 \
//     --chapters "01 Physics:4, 02 Kinetic Type:8, 03 Grid:4, 04 Drop:4, 05 Lookdev:4, Flurry:4, 07 Fin:rest"
//
// A chapter length is in beats; "rest" fills to --length. Inside a chapter whose name
// starts with "Flurry", cuts are listed one per beat, then one per half beat.
// The default split matches the reference reel: about 75% development, 13% flurry,
// 12% resolve. Paste the output into STORYBOARD.md; in GSAP, t = frame / fps.
const args = process.argv.slice(2);
const get = (name) => { const i = args.indexOf(`--${name}`); return i >= 0 ? args[i + 1] : undefined; };
const bpm = Number(get('bpm') ?? 0), period = Number(get('period') ?? 0);
const fps = Number(get('fps') ?? 60), length = Number(get('length') ?? 15), chapters = get('chapters');
if (!chapters || !(period || bpm)) {
  console.error('Usage: node beatgrid.mjs (--period <s> | --bpm <n>) [--fps 60] [--length 15] --chapters "Name:beats, ..., Name:rest"');
  process.exit(1);
}
const P = period || 60 / bpm;
const fr = (t) => Math.round(t * fps);
const pad = (s, w) => String(s).padStart(w);
console.log(`beat ${P.toFixed(4)}s (${(60 / P).toFixed(2)} BPM), ${fps} fps, beat = ${(P * fps).toFixed(2)} frames\n`);
console.log(`${'chapter'.padEnd(24)} ${pad('beats', 11)} ${pad('start s', 8)} ${pad('end s', 8)} ${pad('frames', 11)}`);
let b = 0;
for (const part of chapters.split(',').map((c) => c.trim()).filter(Boolean)) {
  const k = part.lastIndexOf(':');
  const name = part.slice(0, k).trim(), n = part.slice(k + 1).trim();
  const t0 = b * P;
  const nb = n === 'rest' ? length / P - b : Number(n);
  const t1 = n === 'rest' ? length : (b + nb) * P;
  console.log(`${name.padEnd(24)} ${pad(`${b.toFixed(1)}-${(b + nb).toFixed(1)}`, 11)} ${pad(t0.toFixed(3), 8)} ${pad(t1.toFixed(3), 8)} ${pad(`${fr(t0)}-${fr(t1)}`, 11)}`);
  if (name.toLowerCase().startsWith('flurry')) {
    // one beat per cut, then half beats: the cut rate accelerates into the lockup
    for (let s = 0; s < nb - 1e-6; s += s < nb / 2 ? 1 : 0.5) console.log(`${'  cut'.padEnd(24)} ${pad((b + s).toFixed(1), 11)} ${pad(((b + s) * P).toFixed(3), 8)} ${pad('', 8)} ${pad(fr((b + s) * P), 11)}`);
  }
  b += nb;
}
console.log(`\ntotal ${length.toFixed(2)}s = ${fr(length)} frames`);
