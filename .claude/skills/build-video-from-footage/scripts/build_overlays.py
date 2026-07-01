#!/usr/bin/env python3
"""Generate captions.html (word-pop) and callouts.html (count-up) for an assembled film.

THE KEY TRICK: captions come from remapping each clip's CLEAN ORIGINAL transcript onto the film
timeline using the kept segments + measured offsets from build.state.json — never from
re-transcribing the cut (that hallucinates words). Each original word that falls inside a kept
segment gets a new film-time = offset[clip] + (local cut offset) + (word_time - seg_start).

Words are grouped into caption lines (break on segment seam, sentence end, >0.9s gap, or >=5 words),
then rendered with a per-word spring "pop". Callouts are positioned by their original spoken time
(config `at`), remapped the same way, and their numeric value counts up from 0.

Both files inline the local @font-face from <fonts_css> so they render offline and lint clean.
Animations use only property tweens / tl.set (which apply on frame-seek) — see
references/render-safe-effects.md for why tl.call must NOT be used.

Usage:
    python3 build_overlays.py build.config.json
"""
import json
import re
import sys
import os

NUM = re.compile(r"^\d+[.,]?$|^(inches|inch|feet|foot|degrees|gauge)[.,]?$", re.I)


def remap(orig, segs, base):
    off, acc = [], 0.0
    for s, e in segs:
        off.append(acc)
        acc += (e - s)
    for (s, e), o in zip(segs, off):
        if s <= orig < e:
            return base + o + (orig - s)
    return None


def main(cfg_path):
    cfg = json.load(open(cfg_path))
    A = cfg.get("assets_dir", "assets")
    C = cfg.get("compositions_dir", "compositions")
    state = json.load(open(os.path.join(A, "build.state.json")))
    DUR = state["video_dur"]
    offsets = state["offsets"]
    fonts = open(cfg.get("fonts_css", os.path.join(A, "fonts.css"))).read().strip()
    fontblock = "\n      /* self-hosted fonts */\n" + "\n".join("      " + l for l in fonts.splitlines()) + "\n"

    # ---- remap words across all clips, tagging a global segment id for clean group breaks ----
    words, sid = [], 0
    for ci, clip in enumerate(cfg["clips"]):
        d = json.load(open(clip["transcript"]))
        segs, base = clip["segments"], offsets[ci]
        off, acc = [], 0.0
        for s, e in segs:
            off.append(acc)
            acc += (e - s)
        for w in d:
            for k, ((s, e), o) in enumerate(zip(segs, off)):
                if s <= w["start"] < e:
                    t = base + o + (w["start"] - s)
                    en = base + o + (min(w["end"], w["start"] + 2.0) - s)
                    words.append({"t": t, "e": en, "w": w["text"].strip(), "seg": sid + k})
                    break
        sid += len(segs)
    words.sort(key=lambda x: x["t"])

    groups, cur = [], []
    for i, x in enumerate(words):
        if cur and x["seg"] != cur[-1]["seg"]:
            groups.append(cur); cur = []
        cur.append(x)
        es = x["w"].endswith((".", "?", "!"))
        gap = (words[i + 1]["t"] - x["e"]) if i + 1 < len(words) and words[i + 1]["seg"] == x["seg"] else 9
        if len(cur) >= 5 or (len(cur) >= 3 and es) or (len(cur) >= 3 and gap > 0.9):
            groups.append(cur); cur = []
    if cur:
        groups.append(cur)
    merged = []
    for g in groups:
        if len(g) < 2 and merged and merged[-1][-1]["seg"] == g[0]["seg"]:
            merged[-1] += g
        else:
            merged.append(g)
    groups = merged
    G = []
    for i, g in enumerate(groups):
        gs, ge = g[0]["t"], g[-1]["e"]
        nx = groups[i + 1][0]["t"] if i + 1 < len(groups) else DUR
        end = min(ge + 0.25, nx - 0.03, DUR)
        if end < gs + 0.45:
            end = min(gs + 0.45, nx - 0.03, DUR)
        G.append({"t": round(gs, 2), "end": round(end, 2),
                  "words": [{"w": w["w"], "c": "num" if NUM.match(w["w"]) else ""} for w in g]})
    gj = json.dumps(G, separators=(",", ":"), ensure_ascii=False)

    cap = CAPTIONS.replace("__FONT__", fontblock).replace("__GROUPS__", gj).replace("__DUR__", str(DUR))
    open(os.path.join(C, "captions.html"), "w").write(cap)

    # ---- callouts: remap each by its spoken time, parse numeric value for count-up ----
    CO = []
    for c in cfg.get("callouts", []):
        clip = cfg["clips"][c["clip"]]
        t = remap(c["at"], clip["segments"], offsets[c["clip"]])
        if t is None:
            sys.stderr.write("WARN callout at %.2f not inside a kept segment of clip %d\n" % (c["at"], c["clip"]))
            continue
        CO.append({"t": round(t - 0.2, 2), "end": round(t - 0.2 + c.get("hold", 4.2), 2),
                   "label": c["label"], "value": c["value"], "sub": c.get("sub", "")})
    cj = json.dumps(CO, separators=(",", ":"), ensure_ascii=False)
    cout = CALLOUTS.replace("__FONT__", fontblock).replace("__CO__", cj).replace("__DUR__", str(DUR))
    open(os.path.join(C, "callouts.html"), "w").write(cout)
    print("captions.html: %d groups (word-pop) | callouts.html: %d (count-up)" % (len(G), len(CO)))


