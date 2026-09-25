#!/usr/bin/env node
// Generate an SFX kit with ElevenLabs sound generation. PAID calls: confirm with the user first.
//
// Usage: node sfx.mjs kit.json assets/audio/sfx
//   kit.json: { "dot_pop": ["tiny rubbery bouncy ball pop, clean digital", 0.5], ... }
//   Durations must be 0.5-30 seconds. Existing files are skipped, so reruns are free.
// A good showreel kit: dot_pop, click, whoosh, whoosh_big, laser, sub_boom, glitch, ticks,
// shimmer, tape_stop, final_hit, plus brand-native sounds (typing, a notification bell, a like pop).
// Reads ELEVENLABS_API_KEY from the environment or the workspace .env.
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

function loadKey() {
  if (process.env.ELEVENLABS_API_KEY) return process.env.ELEVENLABS_API_KEY;
  let dir = dirname(fileURLToPath(import.meta.url));
  for (let i = 0; i < 8; i++, dir = dirname(dir)) {
    const f = join(dir, '.env');
    if (existsSync(f)) { const m = readFileSync(f, 'utf8').match(/^\s*ELEVENLABS_API_KEY\s*=\s*"?([^"\r\n]+)"?/m); if (m) return m[1].trim(); }
  }
  throw new Error('ELEVENLABS_API_KEY is not set. Add it to .env (see docs/TOOLS-AND-API-KEYS.md).');
}
const [kitFile, outDir] = process.argv.slice(2);
if (!kitFile || !outDir) { console.error('Usage: node sfx.mjs kit.json <out-dir>'); process.exit(1); }
const kit = JSON.parse(readFileSync(kitFile, 'utf8'));
const key = loadKey();
mkdirSync(outDir, { recursive: true });
await Promise.all(Object.entries(kit).map(async ([name, [text, seconds]]) => {
  const out = join(outDir, `${name}.mp3`);
  if (existsSync(out)) return console.log(name, 'exists');
  const r = await fetch('https://api.elevenlabs.io/v1/sound-generation', {
    method: 'POST', headers: { 'xi-api-key': key, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, duration_seconds: Math.max(0.5, seconds), prompt_influence: 0.6 }),
  });
  if (!r.ok) { console.log(name, 'ERROR', r.status, (await r.text()).slice(0, 200)); process.exitCode = 1; return; }
  writeFileSync(out, Buffer.from(await r.arrayBuffer()));
  console.log(name, 'saved');
}));
