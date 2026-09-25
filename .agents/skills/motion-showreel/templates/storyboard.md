# Storyboard: <Brand> Showreel <length>s

Grid: <period>s beats (<bpm> BPM measured), <fps>fps. `B(n) = n * <period>`. Frame sheet: `qa/beatsheet.txt` (from `scripts/beatgrid.mjs`).
Motif: <the brand's most reduced element>. Held-back climax color: <color, flurry only>.

| Beats | Time | HUD label | Value | Frame | Tool overlay | In-transform | Out-transform | SFX |
|---|---|---|---|---|---|---|---|---|
| 0-4 | | 01 · <physics> | ink | the motif enters and obeys physics | live readout | (opening) | motif becomes <laser / line / flash> | pops on contacts |
| 4-12 | | 02 · <type> | paper, invert at B10 | brand phrase as kinetic type, 3 type voices, wallpaper | brand-native input (search bar, chat box) or selection box | flash becomes paper | letters become motif copies | typing, click, invert hit |
| 12-16 | | 03 · <grid> | ink | motif copies become a grid of real brand imagery, wave, camera tilt | grid readout | dots become tiles | push into one tile; pre-drop gap | swishes, whoosh |
| 16-20 | | 04 · <particles> | ink + accent glow | the drop: burst into particles that form a verified stat | particle readout | tile becomes a burst | particles become the hero silhouette | boom, pop, ticks |
| 20-24 | | 05 · <lookdev> | ink | photoreal hero object, two materials | material readout, counter | silhouette becomes the object | push through the lens, hard cut | shimmer, whoosh |
| 24-28 | | 06 · <flurry> | alternating, held-back color arrives | 5-6 signature UI moments, 1 beat then half beats | each moment's own UI | hard cuts | noise | clicks, glitch, tape stop |
| 28-end | | 07 · <end> | ink | logo resolves, rule draws, subtitles type, the motif lands as the logo's own element, tagline last | typing cursor | noise resolves | hold | final hit, pop |

Checks before building:
- [ ] Freeze any frame: it reads as the brand without the HUD.
- [ ] Every transition transforms the object (except flurry cuts).
- [ ] Value flips at every chapter change.
- [ ] Every fact on screen is verified and dated in BRAND.md.
