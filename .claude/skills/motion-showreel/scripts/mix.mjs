#!/usr/bin/env node
// Premix the music bed and beat-placed SFX into one master wav with ffmpeg.
//
// Usage: node mix.mjs --bed music-bed.wav --events events.json --out master.wav [--length 15] [--lufs -14] [--bed-gain 0.9]
//   events.json: [{ "t": 0.4644, "file": "assets/audio/sfx/dot_pop.mp3", "gain": 0.5, "max": 0.5 }, ...]
//   t      seconds (compute from the beat sheet: beat * period)
//   gain   linear gain on the cue as generated (start around 0.2-0.6; hero hits up to 0.9)
//   max    optional: trim a long cue to this many seconds, with a 40 ms fade
// Two-pass loudnorm to --lufs (default -14 LUFS, -1.2 dBTP). Place the result as the single
// <audio> track of the composition. HyperFrames re-encodes audio slightly quieter; after
// rendering, remux the master: ffmpeg -i render.mp4 -i master.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest final.mp4
import { spawnSync } from 'node:child_process';
import { readFileSync } from 'node:fs';

const args = process.argv.slice(2);
const get = (n, d) => { const i = args.indexOf(`--${n}`); return i >= 0 ? args[i + 1] : d; };
const bed = get('bed'), eventsFile = get('events'), out = get('out', 'master.wav');
const LEN = Number(get('length', 15)), LUFS = Number(get('lufs', -14)), BED = Number(get('bed-gain', 0.9));
if (!bed || !eventsFile) { console.error('Usage: node mix.mjs --bed bed.wav --events events.json --out master.wav'); process.exit(1); }
const events = JSON.parse(readFileSync(eventsFile, 'utf8'));

const inputs = ['-i', bed], parts = [`[0:a]aresample=48000,volume=${BED}[b]`], labels = ['[b]'];
events.forEach((e, i) => {
  inputs.push('-i', e.file);
  const trim = e.max ? `atrim=0:${e.max},afade=t=out:st=${Math.max(0, e.max - 0.04)}:d=0.04,` : '';
  const ms = Math.round(e.t * 1000);
  parts.push(`[${i + 1}:a]aresample=48000,aformat=channel_layouts=stereo,${trim}volume=${e.gain},adelay=${ms}|${ms}[e${i}]`);
  labels.push(`[e${i}]`);
});
parts.push(`${labels.join('')}amix=inputs=${labels.length}:normalize=0:duration=first,atrim=0:${LEN}[m]`);
const graph = parts.join(';');
const ff = (tail, extra) => spawnSync('ffmpeg', ['-hide_banner', ...inputs, '-filter_complex', graph + tail, ...extra], { encoding: 'utf8', maxBuffer: 1 << 26 });

// pass 1: measure
const m = ff(`;[m]loudnorm=I=${LUFS}:TP=-1.2:LRA=11:print_format=json[o]`, ['-map', '[o]', '-f', 'null', '-']);
if (m.status !== 0) { console.error(m.stderr.slice(-800)); process.exit(1); }
const js = JSON.parse(m.stderr.slice(m.stderr.lastIndexOf('{'), m.stderr.lastIndexOf('}') + 1));
// pass 2: normalize linearly, then a safety limiter
const af = `loudnorm=I=${LUFS}:TP=-1.2:LRA=11:measured_I=${js.input_i}:measured_TP=${js.input_tp}:measured_LRA=${js.input_lra}:measured_thresh=${js.input_thresh}:offset=${js.target_offset}:linear=true,alimiter=limit=0.87:level=false,aresample=48000`;
const r = ff(`;[m]${af}[o]`, ['-v', 'error', '-y', '-map', '[o]', '-t', String(LEN), '-c:a', 'pcm_s24le', out]);
if (r.status !== 0) { console.error(r.stderr.slice(-800)); process.exit(1); }
console.log(`${out}: bed + ${events.length} cues, input ${js.input_i} LUFS -> ${LUFS} LUFS`);
