# build.config.json schema

One file drives the cut, the caption remap, and the overlay generation. Keep it in the project
root next to `index.html`. All times are in **seconds, in each clip's ORIGINAL timeline** (before
cutting) — the scripts translate them to the assembled film timeline.

```json
{
  "width": 1920,
  "height": 1080,
  "fps": 30,
  "assets_dir": "assets",
  "compositions_dir": "compositions",
  "fonts_css": "assets/fonts.css",

  "clips": [
    {
      "src": "assets/IMG_1648.mov",
      "transcript": "assets/IMG_1648-transcript.json",
      "segments": [[0.0, 56.4], [63.2, 112.2]]
    },
    {
      "src": "assets/IMG_1659.mov",
      "transcript": "assets/IMG_1659-transcript.json",
      "segments": [[0.52, 81.6]]
    }
  ],

  "callouts": [
    {"clip": 0, "at": 31.8, "hold": 4.2, "label": "BOARD LENGTH", "value": "60″", "sub": "Home Depot cut"},
    {"clip": 0, "at": 40.8, "hold": 3.3, "label": "MITER ANGLE",  "value": "45°", "sub": "each end"},
    {"clip": 1, "at": 41.95,"hold": 4.6, "label": "FASTENERS",    "value": "18ga", "sub": "1½″ brad nails + glue"}
  ]
}
```

## Fields

| Field | Meaning |
|---|---|
| `clips[].src` | The clip to cut from. Use the re-encoded 1080p mp4, or the original `.mov` (it must still carry an audio stream — segments trim video+audio together). |
| `clips[].transcript` | The CLEAN transcript of that clip's full original audio (from `npx hyperframes transcribe`). Used for the caption remap. |
| `clips[].segments` | `[[start,end], ...]` of kept ranges, in the clip's original time. Order = play order. Run the clip THROUGH its end clap if you want a clap-synced transition. |
| `callouts[].clip` | Index into `clips`. |
| `callouts[].at` | When the number is spoken, in that clip's original time. The card appears ~0.2s before and counts up. |
| `callouts[].value` | Display value. A leading non-digit prefix, digits, and a trailing suffix are parsed so the digits count up: `"60″"`, `"45°"`, `"18ga"`, `"×5"`. |

## How film-time is computed

`build_film.py` measures each cut's real duration and writes cumulative `offsets` to
`build.state.json`. `build_overlays.py` maps any original time `t` in clip `c` to film-time:

```
local_offset = sum of (seg.end - seg.start) for segments before the one containing t
film_time    = offsets[c] + local_offset + (t - seg.start)
```

Section card fire-times in `index.html` use the same `offsets` (a section card fires at
`offsets[c]` for the clip's start, or at a clap's remapped film-time). Glyphs commonly used in
`value`/`sub`: `″` (inch ″), `°` (°), `½` (½), `×` (×), `·` (·).
