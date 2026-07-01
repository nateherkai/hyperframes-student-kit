#!/usr/bin/env python3
"""Find candidate hand-clap transients near the end of a clip (used as cut/transition cues).

A clap is a short, broadband impulse — its signature is a huge ATTACK RATIO (energy vs the
quarter-second before it), not just loudness (a saw or board-drop is loud too). This scans the
clip tail at 10ms resolution and reports the sharpest-attack impulses.

IMPORTANT: audio alone can't distinguish a clap from a tool. ALWAYS confirm visually — extract a
frame at each candidate time and Read it to see hands coming together:
    ffmpeg -ss <t> -i clip.mov -frames:v 1 frame.png

Input must be a mono WAV (decode first):
    ffmpeg -y -i clip.m4a -ac 1 -ar 8000 -f wav clip-8k.wav

Usage:
    python3 detect_claps.py clip-8k.wav <clip_duration_seconds> [--tail 12]
"""
import argparse
import array
import wave


def main(args):
    w = wave.open(args.wav, "rb")
    sr = w.getframerate()
    raw = w.readframes(w.getnframes())
    w.close()
    a = array.array("h")
    a.frombytes(raw)
    start = max(0, int((args.dur - args.tail) * sr))
    win = int(sr * 0.01)  # 10ms windows
    E, idx = [], []
    for i in range(start, len(a) - win, win):
        s = 0
        for j in range(i, i + win):
            s += a[j] * a[j]
        E.append(s)
        idx.append(i / sr)
    pre = int(0.25 / 0.01)  # baseline window = 250ms before
    cand = []
    for k in range(pre, len(E) - 1):
        base = sum(E[k - pre:k]) / pre or 1
        if E[k] > base * args.min_attack and E[k] >= E[k - 1] and E[k] >= E[k + 1]:
            cand.append((idx[k], E[k] / base, E[k]))
    cand.sort(key=lambda x: -x[2])  # by absolute energy
    seen, rows = [], []
    for t, ratio, e in cand:
        if any(abs(t - s) < 0.3 for s in seen):
            continue
        seen.append(t)
        rows.append((t, ratio, e))
        if len(rows) >= args.top:
            break
    rows.sort()
    print("# clap candidates in tail of %s (clip %.1fs)" % (args.wav, args.dur))
    print("# the highest attack-ratio near the very end is usually the clap — CONFIRM VISUALLY")
    for t, ratio, e in rows:
        print("  t=%6.2fs   attack x%-5.0f   energy=%.2e" % (t, ratio, e))


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("wav", help="mono WAV (decode with ffmpeg -ac 1 -ar 8000 -f wav)")
    p.add_argument("dur", type=float, help="clip duration in seconds")
    p.add_argument("--tail", type=float, default=12.0, help="seconds of tail to scan")
    p.add_argument("--min-attack", type=float, default=6.0, dest="min_attack")
    p.add_argument("--top", type=int, default=4)
    main(p.parse_args())
