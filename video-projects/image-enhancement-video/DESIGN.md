# DESIGN — Image Enhancement Video (TikTok hype)

Vertical 1080×1920 short showing a before → prompt → after AI image transformation. Energetic, social-native, playful — built to stop the scroll.

## Style Prompt

Punchy social-media energy: chunky sans-serif headlines with thick black outlines, bright sticker-bomb backgrounds, slight Y-axis wiggle on text, bouncy elastic entrances. The hero photo cards have soft shadows and rounded corners like polaroids. The reveal beat is the calm in the middle — black flash, then the enhanced B&W photo lands clean and slow, a deliberate contrast against the surrounding chaos. CTA returns to the hype palette with a wobble.

## Colors

- `#FFEC3D` — primary background (electric yellow). Carries energy / "scroll-stopper".
- `#FF2D87` — hot pink accent. Used for the prompt box border and CTA arrows.
- `#1B1B1F` — near-black. All text, photo card borders, the reveal-scene canvas.
- `#FFFFFF` — pure white. Text on dark, photo card fill.
- `#00E5FF` — electric cyan accent. Sparingly: typewriter caret, highlight pulses.

Discipline: at most 3 of these visible in any single scene. The black canvas reveal scene uses only `#1B1B1F` + `#FFFFFF` to make the B&W enhanced photo feel like the payoff.

## Typography

- **`"Archivo Black"`** (Google Fonts) — headline display. ~150–220px, tight tracking, ALL CAPS. Thick black text-stroke (3–4px `#1B1B1F`) on bright backgrounds gives the sticker-cutout look.
- **`"JetBrains Mono"`** (Google Fonts) — the prompt typewriter. ~36px, white on dark, with a blinking cyan caret.

No third font. The two-font system is what keeps a hype piece from going chaotic.

## Motion Rules

- **Entrances:** `back.out(2)` on text (overshoot), `expo.out` on photo cards, stagger 0.06–0.10s.
- **Holds:** elements get a continuous low-amplitude wiggle/breathe (1–2px y drift, `sine.inOut`, finite repeats) so nothing sits dead-still on screen.
- **Transitions:** elastic-push and circle-iris between scenes; one whip-flash (white) into the reveal moment. Durations 0.2–0.3s. Easing `power4.inOut` / `expo`.
- **Reveal moment:** the B&W enhanced photo enters with a slow `power2.out` over 0.7s — deliberately slower than every other entrance in the piece. Stillness sells the payoff.
- **CTA:** "Comment 'PROMPT'" and "Follow for more" each get a finger-tap stamp (scale 1.0 → 1.15 → 1.0 on `back.out(3)`).

## What NOT to Do

1. **No flat fade-ins.** Every entrance has a directional or scale component.
2. **No black canvas in scenes 1, 2, 4.** The black canvas is reserved for the reveal — its scarcity is what makes it land.
3. **No more than 6 words on screen at once** in the hype scenes. The eye can't track stickers + photo + caption + accents simultaneously.
4. **No thin/light type weights.** Display text is Archivo Black only. Hype + thin = wrong vibe.
5. **No exit animations except the final scene** (per framework rule). Transitions handle handoffs.
