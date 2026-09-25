#!/usr/bin/env node
// Splice a music take onto the cut grid, beat-accurate, with ffmpeg.
//
// Usage:
//   node splice-music.mjs <take.mp3> --period 0.4644 --phase 0.073 \
//     --segments "4-28,48-56.7" --length 15 --gap 16 --fade 0.9 --out assets/audio/music-bed.wav
//
// --period/--phase  from music-grid.mjs (use the KICK-band phase)
// --segments        source beat ranges, played in order. Output beat 0 = the first segment's start.
//                   Typical 15s reel at ~129 BPM: intro + build (16 beats) ending on the drop's
//                   downbeat, drop (8), break (4, under the flurry), then the return hit + tail.
// --gap N           duck the half beat before OUTPUT beat N to -16 dB (the pre-drop gap)
// --fade S          fade the last S seconds
// Every cut lands 12 ms before a grid point so the transient survives, joined by a 12 ms
// crossfade; each segment but the last is extended by the crossfade so beats stay on the grid.
// Re-measure the result with music-grid.mjs: its kick phase should be close to 0.
import { spawnSync } from 'node:child_process';

const args = process.argv.slice(2);
const get = (n, d) => { const i = args.indexOf(`--${n}`); return i >= 0 ? args[i + 1] : d; };
const take = args[0];
const P = Number(get('period')), PH = Number(get('phase', 0)), LEN = Number(get('length', 15));
const segs = String(get('segments', '')).split(',').filter(Boolean).map((s) => s.split('-').map(Number));
const gap = get('gap') !== undefined ? Number(get('gap')) : null, fade = Number(get('fade', 0.9)), out = get('out', 'music-bed.wav');
if (!take || !P || !segs.length) { console.error('Usage: node splice-music.mjs <take> --period <s> --phase <s> --segments "a-b,c-d" [--length 15] [--gap 16] [--fade 0.9] [--out bed.wav]'); process.exit(1); }

const PRE = 0.012, XF = 0.012;
const t = (beat) => Math.max(0, PH + beat * P - PRE);
const parts = segs.map(([a, b], i) => `[0:a]asetpts=PTS-STARTPTS,atrim=start=${t(a).toFixed(5)}:end=${(t(b) + (i < segs.length - 1 ? XF : 0)).toFixed(5)},asetpts=PTS-STARTPTS[s${i}]`);
let chain = '[s0]';
for (let i = 1; i < segs.length; i++) { parts.push(`${chain}[s${i}]acrossfade=d=${XF}:c1=qsin:c2=qsin[x${i}]`); chain = `[x${i}]`; }
const post = [`apad=whole_dur=${LEN}`, `atrim=0:${LEN}`];
if (gap !== null) { const g0 = (gap - 0.5) * P, g1 = gap * P - 0.004; post.push(`volume=0.158:enable='between(t,${g0.toFixed(4)},${g1.toFixed(4)})'`); }
if (fade > 0) post.push(`afade=t=out:st=${(LEN - fade).toFixed(3)}:d=${fade}`);
parts.push(`${chain}${post.join(',')}[out]`);
const r = spawnSync('ffmpeg', ['-v', 'error', '-y', '-i', take, '-filter_complex', parts.join(';'), '-map', '[out]', '-ar', '48000', '-ac', '2', '-c:a', 'pcm_s24le', out], { encoding: 'utf8' });
if (r.status !== 0) { console.error(r.stderr); process.exit(1); }
console.log(`${out}: ${segs.map(([a, b]) => `src beats ${a}-${b}`).join(' + ')}, ${LEN}s${gap !== null ? `, gap before beat ${gap} (${(gap * P).toFixed(3)}s)` : ''}`);