CAPTIONS = r'''<template id="captions-template">
  <div data-composition-id="captions" data-width="1920" data-height="1080">
    <style>__FONT__
      [data-composition-id="captions"]{position:absolute;inset:0;font-family:"Inter",sans-serif;}
      [data-composition-id="captions"] .cap-scrim{position:absolute;left:0;right:0;bottom:0;height:300px;pointer-events:none;
        background:linear-gradient(to top,rgba(14,17,22,0.92) 0%,rgba(14,17,22,0.6) 45%,rgba(14,17,22,0) 100%);}
      [data-composition-id="captions"] .cap-wrap{position:absolute;left:0;right:0;bottom:84px;text-align:center;}
      [data-composition-id="captions"] .cap-group{position:absolute;left:0;right:0;bottom:0;padding:0 200px;
        font-size:54px;font-weight:600;line-height:1.18;letter-spacing:-0.01em;color:#f4efe6;text-shadow:0 2px 14px rgba(0,0,0,0.55);}
      [data-composition-id="captions"] .cap-word{display:inline-block;will-change:transform,opacity;}
      [data-composition-id="captions"] .cap-word.num{color:#e8913c;font-weight:700;font-variant-numeric:tabular-nums;}
    </style>
    <div class="cap-scrim"></div>
    <div class="cap-wrap" id="cap-wrap"></div>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <script>
      (function(){
        var GROUPS=__GROUPS__;var wrap=document.getElementById("cap-wrap");var tl=gsap.timeline({paused:true});
        GROUPS.forEach(function(g,gi){
          var el=document.createElement("div");el.className="cap-group";el.id="cg-"+gi;var spans=[];
          g.words.forEach(function(wd,wi){var s=document.createElement("span");s.className="cap-word"+(wd.c?" "+wd.c:"");
            s.textContent=wd.w+(wi<g.words.length-1?" ":"");el.appendChild(s);spans.push(s);});
          wrap.appendChild(el);
          tl.set(el,{opacity:1},0);
          tl.set(spans,{opacity:0,y:16,scale:0.82},0);
          tl.to(spans,{opacity:1,y:0,scale:1,duration:0.3,ease:"back.out(1.8)",stagger:0.04},g.t);
          tl.to(el,{opacity:0,y:-10,duration:0.14,ease:"power2.in"},Math.max(g.t+0.35,g.end-0.14));
          tl.set(el,{opacity:0,visibility:"hidden"},g.end);
        });
        tl.set({},{},__DUR__);
        window.__timelines=window.__timelines||{};window.__timelines["captions"]=tl;
      })();
    </script>
  </div>
</template>
'''

CALLOUTS = r'''<template id="callouts-template">
  <div data-composition-id="callouts" data-width="1920" data-height="1080">
    <style>__FONT__
      [data-composition-id="callouts"]{position:absolute;inset:0;font-family:"Roboto Mono",monospace;}
      [data-composition-id="callouts"] .co-card{position:absolute;top:96px;left:104px;min-width:300px;
        padding:26px 36px 30px;background:rgba(14,17,22,0.82);border-left:4px solid #5cc6d6;border-radius:6px;
        box-shadow:0 18px 50px rgba(0,0,0,0.45);will-change:transform,opacity;}
      [data-composition-id="callouts"] .co-label{font-size:23px;font-weight:500;letter-spacing:0.26em;color:#5cc6d6;text-transform:uppercase;margin-bottom:6px;}
      [data-composition-id="callouts"] .co-value{font-size:104px;font-weight:700;line-height:1;color:#e8913c;font-variant-numeric:tabular-nums;letter-spacing:-0.02em;}
      [data-composition-id="callouts"] .co-rule{height:3px;background:#5cc6d6;margin:16px 0 12px;transform-origin:left center;}
      [data-composition-id="callouts"] .co-sub{font-size:24px;font-weight:500;letter-spacing:0.04em;color:#9aa3ad;}
    </style>
    <div id="co-wrap"></div>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <script>
      (function(){
        var CO=__CO__;var wrap=document.getElementById("co-wrap");var tl=gsap.timeline({paused:true});
        CO.forEach(function(c,ci){
          var card=document.createElement("div");card.className="co-card";card.id="co-"+ci;
          card.innerHTML='<div class="co-label"></div><div class="co-value"></div><div class="co-rule"></div><div class="co-sub"></div>';
          card.querySelector(".co-label").textContent=c.label;
          var valEl=card.querySelector(".co-value");card.querySelector(".co-sub").textContent=c.sub;
          wrap.appendChild(card);var rule=card.querySelector(".co-rule");
          var mm=c.value.match(/^(\D*)(\d+)(.*)$/);var pre=mm?mm[1]:"",num=mm?parseInt(mm[2]):0,suf=mm?mm[3]:"";
          valEl.textContent=mm?(pre+"0"+suf):c.value;
          var prox={v:0};
          tl.set(card,{opacity:0,x:-44,scale:0.94},0);tl.set(rule,{scaleX:0},0);
          tl.to(card,{opacity:1,x:0,scale:1,duration:0.4,ease:"power3.out"},c.t);
          if(mm){tl.to(prox,{v:num,duration:0.6,ease:"power2.out",onUpdate:function(){valEl.textContent=pre+Math.round(prox.v)+suf;}},c.t+0.12);}
          tl.to(rule,{scaleX:1,duration:0.5,ease:"power2.out"},c.t+0.18);
          tl.to(card,{opacity:0,x:-24,duration:0.3,ease:"power2.in"},c.end-0.3);
          tl.set(card,{opacity:0,visibility:"hidden"},c.end);
        });
        tl.set({},{},__DUR__);
        window.__timelines=window.__timelines||{};window.__timelines["callouts"]=tl;
      })();
    </script>
  </div>
</template>
'''

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "build.config.json")
