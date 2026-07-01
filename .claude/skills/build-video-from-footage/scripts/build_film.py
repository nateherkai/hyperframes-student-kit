#!/usr/bin/env python3
"""Assemble a multi-clip film from per-clip kept segments, and record the timeline offsets.

Reads build.config.json (see references/config-schema.md). For each clip it trims the kept
`segments` (video+audio together), scales to 1920x1080, concatenates them into a per-clip cut, then
concatenates all clips into <assets>/film.mp4. Writes <assets>/build.state.json with the MEASURED
per-clip cut durations and cumulative film-timeline offsets — measured because real cut durations
drift a few frames from the segment arithmetic, and the captions/callouts must line up to the frame.

Run scripts that follow (build_overlays.py) consume build.state.json.

Usage:
    eval "$(/opt/homebrew/bin/brew shellenv)" && python3 build_film.py build.config.json
"""
import json
import subprocess
import sys
import os


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.stderr.write(r.stderr[-600:] + "\n")
        raise SystemExit("ffmpeg failed: " + " ".join(cmd[:6]) + " ...")


def dur(f):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", f],
        capture_output=True, text=True,
    ).stdout.strip()
    return float(out)


def build_cut(src, segs, w, h, fps, out):
    parts = []
    for i, (s, e) in enumerate(segs):
        parts.append("[0:v]trim=%s:%s,setpts=PTS-STARTPTS,scale=%d:%d:flags=lanczos,fps=%d[v%d]"
                     % (s, e, w, h, fps, i))
        parts.append("[0:a]atrim=%s:%s,asetpts=PTS-STARTPTS[a%d]" % (s, e, i))
    cat = "".join("[v%d][a%d]" % (i, i) for i in range(len(segs))) + \
          "concat=n=%d:v=1:a=1[v][a]" % len(segs)
    run(["ffmpeg", "-y", "-i", src, "-filter_complex", ";".join(parts) + ";" + cat,
         "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-c:a", "aac", "-b:a", "192k", "-r", str(fps), "-movflags", "+faststart", out])


def main(cfg_path):
    cfg = json.load(open(cfg_path))
    A = cfg.get("assets_dir", "assets")
    w, h, fps = cfg.get("width", 1920), cfg.get("height", 1080), cfg.get("fps", 30)
    cut_files, durs = [], []
    for ci, clip in enumerate(cfg["clips"]):
        out = os.path.join(A, "cut%d.mp4" % ci)
        build_cut(clip["src"], clip["segments"], w, h, fps, out)
        d = dur(out)
        cut_files.append(out)
        durs.append(d)
        print("clip %d -> %s  (%.2fs)" % (ci, out, d))
    # concat all cuts
    inputs = []
    for f in cut_files:
        inputs += ["-i", f]
    streams = "".join("[%d:v][%d:a]" % (i, i) for i in range(len(cut_files)))
    run(["ffmpeg", "-y", *inputs, "-filter_complex",
         "%sconcat=n=%d:v=1:a=1[v][a]" % (streams, len(cut_files)),
         "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-c:a", "aac", "-b:a", "192k", "-r", str(fps), "-movflags", "+faststart",
         os.path.join(A, "film.mp4")])
    offsets, acc = [], 0.0
    for d in durs:
        offsets.append(round(acc, 3))
        acc += d
    state = {"film": os.path.join(A, "film.mp4"), "video_dur": round(acc, 3),
             "clip_durs": [round(d, 3) for d in durs], "offsets": offsets}
    json.dump(state, open(os.path.join(A, "build.state.json"), "w"), indent=2)
    print("film.mp4 = %.2fs | offsets %s -> %s" % (acc, offsets, os.path.join(A, "build.state.json")))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "build.config.json")
