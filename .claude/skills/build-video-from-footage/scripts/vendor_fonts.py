#!/usr/bin/env python3
"""Self-host Google Fonts locally so a Hyperframes project renders offline and lints clean.

Hyperframes will auto-fetch Google Fonts at render time, but that leaves `google_fonts_import`
and `font_family_without_font_face` lint errors plus a network dependency. This downloads every
subset .woff2 for the requested families/weights into <out>/fonts/ and writes <out>/fonts.css with
local @font-face rules (with their unicode-ranges preserved). Inline the contents of fonts.css
into the <style> of index.html AND each sub-composition (captions.html, callouts.html) so the
linter sees the @font-face and the renderer resolves glyphs locally.

Keep ALL returned subsets — the inch-mark `″` (U+2033) and friends live in the `latin` subset's
unicode-range, so trimming to "just latin-1" would drop glyphs your callouts use.

Usage:
    python3 vendor_fonts.py --out assets --families "Inter:500,600,700" "Roboto Mono:500,700"
"""
import argparse
import os
import re
import urllib.request

UA = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0 Safari/537.36"
}


def build_css2_url(families):
    parts = []
    for spec in families:
        name, _, weights = spec.partition(":")
        fam = name.strip().replace(" ", "+")
        ws = weights.replace(" ", "") or "400"
        parts.append("family=%s:wght@%s" % (fam, ";".join(ws.split(","))))
    return "https://fonts.googleapis.com/css2?" + "&".join(parts) + "&display=block"


def main(args):
    os.makedirs(os.path.join(args.out, "fonts"), exist_ok=True)
    url = build_css2_url(args.families)
    css = urllib.request.urlopen(urllib.request.Request(url, headers=UA)).read().decode()
    blocks = re.findall(r"/\*\s*([\w-]+)\s*\*/\s*@font-face\s*{([^}]+)}", css)
    out, n = [], 0
    for subset, body in blocks:
        fam = re.search(r"font-family:\s*'([^']+)'", body).group(1)
        wght = re.search(r"font-weight:\s*(\d+)", body).group(1)
        um = re.search(r"url\((https://[^)]+\.woff2)\)", body)
        ur = re.search(r"unicode-range:\s*([^;]+);", body)
        if not um:
            continue
        fname = "%s-%s-%s.woff2" % (fam.lower().replace(" ", "-"), wght, subset)
        data = urllib.request.urlopen(urllib.request.Request(um.group(1), headers=UA)).read()
        open(os.path.join(args.out, "fonts", fname), "wb").write(data)
        n += 1
        urange = "\n  unicode-range: %s;" % ur.group(1).strip() if ur else ""
        out.append(
            "@font-face {\n  font-family: '%s';\n  font-style: normal;\n  font-weight: %s;\n"
            "  font-display: block;\n  src: url('%s/fonts/%s') format('woff2');%s\n}"
            % (fam, wght, args.out.rstrip("/").split("/")[-1] if args.css_rel else "assets", fname, urange)
        )
    # By default reference fonts as assets/fonts/... (the common project layout). Override with
    # --css-rel to use the literal <out> basename instead.
    css_path = os.path.join(args.out, "fonts.css")
    open(css_path, "w").write("\n".join(out) + "\n")
    print("downloaded %d woff2 files -> %s/fonts/  | wrote %s" % (n, args.out, css_path))
    print("Next: inline the contents of %s into the <style> of index.html + each sub-composition,"
          " and remove any Google Fonts <link>." % css_path)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--out", default="assets", help="project assets dir (fonts go in <out>/fonts/)")
    p.add_argument("--families", nargs="+", required=True, help='e.g. "Inter:500,600,700" "Roboto Mono:500,700"')
    p.add_argument("--css-rel", action="store_true", help="reference fonts via <out> basename instead of 'assets'")
    main(p.parse_args())
