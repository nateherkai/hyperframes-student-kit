#!/usr/bin/env python3
"""Generate a balanced cinematic 3D LUT (.cube) for grading workshop/talking-head footage.

The default grade neutralizes a warm/orange cast, adds a gentle S-curve, lifts shadows a touch,
rolls off highlights (tames blown windows/doorways), slightly desaturates, and applies a subtle
teal-orange split tone. All knobs are CLI flags so you can dial the look per project.

Apply with ffmpeg:
    ffmpeg -i film.mp4 -vf "lut3d=grade.cube" -c:v libx264 -crf 18 -c:a copy film-graded.mp4

Color is subjective — always show the user a before/after frame and adjust.

Usage:
    python3 make_lut.py --out assets/grade.cube
    python3 make_lut.py --out g.cube --wb-r 0.97 --wb-b 1.03 --contrast 1.10 --desat 0.95
"""
import argparse


def build(args):
    N = args.size

    def clamp(x):
        return 0.0 if x < 0 else (1.0 if x > 1 else x)

    def roll(x):  # highlight roll-off above the knee
        k = args.knee
        return x if x < k else k + (x - k) * args.knee_slope

    def grade(r, g, b):
        # 1) white balance — cool a warm cast (wb_r<1 pulls red, wb_b>1 lifts blue)
        r *= args.wb_r
        b *= args.wb_b
        # 2) S-curve contrast around mid grey
        c = args.contrast
        r = (r - 0.5) * c + 0.5
        g = (g - 0.5) * c + 0.5
        b = (b - 0.5) * c + 0.5
        # 3) lift shadows (non-crushed blacks)
        lf = args.lift
        r = r + lf * (1 - r)
        g = g + lf * (1 - g)
        b = b + lf * (1 - b)
        # 4) highlight roll-off
        r, g, b = roll(r), roll(g), roll(b)
        # 5) global desaturation
        lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
        s = args.desat
        r = lum + (r - lum) * s
        g = lum + (g - lum) * s
        b = lum + (b - lum) * s
        # 6) teal-orange split: shadows -> teal, highlights -> warm
        t = lum - 0.5
        sp = args.split
        if t < 0:
            b += (-t) * sp
            g += (-t) * sp * 0.4
        else:
            r += t * sp * 0.85
            g += t * sp * 0.2
        return clamp(r), clamp(g), clamp(b)

    with open(args.out, "w") as f:
        f.write('TITLE "%s"\nLUT_3D_SIZE %d\n' % (args.title, N))
        for bi in range(N):
            for gi in range(N):
                for ri in range(N):
                    r, g, b = grade(ri / (N - 1), gi / (N - 1), bi / (N - 1))
                    f.write("%.6f %.6f %.6f\n" % (r, g, b))
    print("wrote %s (%d^3)" % (args.out, N))


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--out", default="grade.cube")
    p.add_argument("--title", default="balanced cinematic")
    p.add_argument("--size", type=int, default=33, help="LUT cube resolution (33 is standard)")
    p.add_argument("--wb-r", type=float, default=0.955, dest="wb_r", help="red gain (<1 cools)")
    p.add_argument("--wb-b", type=float, default=1.05, dest="wb_b", help="blue gain (>1 cools)")
    p.add_argument("--contrast", type=float, default=1.12)
    p.add_argument("--lift", type=float, default=0.018, help="shadow lift (0..0.05)")
    p.add_argument("--knee", type=float, default=0.78, help="highlight roll-off knee")
    p.add_argument("--knee-slope", type=float, default=0.72, dest="knee_slope")
    p.add_argument("--desat", type=float, default=0.92, help="saturation (1.0 = unchanged)")
    p.add_argument("--split", type=float, default=0.03, help="teal-orange strength (0 to disable)")
    build(p.parse_args())
