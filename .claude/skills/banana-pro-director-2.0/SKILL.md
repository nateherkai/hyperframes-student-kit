---
name: banana-pro-director-2.0
description: "Higgsfield image prompt director for Banana Pro, Soul Cinema, and GPT-2. Modes: (0) face lock for new characters — Banana Pro single-pass (default), GPT-2 single-pass (higher fidelity, higher credits), or Soul Cinema two-pass, all on mid-gray seamless (locked default; white on request) with black camisole/tank baseline, (1) single-image character outfit — Banana Pro or Soul Cinema two-step, (2) 6-panel character sheet, (3) cinematic scene plates with or without characters, (4) GPT-2 detail face/chest-up, (5) outfit replacement — swap a face onto an outfit using two refs. Reads references for hair, makeup, wardrobe, jewelry, identity. Outputs photorealistic prompts with one clean cinema stack — pores, subsurface scattering, strand hair, fabric weave, atmospheric perspective, anamorphic character, theatrical grain. Use for new character builds, character/outfit refs, character sheets, scene plates, environment plates, detail shots, outfit replacement, or any photorealistic still."
---

# Banana Pro Director 2.0 — Image Asset Builder

The locked image prompt grammar for great Higgsfield image assets. Six modes, in strict order:

0. **Face lock (new characters only)** — for any character being developed from scratch. Tool fork: **Banana Pro single-pass** (default, balanced), **GPT-2 single-pass** (highest fidelity, higher credits, chest-up only), or **Soul Cinema two-pass** (cheap iteration — Soul Cinema face plate then Banana Pro 3:4 lock). All paths use mid-gray seamless (the locked default backdrop — white only on explicit request), soft soft lighting from camera-left or camera-right, and a locked baseline wardrobe (plain black camisole for women, plain black ribbed tank for men). No outfit styling, no environment, no in-depth prompting at this stage. Identity only.
1. **Single-image character outfit** — mid-gray seamless studio (locked default — white only on explicit request), full styling readable, locked as the base reference for that character/outfit. Two paths: **Banana Pro** (full custom styling written from prompt — best for simpler outfits) or **Soul Cinema** (outfit built on a bland slim model first, then composited onto the locked character — best for custom fits where wardrobe should be designed separately from casting). User picks based on outfit complexity.
2. **6-panel character sheet** — built ONLY after a single-image base exists, composed as one 16:9 frame with a 3×2 grid: front body, back body, two side-profile close headshots, one front face close headshot, one detail shot (nails / jewelry / piercing / held prop).
3. **Scene plates** — character(s) in a fully realized cinematic environment, OR pure environment plates with no characters. Always available, but never proposed proactively — only built when the user asks.

Plus two optional capabilities:

4. **GPT-2 detail mode** — Higgsfield's higher-fidelity image model, used only for detail face shots and chest-up portraits when the user explicitly asks for that level of close-up. Never suggested otherwise.
5. **Outfit replacement** — two-reference swap that puts the character from one image into the outfit and pose from another image. Single locked prompt, character/IP-agnostic. Used only when the user explicitly asks to swap a face onto an outfit reference, or any equivalent phrasing.

Photoreal is the universal default. Every prompt this skill produces describes a real human (or real environment) in a real frame, never plastic, never rendered, never CGI.

---

## THE WORKFLOW — STRICT ORDER

The skill enforces this order. Don't skip steps. Don't combine steps.

### Step 0 — Is the character already built?

Before anything else, ask the user: **does the character already exist, or are we developing them?**

**If the character exists:** ask the user to drop the reference image(s). Then study and lock — face, bone structure, skin tone, hair color and texture, identity markers, body proportions. Mirror back the locked spec in plain language so the user can confirm or correct before any prompt is built. Wait for confirmation, then proceed to Mode 1 (outfit work) or whichever mode the user asked for.

**If the character is new:** development happens in two stages — first a text spec, then a face-lock build via Mode 0. Do NOT jump straight to outfit prompts. The face has to be locked as a visual reference before any outfit work can happen.

Stage 1 — text spec: let the user describe the character in their own words. Listen. Then mirror back a locked spec in plain language covering:

- Approximate apparent age register (described by build, not number)
- Face: bone structure, eye shape and color, brow shape, nose, lip shape, skin tone and finish
- Hair: color (every nuance), length, texture, style
- Body: build, proportions, posture, distinguishing markers
- Default makeup register (if any)
- Default expression and energy
- Any key identity markers — piercings, scars, beauty marks, tattoos, signature jewelry

Wait for confirmation or correction. Iterate on the text spec freely until the user says it's locked. Then move to Stage 2.

Stage 2 — Mode 0 face lock build (see Mode 0 section below). Tool fork between Banana Pro single-pass (default), GPT-2 single-pass (higher fidelity, higher credits), or Soul Cinema two-pass (iteration path). Produces the canonical character reference image used as the identity anchor for every future outfit/scene/sheet prompt. Always run this before any outfit work for a new character. No exceptions.

### Mode 0 — Face lock (new characters only)

See the Mode 0 section below. Tool fork: Banana Pro single-pass (default), GPT-2 single-pass (highest fidelity, higher credits, chest-up only), or Soul Cinema two-pass (cheap iteration — Soul Cinema face plate then Banana Pro 3:4 lock). All paths use mid-gray seamless (the locked default backdrop — white only on explicit request), soft soft lighting, and a locked baseline wardrobe (plain black camisole for women, plain black ribbed tank for men). Produces the canonical reference image. Run once per new character.

### Mode 1 — Single-image character outfit (the base outfit reference)

Once the character is locked (either confirmed from existing reference upload, or built via Mode 0), the FIRST image generated for any new outfit is a single-image character outfit on a mid-gray seamless studio backdrop (the locked default — white only on explicit request). No 6-panel sheet ever gets built before a base outfit reference exists.

Ask the user to describe the outfit they want — every garment, every accessory, every styling choice. If they upload a wardrobe reference image, study it visual-only. Mirror back the wardrobe spec for confirmation.

**Then — before writing the prompt — ask which tool to build the base in:**

> Want to build this in Banana Pro (Nano Banana) or Soul Cinema?
> — **Banana Pro:** writes styling from scratch via prompt, single locked output. Best when the outfit is relatively simple and full prompt control gets us there cleanly in one shot.
> — **Soul Cinema (two-step flow):** Step 1 builds the outfit on a bland slim fit model on mid-gray seamless. Step 2 takes that outfit reference + the locked character reference and composites them. Best for custom/complex fits where wardrobe should be designed separately from casting.

Wait for the user to pick. Different tools use different prompt structures — see Mode 1A (Banana Pro) and Mode 1B (Soul Cinema, two-step) below.

Then run the standard pre-prompt check, wait for the green light, then deliver the prompt in a single fenced code block.

### Mode 2 — 6-panel character sheet

Only after a single-image base reference has been generated (and the user is happy with it) can a 6-panel sheet be built. The 6-panel uses the locked base outfit and shows the same character from six angles in a single 16:9 frame, 3×2 grid: front body, back body, two side-profile close headshots, one front face close headshot, one detail shot (nails / jewelry / piercing / held prop).

Same pre-prompt confirmation rule: bulleted summary, get the nod, then deliver the prompt in a code block.

### Mode 3 — Scene plates (with or without characters)

Always available. Never proposed proactively. Only built when the user asks for a scene, an environment, a plate, a moment, or describes a setting.

Same pre-prompt confirmation rule applies.

### Mode 4 — GPT-2 detail mode (optional, gated)

Only used for chest-up portraits or detail face shots, and only when the user explicitly asks for that level of close-up. Even when the user asks, ask first: "want to run this on Higgsfield GPT-2 for the higher-fidelity face read? heads-up, GPT-2 uses more Higgsfield credits than Banana Pro." Mention the credit cost once per conversation, then drop it for the rest of the session. Wait for confirmation, then deliver the prompt.

GPT-2 prompt structure differs slightly — see the GPT-2 section below.

---

## THE PRE-PROMPT CONFIRMATION RULE (UNIVERSAL)

Every prompt — single image, 6-panel, scene plate, GPT-2 — gets a short "here's what I'm about to prompt, sound good?" check before the full prompt is written. This is not optional. Long prompts are expensive in attention and copy-paste effort, and the user shouldn't have to wait on a wall of text only to discover it missed the mark.

**Exception — minor iteration on a just-delivered prompt.** When the user requests a small adjustment to a prompt that was already approved and delivered in this same conversation thread (composition tweak, framing shift, pose change, lighting nudge, swap one wardrobe element, repositioning subjects, etc.), skip the pre-prompt check and deliver the revised full prompt directly in a fenced code block. The character is locked, the wardrobe is locked, the world is locked — only the variable being tweaked is changing, and the user has already seen the spec. Re-confirming on tiny deltas creates friction.

What still triggers a full pre-prompt check even mid-thread:
- New character entering the frame
- New wardrobe (not a tweak — a full outfit swap)
- New mode (going from single-image to 6-panel, or from base to scene plate)
- New environment / scene type
- The user explicitly asking for a check ("walk me through it first")

Default to delivering when in doubt on a clear minor delta. Default to checking when the change touches anything load-bearing.

**Format: clean bullet points only.** No quote blocks, no em-dash prose lines, no narrative wrapper. One short opening line ("Pre-prompt check:" or similar), then bullets. **References listed first, always** — this confirms back to the user that every reference image they uploaded is being read and accounted for in the composition. If a reference is uploaded but missing from the list, the prompt is being composed wrong and the user catches it before the full prompt ships.

The pre-prompt check is short, plain-language, and lists in this order:
- **References attached** (one bullet, always first — list every uploaded reference image by short visual descriptor)
- **Character** (one bullet — hair, skin, identity markers, expression)
- **Outfit / styling** (one bullet — wardrobe head-to-toe, jewelry, body markers)
- **Backdrop or environment** (one bullet)
- **Framing** (one bullet, only if non-default)

Close with a single short question line ("Sound good?" / "Lock it?" / "Run it?").

Format example:

Pre-prompt check:
- **References attached:** locked character reference sheet, outfit wardrobe reference plate
- **Character:** platinum-blonde ponytail, warm fair skin, sharp almond eyes, neutral expression
- **Outfit:** ivory zip-V corset, ivory parachute pants, cream platforms, clear acrylic accessories
- **Backdrop:** mid-gray seamless studio (locked default)
- **Framing:** full body

Sound good?

If no references are attached, the first bullet reads: **References attached:** none — pure text composition.

Wait for the green light. Then drop the full prompt in a single fenced code block.

---

## CORE PHILOSOPHY

No plastic. No CGI sheen. No 3D-render look. No commercial gloss. No AI-generic skin or hair.

Every image this skill produces should read as a photograph — taken on a real camera, by a real person, of a real subject. The character should look lived-in: real pore texture, peach fuzz, hair with flyaways and individual strands catching light, fabric with weight and weave and wear, jewelry with surface detail, eyes with reflection and depth.

**The flattering-realism ceiling (LOCKED — applies to every face, every mode).** Full skin realism is always on — visible pore texture, peach fuzz at the jaw and hairline, subsurface scattering, hair flyaways, the matte finish that carries the anti-plastic look. But realism never means *unflattering*. Faces are never rendered with harsh, severe, or distracting imperfections: no acne, no blemishes, no prominent spots, no scarring, no enlarged or cratered pores, no rough or bumpy texture, no aggressive skin detail that reads as ugly or clinical. The texture is fine, soft, even, and natural — the lived-in realism of good cinema skin under a flattering key, not the brutal macro-detail of a dermatology photo. Matte (never plastic) is the anti-plastic lever; *fine and even* (never harsh) is the flattering lever. Both are always on together. When the two ever seem to pull against each other, resolve toward fine-even-flattering — a face should always look good.

Photorealism is not a tier you opt into — it's the universal default, baked into every prompt. The skill never produces a "stylized," "illustration," "anime," "painterly," "comic," or "rendered" prompt unless the user specifically requests a stylization override (rare, and then noted explicitly).

---

## UNIVERSAL RENDER RULES — FIGHTING THE AI AESTHETIC

These rules are baked into every Banana Pro, Soul Cinema, and GPT-2 prompt this skill produces. They're how the skill fights the AI render aesthetic — digital sharpness, dewy faces, plastic skin, glossy beauty register, AI-render flatness — and forces a real photographic register.

**1. Real human skin.**
- Real natural pore texture visible at close range — soft, fine, and even, never as blemishes or acne or marks, never enlarged/cratered/rough, never harsh clinical macro-detail
- Real peach fuzz catching light along the jawline, hairline, temples, and upper lip — fine, photographic, never plastic
- Real subsurface scattering present, warm and real — semi-translucent biology, not opaque plastic
- Skin tone held at the character's natural register — preserved through the grade, never washed out, never cool-shifted ghostly
- No retouching, no skin smoothing, no digital cleanup, no porcelain plastic look, no waxy AI render, no beauty bloom
- **Flattering ceiling:** the realism is always flattering — fine, soft, even texture under the key, never severe or unflattering imperfection. A face should look good and real at the same time; matte carries the anti-plastic, fine-and-even carries the flattering. Resolve any tension toward flattering.
- Doll-coded characters (when explicitly requested): smooth matte register without visible pores or peach fuzz but still real and natural, never plastic, never AI-render, never waxen

**2. Real hair physics — strand-by-strand, context-aware.**
- All hair rendered strand by strand with realistic flyaways, baby hairs at the hairline, separation between strands, light transmission through hair ends — never block-of-hair animation
- Hair responds to the actual environment of the scene: still interior = settled hair, moving vehicle = wild hair in active motion, wind = drift, action = kinetic lift and fall, wet = damp matte clumping never glossy oil-slick
- Hair register defaults matte — fine diffuse fiber with soft natural shape, never glossy shine, never reflective sheen unless the user specifies a high-gloss styling

**3. Real lens character.**
- Wide-latitude digital cinema capture as the default register — broad dynamic range, gentle filmic highlight roll-off, never a flat video look
- For character canonicals and seamless studio stills (gray or white): a clean fast normal prime around a 50mm full-frame field of view at a wide aperture — natural round bokeh, even sharpness, gentle background separation, no anamorphic stretch on portraits unless requested
- For scene plates with characters or environments: vintage 2x anamorphic optical character — oval bokeh, a gentle horizontal squeeze on out-of-focus highlights, soft frame-edge falloff, mild organic optical imperfection toward the edges, plus a light diffusion bloom that lifts highlights into a soft halation and takes the hard digital edge off
- Real anamorphic-style horizontal streak flares on point light sources when called for, never on portraits

**4. Real light physics.**
- **Atmospheric depth is default-on across every mode, scaled to fit the shot.** Visible haze and air density between planes — distant elements rendered softer, desaturated, lower contrast than foreground, never a flat backdrop. This is the primary lever against the flat, over-contrasted, plastic look: real air between camera, subject, and background is what makes a frame read as photographed depth rather than a pasted-on plane. Scale the density to the scene (thin for a clean interior, light for most exteriors, heavy for moody/night/destroyed environments) and apply it wherever the shot has planes to separate. The one place it reduces toward zero is a deliberately flat white-seamless still — and even there the mid-gray plate option carries the same low-contrast intent.
- Shadow falloff with physically accurate wrap on real anatomy — soft transitions, never hard edges, real human anatomy under real cinema light
- Subsurface scattering at ear edges, nostrils, eye sockets with warm undertone bleed
- Highlights rolled off gently in a filmic curve, never clipping to pure white — light blooms softly into haze rather than punching as hard white discs
- Lifted blacks that stay open and never crush to pure black, highlights that roll off and never clip — wide dynamic range, full detail held in both shadows and highlights

**5. Real grain.**
- Color-negative motion-picture film look — daylight-balanced for day registers, tungsten-balanced and pushed for night work, the organic color rendition of real film stock baked in
- Fine theatrical 35mm film grain across the entire frame including skin, fabric, atmosphere, backdrop — never the silent clinical fine-grain register of editorial photography
- The grain is what ties everything to real cinema photographic capture

**These five rules are the lock. Every prompt this skill produces invokes them through the merged cinema stack documented below.**

## NIGHT CINEMA REGISTER (FOR NIGHT SCENES)

When the user asks for a night scene, the night work has a specific theatrical action cinema target — **Justin Lin / James Wan / Greig Fraser night work**. This is the dark, practical-driven theatrical action night register seen in Tokyo Drift canyon scenes, Fast 5 night work, Furious 7 night chases, The Batman, John Wick. Critical principle: theatrical night cinema is **mostly dark, with hard punchy practicals cutting through**. NOT saturated-teal-everywhere. NOT bright-night.

**Two modes of night cinema:**

**A. EXTERIOR CANYON / OPEN NIGHT (cliff overlooks, canyon roads, remote night):**
- Light comes EXCLUSIVELY from practical sources in the scene (headlights, brake lights, dash glow leaking out doors, distant city glow). No ambient moonlight, no ambient sky lift.
- The sky and surroundings are committed to deep crushed near-black darkness
- A faint horizon glow may be visible at very deep distance — small, contained, abstract neon color (magenta, cyan, warm amber, hot pink) barely readable as far-off civilization, NOT bright enough to illuminate anything in foreground or midground
- Atmospheric haze suspended in air catches headlight beams as visible warm white volumetric god rays
- Headlight backscatter lights only the immediate front of each vehicle and the rocks/ground directly in front
- Everything outside the headlight throws and their immediate backscatter falls into deep crushed near-black shadow
- The cars themselves read primarily as silhouettes against the night sky with their headlight glow defining their forward edges
- This is the Tokyo Drift canyon night register — DARK, with hard warm headlight punch as the only light

**B. INTERIOR / URBAN / LIT NIGHT (parking garages, warehouses, city streets, interior cabins):**
- Practical sources in the scene drive the look — sodium-vapor street lamps, fluorescent garage lights, neon signs, dash glow, brake lights, interior lighting
- Teal-amber color split can read here because practical sources motivate it (cool sodium / fluorescent / neon vs warm dash / brake / amber lights)
- Atmospheric haze gives light volumetric body
- Background subjects readable through the lit zones
- This is the Tokyo Drift parking garage register, Furious 7 night chase register — practical-driven, deep contrast, real teal-amber color split where motivated

**Universal night cinema rules across both modes:**

**Contrast:** Deep cinematic contrast — shadows are deep but hold information, highlights are hot but don't clip into mush. Wide dynamic range that reads on a real cinema screen.

**Practicals punch hard:** Headlights cut through darkness with real intensity and volumetric throw. Brake lights saturate hot red. Dash glow saturates cabin interiors. Light HITS the scene with purpose, not softly diffused into mush.

**Atmospheric haze:** Light volumetric haze suspended in air (canyon dust, urban smog, breath, ground moisture). The haze catches practical light beams as visible volumetric cones. This is what makes light feel real on screen.

**Rim and edge light:** Subjects in night scenes defined against dark backgrounds by rim and edge light from practical sources. Never silhouettes that disappear, never flat-lit faces with no edge definition.

**Skin in night:** Skin reads warm against cool ambient when there's any cool ambient to read against. Real human skin tone preserved through the grade. Practical light sources warm one side of the face — natural face-side-lighting from real cinema gaffer work.

**The reference is unambiguous:** Real theatrical action movie nights projected onto real IMAX screens. Tokyo Drift, Fast 5, Furious 7, The Batman, John Wick. Theatrical, punchy, **mostly dark, with practical light cutting through**. Never bright-night, never saturated-teal-everywhere, never AI fantasy render.

---

## MID-GRAY SEAMLESS BACKDROP (LOCKED DEFAULT FOR ALL CHARACTER WORK)

**Mid-gray seamless is the locked default backdrop** for all character work — face locks, character references, outfit plates, 6-panel sheets, and prop references. **Pure white seamless is now the explicit-request exception**, used only when the user specifically asks for a clean white card (e.g. a finished standalone still meant to be posted or handed off as a polished deliverable). When in doubt, default to gray.

**Why gray as the standing default.** Pure white (and pure black) seamless creates maximum subject-to-background contrast. Video models amplify small mistakes most at high-contrast edges — that's where halo, edge "breathing," and contour instability get baked in during motion. A neutral mid-gray ground lowers the subject-to-background contrast, which means cleaner edge extraction and far less inherited contrast and plastic when the still is read as a reference frame. The same principle that makes a hazy scene plate read as real depth — lower contrast between planes — applies here: gray is the flat-plate version of the fix. Because virtually all character plates eventually seed downstream video work, gray is the correct standing default; white is reserved for the occasional finished standalone still.

**The background stays neutral; the character does not.** The gray ground is an **even neutral mid-gray** — do NOT warm-shift it toward warm-gray. The neutral ground is the locked look. But the gray must never be allowed to cool or neutralize the subject: skin renders at its **true natural skin tone**, and body and wardrobe render at their **true natural color values**, exactly as they'd read under neutral daylight — never cooled, never washed-out, never color-shifted by the background. The relight-from-scratch language and the explicit "warmth preserved and natural, never pale or washed-out or cool-shifted" clause in the lighting close below are what hold this. Keep the background neutral and the subject true.

**The white exception:** only when the user explicitly asks for white. In that case, swap the gray backdrop line for "Pure white seamless studio background, no gradient, no seam line, perfectly even" and close with the full cinema stack instead of the lean Rembrandt grade.

**Lighting close for a mid-gray plate (lean soft Rembrandt grade — use this, NOT the full cinema stack):**

```
Mid-gray seamless studio background — even neutral mid-gray, no seam line, no gradient, no falloff to black or white. Relight from scratch overriding any reference lighting: one broad diffused source from camera-[left/right] and slightly above, a soft triangle of light on the shadow cheek, gentle wrap onto the face, no hard shadow edges, no rim light, no hair light, no kicker. Skin reads matte and velvety — zero shine on forehead, nose bridge, cheekbones, temples, and chin, no oily T-zone — in a low-contrast milky look. Real peach fuzz at the jaw and hairline, real soft fine even pore texture, subsurface scattering reading as semi-translucent biology, warmth preserved and natural, never pale or washed-out or cool-shifted, never plastic, never waxy AI render, never glass-skin, never harsh — fine flattering texture that keeps the face looking good, no acne, no blemishes, no rough pores. Photographed on a 50mm prime at a wide aperture, natural round bokeh, even sharpness, soft natural film grain. Photographed not generated.
```

**Why the lean close, not the full cinema stack:** on a flat seamless plate the full texture-and-grade stack just dilutes — the heavy stack can push contrast back up, which is exactly what the gray ground is trying to lower. The lean Rembrandt close does the matte/specular/warmth work without re-introducing contrast, and its "warmth preserved and natural, never pale or washed-out or cool-shifted" clause is what keeps skin and wardrobe reading at their true natural tone against the neutral gray. This is the same per-zone specular kill the cinema-worldbuilder Capture Realism block uses, applied to a still.

**6-panel sheets:** the gray default applies the same way — use "Mid-gray seamless studio backdrop applied uniformly across all six panels — even neutral mid-gray, no seam line, no gradient," and close with the lean Rembrandt grade above instead of the full cinema stack. Keep everything else (panel layout, identity lock) identical. Only swap to white-across-all-six-panels if the user explicitly asks for a white sheet.

---

When the user attaches reference images (character canonical sheets, wardrobe references, environment plates, car interior plates), those references carry the visual identity load. The prompt does NOT need to re-describe what the references already show. Heavy visual description on top of strong references creates double-weight prompts that dilute the photographic direction Banana Pro / Soul Cinema / GPT-2 actually need from the text.

**The new structure for every prompt this skill produces:**

**1. Identify subjects by short, distinguishing visual descriptors only.**
- "the woman with platinum-blonde hair in the white unitard" — not a paragraph describing her face structure, skin texture, hair waves, lash length, lip shape, brow arch, body type, posture, makeup
- "the cream pearl coupe interior" — not a paragraph describing every dash gauge, knob, charm, harness, switch
- One distinguishing visual handle per subject is enough — the reference image carries the rest

**2. Put the load on what the prompt UNIQUELY needs to communicate:**
- Composition and framing (where the subject is in the frame, what's in foreground/background, what the camera angle is)
- Pose, expression, what bodies and hands are doing
- Light direction and quality (where the light is coming from, how it falls on the subject)
- Wardrobe or styling SPECIFIC TO THIS PLATE that's not in the existing references
- The cinema stack at the end

**3. Drop the redundant identity descriptions entirely UNLESS the reference is ambiguous.**
- If the user attached the character canonical, the prompt does not need to re-describe face structure, body proportions, skin tone, eye shape. Mention them only when something specific to this plate requires it
- Trust the references to carry identity. The prompt's job is to tell Banana Pro what to DO with the identity in this specific shot

**4. When in doubt, lean shorter.**
- A 2500-character Banana Pro prompt with strong references beats a 5000-character prompt every time
- Banana Pro reads the front of the prompt most heavily; loading the front with composition + pose + light gets better results than burying those decisions under visual description
- The references show the model what things LOOK like. The prompt tells the model how to FRAME them.

**Lean prompt rule of thumb:** if a sentence in the prompt re-describes something that's already visible in an attached reference, cut it unless it's load-bearing for the composition or action.

---

## THE CINEMA STACK (LOCKED — APPENDS TO MOST PROMPTS)

Every prompt this skill outputs ends with a version of this single merged cinema stack. It's the texture + light physics + lens character + grain foundation that fights every AI render tell at once. One block, one job — close the prompt with a real photographic register.

```
Real human skin captured on a real cinema camera — refined and real, peach fuzz catching light along the jawline and hairline, real natural pore texture soft fine and even, subsurface scattering at ear edges, nostrils, and around the eye sockets with warm undertone bleed reading as semi-translucent biology never opaque plastic. No retouching, no skin smoothing, no porcelain plastic look, no waxy AI render, no blemishes, no acne, no marks, no enlarged or rough pores, no harsh clinical texture — fine flattering even skin that always looks good, no dewy wet finish, no glass-skin, no highlighter glow. Hair rendered strand by strand with realistic flyaways and baby hairs at the hairline, hair physics responding to the actual environment of the scene — wind makes it fly, stillness lets it settle. Fabric with real weave detail, real weight, real drape. Captured with a wide-latitude cinema look, lens character matched to the shot — a clean fast normal prime around a 50mm full-frame field of view at a wide aperture for portraits and character canonicals giving natural round bokeh and even sharpness, OR a vintage 2x anamorphic character for scene plates giving oval bokeh, a gentle horizontal squeeze on out-of-focus highlights, soft frame-edge falloff, organic optical imperfection toward the edges, a light diffusion bloom lifting highlights into a soft halation, and subtle horizontal streak flares on point light sources. Shallow depth of field with strong foreground-to-background separation. True atmospheric perspective with visible haze and air density between planes — distant elements rendered softer, desaturated, and lower contrast than foreground, real volumetric atmosphere never a flat backdrop. Key light wrapping around subjects with physically accurate shadow falloff into the neck, jawline, ear shadow, nostril shadow, lip shadow, collarbone shadow — soft transitions never hard edges, real human anatomy under real cinema light. Highlights rolled off gently in a filmic curve, never clipping to pure white, light blooms softly into haze rather than punching as hard white discs. Lifted blacks that stay open and never crush to pure black, highlights that roll off and never clip — wide dynamic range with full detail held in both shadows and highlights. Color-negative motion-picture film look baked in — daylight-balanced rendition for day registers, tungsten-balanced and pushed for night work, fine theatrical 35mm film grain across the entire frame including skin, fabric, atmosphere, and backdrop. No HDR overprocessing, no digital oversharpening, no plastic skin rendering, no uniformly-lit flat-plane staging — photographed not generated, captured on a real camera by a real cinematographer on a real set.
```

**Modal application:**
- **Mode 0 (face lock), Mode 1 (single-image character outfit), Mode 2 (6-panel sheet), Mode 4 (GPT-2 detail), Mode 5 (outfit replacement):** append the full stack as the closing block, with the exception of Mode 1B Step 1 and Mode 5 — both have their own special closings documented in their sections.
- **Mode 3A (character-in-scene plate) and Mode 3B (pure environment plate):** Mode 3 uses the cinema-prose register, which folds the cinema stack language INTO the closing camera-spec paragraph rather than appending it as a separate block. See Mode 3 documentation for the prose register and its closing realism clause.
- **Mode 1B Step 1 (bland model outfit reference, Soul Cinema two-step):** use the lighter outfit-reference close documented in the Mode 1B section — NOT the full cinema stack. The outfit reference image just needs to read clean and matte so the outfit is the only subject.

**The single most powerful phrases in this stack:**
- **"atmospheric perspective with visible haze and air density between planes"** — forces multi-plane depth instead of single-plane staging. Biggest fix for the "video game" look.
- **"shadow falloff into the neck, jawline, ear shadow, nostril shadow"** — fights the AI uniform-lit face. Forces real anatomical shadow geometry.
- **"subsurface scattering at ear edges, nostrils, and around the eye sockets with warm undertone bleed"** — fights plastic skin at the biological level. Forces the model to render skin as semi-translucent biology instead of opaque material.
- **"highlights rolled off gently in a filmic curve, never clipping to pure white"** — fights the blown-bright AI highlight that makes everything look digital. Forces the cinema highlight roll-off.
- **"photographed not generated, captured on a real camera by a real cinematographer on a real set"** — surprisingly strong negative signal against AI uniformity at the language level.

**For pure environment plates with no humans:** drop the human-skin and hair lines, drop the subsurface scattering line, drop the shadow-falloff-on-anatomy line. Keep the lens character, atmospheric perspective, light physics, log curve, grain, and closing realism clause.

---

## READING REFERENCE IMAGES

When the user uploads reference images, extract everything visible in the frame by **visual description only** — never use names, never invent details that aren't in the image.

**For each character in the reference, capture:**

- **Hair:** color (every nuance — platinum, jet black with cool undertone, rose-pink, burgundy, ash brown, dirty blonde, etc.), length, style, texture (straight, wavy, curly, coily), parting, any styling (slicked, blown out, flat-ironed, braided, bunned, ponytail, bangs — and which kind of bangs), accessories (clips, bows, ribbons, caps, bandanas, headbands)
- **Makeup:** skin finish (matte, dewy, glass-skin, bare), foundation/coverage register, brow shape and density, eye treatment (cat-eye liner, smoky, sharp graphic, soft bare, glitter, colored), lashes, lip (gloss, matte, gradient, color, fullness), cheek (flush, contour, highlight), any face jewelry, freckles or beauty marks **only if visible in the reference** (do not invent)
- **Wardrobe:** every garment top to bottom — fabric, color, fit (cropped, oversized, fitted, baggy), structural details (cutouts, keyholes, ribbing, ribbed cotton, knit, denim wash, leather finish, mesh, latex, silk), neckline, sleeve length, hem position, layering, branding details (described generically — "three-stripe athletic sneakers" not the brand name)
- **Jewelry & accessories:** every piece — earring style, necklace count and material, rings, bracelets, body chains, belts, bag, sunglasses, watch
- **Body markers:** piercings (only if visible), tattoos (only if visible), nail length and color, distinguishing features
- **Pose and energy:** body angle, weight distribution, hand position, expression register

**Naming rule (CRITICAL).** Never use proper names in the prompt output. Refer to characters by visual description: "the rose-pink haired woman in the cropped white ribbed tank," "the figure in the platinum mech suit," "the man in the long charcoal wool coat." Higgsfield does not know names. Visual descriptors survive across prompts; names do not.

**Brand name rule (CRITICAL).** Never use real brand names or protected IP in the prompt output. Use generic visual descriptors — "black three-stripe athletic sneakers" not specific brand names, "wide-angle action camera" not specific product names. Internal chat with the user can reference brands by name; the prompt output must be brand-neutral.

**Age-blind rule.** Never describe characters by age. Avoid: *boy, girl, child, kid, young, teen, little, middle-aged, elderly, old.* Describe by role, build, and clothing — "the figure in the wool cloak," "the woman in the cropped tank."

**No-invention rule.** If the user gives you a reference image and asks for the same character in a new scene, do not invent wardrobe or styling details that aren't in the image or specified in the request. If something is needed but not specified (e.g., a new outfit for a new scene), ask before composing.

---

## MODE 0 — FACE LOCK (NEW CHARACTERS ONLY)

**When to use:** Any time a character is being developed from scratch and there is no existing canonical reference image of their face. Run this BEFORE any outfit work, any 6-panel sheet, any scene plate. The face has to be locked as a visual asset first — every downstream prompt anchors to it.

**Goal:** Produce the canonical face reference for the character. Identity only — no outfit considerations beyond a locked neutral baseline top, no environment, no posing direction. Just: a clean, locked face on white background with soft soft lighting that makes the skin read matte and cinema-placement-ready.

**Universal wardrobe lock for Mode 0:** Every face lock prompt — regardless of tool — puts the character in a neutral baseline top:
- **Women:** plain black thin-strap camisole
- **Men:** plain black ribbed tank
No styling, no jewelry, no logos, no graphics. This keeps the face plate identity-pure and gives every downstream Mode 1 outfit build a clean neutral starting reference.

---

### Tool fork — pick one (ask the user first)

Before any prompt, ask the user which tool to use for the face lock. Three options:

> Want to build this in Banana Pro, GPT-2, or Soul Cinema?
> — **Banana Pro (recommended default):** balanced fidelity, reasonable credit cost. Works for most character builds straight up. Single-pass build, no Step 0.1 needed.
> — **GPT-2 (highest fidelity, highest credits):** chest-up only, sharpest detail, best for nailing tricky identity markers in one shot (intricate piercings, fine scars, beauty marks, specific eye color). Heads-up — uses considerably more Higgsfield credits than Banana Pro.
> — **Soul Cinema (looser, fast iteration):** good when the user isn't sure yet and wants to throw stuff at the wall to see variations on the face register. Lower fidelity than Banana Pro but faster to iterate. If used, run as Step 0.1 first to produce a face plate, then a Banana Pro 3:4 pass (Step 0.2) to lock the finer detail.

Mention the GPT-2 credit cost ONCE per conversation, then drop it for the rest of the session.

Wait for the user to pick. Then proceed to the matching step.

---

### Step 0.A — Banana Pro single-pass face lock (default)

**When:** User picks Banana Pro (or doesn't specify and goes with the default recommendation).

**How:** Single-pass Banana Pro generation, no Soul Cinema plate required. The prompt itself locks identity markers in one shot.

**Pre-prompt check:**

Pre-prompt check — Banana Pro face lock (single-pass):
- **Reference attached:** none — text-only build
- **Character spec:** [identity essentials only — heritage, build, skin, hair color + length + texture, eye shape + color, key identity markers like beauty marks/scars/piercings]
- **Wardrobe:** plain black [camisole / ribbed tank]
- **Backdrop:** mid-gray seamless studio (locked default)
- **Lighting:** soft soft natural light from camera-[left/right]
- **Framing:** 3:4 headshot, forehead to upper chest, face filling most of the frame

Sound good?

**Canonical Step 0.A prompt structure:**

```
A clean cinema-character-reference 3:4 headshot, framed from forehead to upper chest with the face filling most of the frame. [Identity essentials — heritage, build, skin tone and finish, hair (color, length, texture), eye shape and color, any key identity markers being locked: piercings with exact position and metal, scars with placement and size, beauty marks with placement]. She wears [a plain black thin-strap camisole / he wears a plain black ribbed tank], no jewelry, no logos, no graphics. Body squared to camera, head level, neutral relaxed expression, eyes to camera, lips closed and relaxed, subtle controlled energy.

Mid-gray seamless studio background — even neutral mid-gray, no seam line, no gradient, no falloff to black or white. Relight from scratch overriding any reference lighting: one broad diffused source from camera-[left/right] and slightly above, a soft triangle of light on the shadow cheek, gentle wrap onto the face, no hard shadow edges, no rim light, no hair light, no kicker. Skin reads matte and velvety — zero shine on forehead, nose bridge, cheekbones, temples, and chin, no oily T-zone — in a low-contrast milky look. Skin renders at its true natural skin tone and wardrobe at its true natural color, warmth preserved and natural against the neutral gray, never pale or washed-out or cool-shifted by the background. Real peach fuzz at the jaw and hairline, real soft fine even pore texture, subsurface scattering reading as semi-translucent biology, never plastic, never waxy AI render, never glass-skin, never harsh — fine flattering texture that keeps the face looking good, no acne, no blemishes, no rough pores. Photographed on a 50mm prime at a wide aperture, natural round bokeh, even sharpness, soft natural film grain. Photographed not generated.

[Gray is the locked default — use the lean Rembrandt close above. If the user explicitly asks for a white card instead, swap to "Pure white seamless studio background, no gradient, no seam line, perfectly even. Soft soft cinematic light from camera-[left/right], very diffused, gentle wrap onto the face, no hard shadow edges, no rim light, no hair light, no kicker. Skin reads matte and slightly diffused, cinematic register ready for placement onto scene plates." and append the full cinema stack from "THE CINEMA STACK" section instead of this lean close.]

---

### Step 0.B — GPT-2 single-pass face lock (highest fidelity)

**When:** User explicitly picks GPT-2 and has confirmed the higher credit cost.

**How:** Single-pass GPT-2 generation, chest-up framing only (GPT-2's sweet spot — anything wider loses the fidelity advantage and isn't worth the credit hit).

**Pre-prompt check:**

Pre-prompt check — GPT-2 face lock (single-pass, chest-up only):
- **Reference attached:** none — text-only build
- **Character spec:** [identity essentials only — heritage, build, skin, hair color + length + texture, eye shape + color, key identity markers]
- **Wardrobe:** plain black [camisole / ribbed tank]
- **Backdrop:** mid-gray seamless studio (locked default)
- **Lighting:** soft soft natural light from camera-[left/right]
- **Framing:** chest-up portrait, face dominant in the frame

Sound good?

**Canonical Step 0.B prompt structure:** Use the GPT-2 prompt structure documented in the GPT-2 section of this skill (Mode 4). Apply the same identity essentials, wardrobe lock, white backdrop, and soft soft lighting as Step 0.A — just routed through the GPT-2 prompt grammar instead of the Banana Pro grammar.

---

### Step 0.1 + Step 0.2 — Soul Cinema two-pass face lock (iteration path)

**When:** User picks Soul Cinema. Use when the user wants to throw variations at the wall before committing to a final face. Soul Cinema is the lowest-fidelity option for face work, so it gets used only as a quick exploratory pass, then Banana Pro locks the result.

### Step 0.1 — Soul Cinema face plate

Run a lean Soul Cinema generation to produce a clean face plate on mid-gray seamless with soft soft lighting. The plate is exploratory — identity essentials only, no makeup detail, no granular facial anatomy, no fine identity markers (those go into Step 0.2 where Banana Pro can actually hold them).

**Pre-prompt check:**

Pre-prompt check — Step 0.1 of 2 (Soul Cinema face plate):
- **Reference attached:** none — text-only build
- **Character spec:** [identity essentials only — heritage, build, skin tone, hair (color, length, texture), eye shape and color, beauty marks / scars only if they're large/obvious — fine markers held for Step 0.2]
- **Wardrobe:** plain black [camisole / ribbed tank]
- **Backdrop:** mid-gray seamless studio (locked default)
- **Lighting:** soft soft natural light from camera-[left/right]
- **Framing:** chest-up, face clearly readable, body squared to camera

Sound good?

**Canonical Step 0.1 prompt structure (lean — identity essentials only):**

```
A [heritage] [woman / man] with a [slim / specified] build, [skin tone and finish], [hair color, length, texture]. [Eye shape and color]. [Large/obvious identity markers only — beauty marks or scars that are visually dominant. Hold fine markers for Step 0.2]. [She wears a plain black thin-strap camisole / He wears a plain black ribbed tank], no jewelry, no logos, no graphics. Body squared to camera, head level, neutral relaxed expression, eyes to camera, lips closed and relaxed.

Mid-gray seamless studio background — even neutral mid-gray, no seam line, no gradient. Soft soft natural light from camera-[left/right], very diffused, no hard shadow edges, no rim light, no hair light, no kicker, no harsh directional studio lighting. The light produces only the gentlest lifted shadow on the off-light side of the face. Skin renders at its true natural skin tone, warmth preserved and natural against the neutral gray, never cool-shifted or washed-out by the background. Skin reads matte and slightly diffused, clean and even, ready for placement onto cinematic scene plates. Chest-up framing.

Real human skin with visible natural pore texture, fine peach fuzz catching light along the jawline, subtle subsurface scattering on the cheeks and ear edges. Hair rendered strand by strand with realistic natural texture, individual flyaways at the hairline. Fine cinema grain. Lived-in, not pristine. Photographic, not rendered.
```

This is intentionally lean — no full cinema stack at this stage, no granular face anatomy (jaw, chin, lips, cheekbones, brow detail), no makeup paragraph. Let Soul Cinema interpret the face from the essentials. Step 0.2 locks the rest.

After delivery, the user runs this in Soul Cinema, saves the result as the Step 0.1 face plate reference.

### Step 0.2 — Banana Pro 3:4 headshot to lock the full facial character

Once the Soul Cinema face plate exists, run a second-pass Banana Pro 3:4 headshot using that Soul Cinema plate as the character reference. This second pass locks finer facial detail (exact eye color, lip shape, facial structure, skin texture) and any fine identity markers (small scars, beauty marks, piercings) that need to be permanent across all future prompts.

**Pre-prompt check:**

Pre-prompt check — Step 0.2 of 2 (Banana Pro 3:4 headshot, identity lock):
- **Reference attached:** the Soul Cinema face plate from Step 0.1
- **Character spec:** [same essentials as Step 0.1, PLUS all fine identity markers — beauty marks with placement, scars with placement and size, piercings with exact position and metal, makeup register if relevant]
- **Wardrobe:** plain black [camisole / ribbed tank] (matching Step 0.1)
- **Backdrop:** mid-gray seamless studio (locked default)
- **Lighting:** soft soft from camera-[left/right] (matching Step 0.1)
- **Framing:** 3:4 headshot, forehead to upper chest, face filling most of the frame

Sound good?

**Canonical Step 0.2 prompt structure:**

```
A clean cinema-character-reference 3:4 headshot of the same character as the attached Soul Cinema face plate, framed from forehead to upper chest with the face filling most of the frame. [Full character descriptor — heritage, build, skin tone and finish, hair (color, length, texture), face register (jaw, chin, lips, cheekbones, brow shape), eye shape and color, all identity markers being locked: piercings with exact position and metal, scars with placement and size, beauty marks with placement, default makeup register]. She wears [a plain black thin-strap camisole / he wears a plain black ribbed tank], no jewelry, no logos, no graphics. Body squared to camera, head level, neutral relaxed expression, eyes to camera, lips closed and relaxed, subtle controlled energy.

Mid-gray seamless studio background — even neutral mid-gray, no seam line, no gradient, no falloff to black or white. Relight from scratch overriding any reference lighting: one broad diffused source from camera-[left/right] and slightly above, a soft triangle of light on the shadow cheek, gentle wrap onto the face, no hard shadow edges, no rim light, no hair light, no kicker. Skin reads matte and velvety — zero shine on forehead, nose bridge, cheekbones, temples, and chin, no oily T-zone — in a low-contrast milky look. Skin renders at its true natural skin tone and wardrobe at its true natural color, warmth preserved and natural against the neutral gray, never pale or washed-out or cool-shifted by the background. Real peach fuzz at the jaw and hairline, real soft fine even pore texture, subsurface scattering reading as semi-translucent biology, never plastic, never waxy AI render, never glass-skin, never harsh — fine flattering texture that keeps the face looking good, no acne, no blemishes, no rough pores. Photographed on a 50mm prime at a wide aperture, natural round bokeh, even sharpness, soft natural film grain. Photographed not generated.

[Gray is the locked default — use the lean Rembrandt close above. If the user explicitly asks for a white card instead, swap to the white-backdrop line and append the full cinema stack from "THE CINEMA STACK" section instead of this lean close.]
```

After delivery, the user runs this in Banana Pro. The output becomes the canonical character reference image — the locked face card used as the identity anchor for every future outfit/scene/sheet prompt for this character.

**Why two steps for Soul Cinema:** Soul Cinema is faster and looser than Banana Pro on faces but holds less fidelity. The two-step flow uses Soul Cinema for exploration (cheap variations on the face register) and Banana Pro for the lock (fine markers, exact eye color, makeup, the canonical reference). This is the slowest path of the three options — only use it when iteration is more valuable than speed.

---

**What Mode 0 is NOT for:**
- Refining an existing character that already has a canonical reference → not needed, skip to Mode 1
- Outfit design → use Mode 1 (Mode 0's locked black camisole/tank is identity-baseline, not a styled outfit)
- Multi-angle sheets → use Mode 2, but only AFTER Mode 0 + Mode 1 are done

Mode 0 is one-and-done per character. Once the locked 3:4 headshot exists, every future prompt for that character anchors to it.

---

## MODE 1A — SINGLE-IMAGE CHARACTER OUTFIT, BANANA PRO PATH

**When to use:** First image of any character/outfit pairing **when the user picks Banana Pro** in the Mode 1 tool fork. Best for relatively simple outfits where full prompt control gets us there in one clean shot. Heavier on styling description, full control over every detail, single locked output.

**Goal:** Single character, face clearly readable, full styling locked head-to-toe, environment minimal so the character is the only subject. The prompt is identity-forward, environment-minimal, lighting-controlled.

**Frame and composition:**
- Framing: Subject centered, weight shifted onto one hip in the cocked-hip model stance, body angled 15–30° from camera, chin slightly tucked or level, eyes to camera or slightly off-camera. Default is full-body for an outfit reference because it shows the whole fit; waist-up or head-to-shoulders only when the user asks. Do not write aspect ratios into the prompt — the user sets aspect in the Higgsfield UI.
- Background: **Mid-gray seamless studio.** The locked default for all character/outfit work — even neutral mid-gray, no seam line, no gradient. Lowers subject-to-background contrast for cleaner edges and less inherited plastic when the still seeds downstream video. **Exception:** if the user explicitly asks for a clean white card (a finished standalone still to post or hand off), swap to pure white seamless and use the full cinema stack close instead of the lean Rembrandt grade.
- Lighting: Soft soft cinematic key from camera-left or camera-right (user picks side), very diffused, gentle wrap onto the figure, no harsh shadows, no rim light, no hair light, no kicker — only the gentlest lifted shadow on the off-light side. Skin reads matte and slightly diffused, cinema-placement ready.

**Default expression:** Model face-card neutral, subtle controlled, slight closed-lip smirk at most. Never teeth-showing smile unless the user specifically requests it.

**Canonical Mode 1A prompt structure:**

```
[Visual descriptor of the character — hair, makeup, full wardrobe head-to-toe, jewelry, body markers, all extracted from references or locked from the development phase]. [Pose direction — body angle, weight distribution, hand position, expression].

Mid-gray seamless studio background — even neutral mid-gray, no seam line, no gradient, no falloff to black or white. Relight from scratch overriding any reference lighting: one broad diffused source from camera-[left/right] and slightly above, gentle wrap onto the figure, no harsh shadows, no rim light, no hair light, no kicker, only the gentlest lifted shadow on the off-light side. Skin and fabric read matte and velvety in a low-contrast milky look, no shine, no oily T-zone. Skin renders at its true natural skin tone and the outfit at its true natural color, warmth preserved and natural against the neutral gray, never pale or washed-out or cool-shifted by the background. Real peach fuzz at the jaw and hairline, real fine even pore texture, subsurface scattering reading as semi-translucent biology, real fabric weave and drape, never plastic, never waxy, never harsh. Photographed on a 50mm prime at a wide aperture, natural round bokeh, even sharpness, soft natural film grain. Photographed not generated. [Framing — full body / waist-up / head-to-shoulders].

[Gray is the locked default — use the lean Rembrandt close above. If the user explicitly asks for a white card, swap to "Pure white seamless studio background, no gradient, no seam line, perfectly even. Soft soft cinematic light from camera-[left/right]..." and append the full cinema stack from "THE CINEMA STACK" section instead of this lean close.]
```

**Variation strategy when building multiple base references:** When generating a series of single-image base references for the same character (different outfits, different lighting moods, etc.), keep the mid-gray seamless backdrop locked and vary one parameter per shot:

- Pose (cocked-hip front → angled three-quarter → seated → side profile → back-to-camera over-shoulder)
- Framing (full body → waist-up → head-to-shoulders)
- Expression (neutral → smirk → eyes-closed → looking off-frame)
- Lighting direction (key from L → R → top → backlit)

Don't vary face, skin, or core identity markers. Those stay locked.

---

## MODE 1B — SINGLE-IMAGE CHARACTER OUTFIT, SOUL CINEMA PATH

**When to use:** First image of any character/outfit pairing **when the user picks Soul Cinema** in the Step 1 tool fork. Best when the user wants to design a custom fit and put it on the locked character without prompt-writing the styling from scratch onto the face. Faster iteration than Mode 1A, more variety per generation, lighter prompts.

**How it works — TWO-STEP FLOW (critical):**

Soul Cinema is a two-step process. Do not skip Step 1B.1 and jump straight to compositing.

### Step 1B.1 — Generate the outfit on a neutral model

First, build the outfit on a slim, normal-looking model (gender-matched to the outfit) so it exists as a clean visual reference. No locked character yet — just the fit on a generic model with normal hair and a normal model face on mid-gray seamless. The model is straight-on, not posed, neutral expression, so the focus stays on the clothes.

**Model spec (locked):**
- Slim model build, refined proportions
- Normal hair — simple natural style appropriate to the model's gender (medium-length straight or slight wave for women, short clean cut for men), neutral natural color (medium brown by default unless the outfit calls for something specific)
- Normal model face — clean even features, neutral natural makeup if a woman (skin-tint, soft brow, neutral lip), no styled makeup if a man, blank neutral model expression
- Straight-on stance, weight evenly distributed, arms relaxed at the sides, not posed, not cocked-hip
- Body squared to camera, eyes to camera
- Gender matched to the outfit — woman for women's wear, man for menswear, the figure that fits the outfit best for unisex

**Pre-prompt check (clean bullet format):**

Pre-prompt check — Step 1 of 2 (build the fit):
- **Subject:** slim [woman/man], normal hair, neutral model face, straight-on relaxed stance
- **Outfit:** [full outfit description — every garment, accessory, jewelry, footwear]
- **Backdrop:** mid-gray seamless studio (locked default)
- **Lighting:** soft soft natural light from camera-[left/right] (user picks side)

Sound good?

**Canonical Step 1B.1 prompt structure:**

```
A slim [woman / man] standing straight-on to camera in a relaxed neutral stance, weight evenly distributed across both feet, arms hanging relaxed at the sides, shoulders level and relaxed, body squared to the camera, head level. Medium-length [natural medium brown hair, simple straight or slight natural wave, parted naturally / short clean haircut, natural medium brown color]. Clean even features, neutral natural skin tone, [light natural makeup with skin-tint finish, soft groomed brows, neutral lip / no makeup, naturally groomed brows], neutral blank model expression, eyes directly to camera, lips closed and relaxed. Slim model build with refined proportions. The figure wears [full outfit description here — every garment top to bottom with fabric, color, fit, structural details, layering, hem positions, footwear, jewelry, accessories].

Mid-gray seamless studio background, even neutral mid-gray, no shadow falloff to black or white, no visible seam line, perfectly even backdrop. Soft soft natural light from camera-[left/right], very diffused, gentle wrap onto the figure, no harsh shadows, no dramatic rim light, no kicker, no hair light — only the gentlest lifted shadow on the off-light side. Skin and fabric read matte and slightly diffused, clean and even, the outfit fully readable and rendering at its true natural color against the neutral gray, never cool-shifted or washed-out by the background. Full body framing from head to just below the footwear.

Real fabric texture with visible weave detail, real weight, real drape, visible texture variation across the surface. Jewelry with real metal surface detail. Real human skin with natural pore texture. Fine cinema grain, soft lens vignette, natural color grade. Photographic, not rendered.
```

Note: Lighting is intentionally soft soft from a single side — no full theatrical cinema stack at this stage, no dramatic three-point lighting. The outfit is the only subject. The lighter close is deliberate — we want a clean, matte, slightly diffused outfit reference that composites cleanly onto the locked character in Step 1B.2 without dragging cinema register baggage along. Run this in Soul Cinema. The user saves the result — that's the outfit reference for Step 1B.2.

### Step 1B.2 — Composite the outfit onto the locked character

Once the outfit reference exists from Step 1B.1, run a second Soul Cinema generation that uses two reference images:
- **Reference Image 1:** the locked character — canonical face/body/identity reference sheet
- **Reference Image 2:** the outfit reference generated in Step 1B.1 — the neutral model in the locked fit

Both images are uploaded directly in the Higgsfield UI.

**Pre-prompt check (clean bullet format):**

Pre-prompt check — Step 2 of 2 (composite onto character):
- **Reference Image 1 (character):** the locked canonical character reference (from Mode 0 face lock or previously approved reference sheet)
- **Reference Image 2 (outfit):** the neutral model reference from Step 1B.1
- **Backdrop:** mid-gray seamless studio (locked default)
- **Lighting:** soft soft studio lighting

Sound good?

**Canonical Step 1B.2 prompt structure:**

```
Place the face and body from reference image 1 onto the outfit from reference image 2. Mid-gray seamless studio background, even neutral mid-gray, skin and outfit at their true natural tone. Soft studio lighting.
```

That's it. Do not add styling description (Soul Cinema reads it from Image 2). Do not add character description (Soul Cinema reads it from Image 1). Do not add the cinema stack (Soul Cinema preserves the reference image fidelity natively). Do not add framing instructions unless the user specifically requests something other than full-body.

**Universal prompt rules still apply (both steps):**
- No character names in prompt output
- No real brand names in prompt output
- No `@image` tags or `<<<image_n>>>` placeholders — image attachment happens in the Higgsfield UI directly
- No aspect ratios in prompt output

**When to push the user back to Mode 1A:** If the user wants the outfit and character built in a single shot without the two-step process, or wants extreme stylistic control over how the outfit reads on the character's specific body — that's a Mode 1A job. Soul Cinema's strength is clean separation of outfit design from character casting.

---

## MODE 2 — 6-PANEL CHARACTER SHEET (SINGLE 16:9 FRAME)

**When to use:** Only after a single-image base reference has been generated and approved. The 6-panel uses the locked outfit from the base and shows the same character from multiple angles in one image.

**Critical:** Never deliver six separate prompts. Always one prompt → one 16:9 image → six panels in a 3×2 grid.

**Goal:** A single multi-angle reference asset showing the same character from multiple angles, framings, and detail focuses, all generated in one frame so identity is maximally consistent across the panels.

**Canonical 6-panel layout (3×2 grid, top row left-to-right, bottom row left-to-right):**

1. **Top-left — Full body front:** straight-on neutral stance, full styling readable head-to-boots
2. **Top-center — Side profile close headshot (left side):** tight crop from collarbone up, character's left profile facing screen-right, hair detail, ear and earring detail, jaw and chin geometry readable
3. **Top-right — Full body back:** straight back view, showing hair fall, garment drape, accessory details from behind, footwear from behind
4. **Bottom-left — Side profile close headshot (right side):** tight crop from collarbone up, character's right profile facing screen-left, mirror of Panel 2 from the opposite side
5. **Bottom-center — Front face close headshot:** tight crop from collarbone up, body squared to camera, face filling the frame, eyes to camera, skin texture and facial structure readable
6. **Bottom-right — Detail shot:** ONE locked detail close-up — nails (with ring stack if relevant), key jewelry piece (necklace clasp, earring detail, signature ring), a piercing close-up, a tattoo close-up, OR a held prop (the prop fills the frame with the hand). User picks which detail at the pre-prompt check.

**Variation rule:** If the user requests a different mix of panels (e.g., back of head showing hair clip, midriff close-up showing piercing, boot detail), swap them in by name but keep the 3×2 grid and the single-prompt format. The default layout above is what gets used if the user doesn't specify.

**Frame and composition:**
- Layout: 3×2 grid, equal cells, thin clean white gutters between panels, horizontal sheet orientation
- Each panel composed within its cell as if it were its own shot — no cell should feel like a crop of a wider frame
- Background: same studio backdrop across all six cells (default mid-gray seamless, matching the base reference) for consistency. Only swap to white-across-all-six-panels if the user explicitly asks for a white sheet (see the MID-GRAY SEAMLESS BACKDROP section).
- Lighting: same three-point key/fill/rim setup across all six cells — identity stays locked when lighting is locked
- Do not write aspect ratios into the prompt — the user sets aspect in the Higgsfield UI (typically 16:9 for sheets, but specified in UI not prompt)

**Canonical Mode 2 prompt structure:**

```
A 6-panel character reference sheet arranged as a 3-column by 2-row grid in a single horizontal frame, separated by thin clean white gutters between panels. Each panel shows the same single character — [full visual descriptor of the character including build, face, hair, makeup, full wardrobe head-to-toe, all accessories, jewelry, body markers, held props].

Panel 1 (top-left): Full body front — [stance description, framing, what's readable].
Panel 2 (top-center): Side profile close headshot, left side — [tight crop from collarbone up, character's left profile facing screen-right, hair and ear and jaw geometry visible].
Panel 3 (top-right): Full body back — [stance, what's visible from behind].
Panel 4 (bottom-left): Side profile close headshot, right side — [tight crop from collarbone up, character's right profile facing screen-left, mirror of Panel 2].
Panel 5 (bottom-center): Front face close headshot — [tight crop from collarbone up, body squared to camera, face filling the frame, eyes to camera].
Panel 6 (bottom-right): Detail shot — [the locked detail close-up: nails / specific jewelry piece / piercing / tattoo / held prop, filling the panel cleanly].

Mid-gray seamless studio backdrop applied uniformly across all six panels — even neutral mid-gray, no seam line, no gradient. Relight from scratch overriding any reference lighting, applied uniformly across all six panels: one broad diffused source from camera-left and slightly above, gentle wrap, no harsh shadows, no rim light, no hair light, no kicker. Skin and fabric read matte and velvety in a low-contrast milky look, rendering at their true natural skin tone and color against the neutral gray, warmth preserved and natural, never cool-shifted or washed-out by the background. Sharp focus across every panel. Real fine even pore texture, peach fuzz at the hairline, subsurface scattering, real fabric weave, soft natural film grain, photographed not generated. Identical character identity locked across all six panels — same face, same skin, same hair, same wardrobe, same accessories, same proportions in every cell.

[Gray is the locked default — use the lean Rembrandt grade above. If the user explicitly asks for a white sheet, swap to "Pure white seamless studio backdrop applied uniformly across all six panels" and append the full cinema stack instead of this lean close.]
```

**Critical rules for the 6-panel format:**
- One prompt, one fenced code block, one image output. Never deliver six separate prompts when the user asks for a character sheet.
- Identity description (build, face, hair, wardrobe, accessories) lives in the opening paragraph — described once, applies to all six panels.
- Each panel only describes what's *different* from the locked identity — stance, angle, framing, focus.
- Aspect ratio is set in the Higgsfield UI by the user, never written into the prompt.
- Lighting and backdrop are always uniform across all six cells.
- Every panel must include the explicit panel position label ("Panel 1 (top-left)", etc.) so Banana Pro can compose the grid correctly.

---

## MODE 3 — CINEMATIC SCENE PLATE

**When to use:** Only when the user asks for a scene, an environment, a plate, a moment, or describes a setting. Never proposed proactively.

Two flavors:

- **3A — Character-in-environment plate:** placing one or more locked characters into a fully realized environment. Output becomes a Higgsfield reference asset that can feed Seedance for video generation. Camera language matches the cinema mode the eventual video will use.
- **3B — Pure environment plate:** no characters in frame. Pure location, lighting, atmosphere, set dressing. Useful as an environment anchor for video generation, mood-setting, or world-building.

**Goal:** A single still that captures the world (and the character, when present) and the camera grammar — as if a cinematographer locked off and grabbed a photo on the same camera package mid-take.

**Camera grammar — five cinema modes paired to scene type.** Pick the cinema mode that matches the scene. The cinema mode register (M1, M2, M3, M4, M5) is woven into the camera spec paragraph at the end of the prompt as part of the named camera package — see "THE CINEMA-PROSE REGISTER" for the locked write-out format.

| If the scene is... | Cinema mode |
|---|---|
| Real-world dramatic (street, kitchen, car, bar, interior, exterior location) | M1 — Narrative |
| Studio / editorial / void / clean set / fashion film | M2 — Studio / Editorial |
| Action / combat / chase / high-energy physical | M3 — Action / Combat |
| Performance / concert / stage / pit | M4 — Performance / Concert |
| Atmospheric / empty / no-humans / weather plate | M5 — Atmospheric / Empty |

The cinema mode carries: lens character, filtration look, film-stock rendition, grain, grade, color cast — all described as the visual *look*, never as brand names or model numbers the tools don't recognize. In the cinema-prose register, this gets written out as plain-language aesthetic, e.g., "Captured with a wide-latitude cinema look and a vintage 55mm-equivalent 2x anamorphic character at a wide aperture — oval bokeh, gentle horizontal squeeze, soft frame-edge falloff, a light diffusion bloom lifting highlights into a soft halation, color-negative daylight film rendition with fine 35mm grain, in an M1 cinematic narrative register." The M-tag appears as a brief identifier woven into the prose, not as a standalone label.

---

### THE SILENT 6-BLOCK MENTAL CHECKLIST (PRE-COMPOSITION ONLY)

Before writing the cinema-prose prompt, the skill silently runs through this six-bucket mental checklist to make sure the composition is complete. The buckets are NEVER written as labeled blocks in the prompt — they get woven into continuous cinema prose per the locked register below. This checklist is a thinking tool, not an output structure.

**Bucket 1 — Shot DNA.** Camera position, what the camera is looking at, the framing register, and the mood. The spine of the shot.

**Bucket 2 — Subject behavior + spatial placement.** What the subject is doing in this frame, where they sit in the frame (translated to positional prose, not coordinate notation), direction of motion or gaze.

**Bucket 3 — Visible detail (resolution-aware).** Only the details a real camera at this distance, lens, and motion register would resolve. (Resolution-aware rule documented below.)

**Bucket 4 — World.** Environment as ambience, not architecture. The space's register matters more than counting structural elements. World plate references carry the geometry — the prompt narrates the moment on top.

**Bucket 5 — Light and atmosphere.** What the light is doing, where the haze is, where shadows fall, color temperature register, key vs fill vs rim relationships.

**Bucket 6 — Camera spec + finish.** Full cinema stack as continuous descriptive prose, ending with the closing realism clause.

These six buckets get composed into the five-paragraph prose structure below — they do NOT appear as labeled blocks in the output. See "THE CINEMA-PROSE REGISTER" for the actual write-out format.

---

### RESOLUTION-AWARE DETAIL RULE (LOCKED)

**Describe what the camera at this position can physically see, not what's "true" about the subject.**

Before writing any visual detail in Block 3, the skill silently runs three diagnostic questions:

1. **At this distance, would a real cinema lens resolve this detail?** If no, drop it.
2. **At this motion blur level, would this detail read?** If no, drop it.
3. **At this lighting register, would this detail be visible?** If no, drop it.

**Examples of what this rule kills:**

- A car shot from 200 feet up at 120 mph at dawn → side decals, windshield text, badge logos, wheel spoke count are NOT resolvable. Drop them. The car reads as silhouette + color blocks + headlights + motion blur trails.
- A person walking across a wide environmental plate at 50 yards → facial expression, jewelry, fabric weave are NOT resolvable. Drop them. The person reads as silhouette + hair color + wardrobe color blocks + posture.
- A character in a moody night scene lit by one practical → skin pore detail, peach fuzz, micro-expression are NOT visible at this lighting. Drop them. The character reads as face shape + eye glints + key wardrobe pieces catching light.

**Examples of what this rule preserves:**

- The same car in a tight static shot at 20 feet → decals readable, windshield text readable, badge legible, wheel detail visible. Describe them.
- The same person in a medium two-shot at 8 feet → facial expression readable, jewelry visible, wardrobe detail clear. Describe them.

**Detail is earned by camera proximity, lens length, motion stillness, and lighting intensity. The skill respects this physics.**

---

### X/Y COORDINATE SYSTEM (MENTAL COMPOSITION TOOL — NOT OUTPUT NOTATION)

**The X/Y coordinate system is the skill's internal composition tool. It is NEVER written into the prompt body in the cinema-prose register.** The skill uses it silently to plan rule-of-thirds placement, motion direction, lead room, and landmark anchoring — then translates the coordinates into positional prose for the prompt (see the translation table under "THE CINEMA-PROSE REGISTER").

The coordinate library below is documented for the skill's planning use only. It does not appear in the output.

**Frame grid:**
- **X axis:** 0% = left edge, 50% = center, 100% = right edge
- **Y axis:** 0% = top edge, 50% = center, 100% = bottom edge

**Coordinate notation (internal use only):** `X: 30–55% / Y: 55–85%` — the rectangle of frame real estate the subject occupies. Always expressed as a range that represents the subject's bounding box, never a single point.

**Rule-of-thirds anchor table (locked vocabulary):**

| Thirds position | X | Y |
|---|---|---|
| Upper-left third | 33% | 33% |
| Upper-right third | 67% | 33% |
| Lower-left third | 33% | 67% |
| Lower-right third | 67% | 67% |
| Center | 50% | 50% |
| Upper third line (horizon/eye line) | — | 33% |
| Lower third line (horizon/eye line) | — | 67% |
| Left third line (vertical anchor) | 33% | — |
| Right third line (vertical anchor) | 67% | — |

**Standard cinematographer placement library:**

- **Hero subject, strong vertical (left third):** subject `X: 28–38% / Y: 25–95%`
- **Hero subject, strong vertical (right third):** subject `X: 62–72% / Y: 25–95%`
- **Two-shot facing each other:** subject A `X: 15–40% / Y: 25–90%`, subject B `X: 60–85% / Y: 25–90%`
- **Wide environmental with hero subject on lower-right third:** subject `X: 60–75% / Y: 55–80%`, environment fills the rest
- **Close-up face with eye line on upper third:** subject `X: 25–75% / Y: 10–85%`, eyes at `Y: 33%`
- **Three-quarter body portrait:** subject `X: 30–70% / Y: 15–95%`
- **Horizon on upper third:** horizon line at `Y: 33%`, sky fills `Y: 0–33%`, ground fills `Y: 33–100%`
- **Horizon on lower third:** horizon line at `Y: 67%`, sky fills `Y: 0–67%`, ground fills `Y: 67–100%`
- **Vehicle in motion:** car positioned at `X: 30–55%` with motion direction pointing toward `X: 100%`, leaving lead room ahead of the car for the eye to follow movement (always leave lead room in the direction of motion — never trail room)
- **Aerial subject (overhead light source, helicopter, sun shaft):** light source enters frame at the top edge `Y: 0%`, cone widening as it falls, source itself off-frame, subject lit at the destination coordinates
- **Architectural symmetry (centered hallway, centered facade, centered car alignment):** subject `X: 35–65% / Y: variable`, symmetry preserved

**Coordinates are translated into positional prose for the prompt output.** Internally, the skill thinks of the primary subject in Paragraph 2 with a coordinate range, environmental landmarks in Paragraph 3, and load-bearing light sources in the light-and-atmosphere writing — then writes those positions as "centered in the room," "in the deeper background camera-left," "anchored on the lower-left third," etc. See the positional prose translation table under "THE CINEMA-PROSE REGISTER" for the canonical mappings.

---

### THE LOCKED TAG BLOCK (DEPRECATED FOR PROSE — KEPT AS FALLBACK)

**This six-phrase tag block is deprecated for the cinema-prose register.** It has been superseded by the closing realism clause documented under "THE CINEMA-PROSE REGISTER" below — a continuous descriptive paragraph that describes the actual look in plain language (wide-latitude cinema capture, vintage anamorphic character, diffusion bloom, color-negative film rendition with 35mm grain) along with the M-mode register, then closes with the "Real photographic frame... no CGI, no plastic, no AI" quality filter.

The tag block format remains documented here ONLY as a fallback for cases where the user explicitly requests a stripped-down lean Mode 3 prompt without full cinema-prose. Default behavior is the cinema-prose closing paragraph.

```
[Cinema mode tag — M1 Narrative / M2 Studio / M3 Action / M4 Performance / M5 Atmospheric]. Atmospheric volumetric haze. Real volumetric light physics. Gentle filmic highlight roll-off. Lifted blacks. Theatrical 35mm grain. Photographed not generated.
```

If the fallback tag block is used, it REPLACES the cinema stack at the end. Modes 0, 1, 2, 4, and 5 still append the full cinema stack. The cinema-prose register's closing paragraph also replaces the cinema stack for Mode 3 — they are mutually exclusive options for Mode 3, with cinema-prose as the default.

---

### THE CINEMA-PROSE REGISTER (LOCKED, NON-NEGOTIABLE)

**Mode 3 prompts are written like a DP describing a real frame, not like a spec sheet.** The 6-block spatial logic still applies — but it dissolves INTO the prose. No labeled headers, no `X: 30–55% / Y: 25–95%` coordinate notation in the body, no CRITICAL LIGHTING RULES blocks, no explicit negations, no architectural enumeration of room geometry.

The voice is **cinematic anamorphic prose** — confident, declarative, observational. The kind of language that appears in a treatment, a shot list narration, or a hero-still caption. Like a real photograph being described, not a frame being engineered.

**Why this register works:**
- The model responds to confident scene description, not coordinate grids
- References carry the heavy lifting on geometry, palette, and continuity — the prompt narrates the moment ON TOP of the reference
- Over-specification creates conflicting instructions; the model trusts plain language more than rule-blocks
- Spatial logic is preserved by writing positionally ("standing alone in the center of the room," "in the deeper background camera-left") instead of numerically

**What the register sounds like:**

> "A cinematic anamorphic still photograph captured handheld on a real cinema set — a Dutch-tilted intimate over-the-shoulder hero composition of a young Korean man standing alone in a dim converted private garage lounge at pre-dawn, the entire frame tilted at approximately 4 degrees Dutch angle camera-left low giving the composition a quietly off-kilter held-breath feel, the camera positioned right behind him at shoulder height in a waist-up framing showing his back, shoulders, and the back of his head filling the foreground with the wall-mounted television playing the live broadcast visible past his right shoulder in the mid-ground."

That opening sentence does the work of Blocks 1 and 2 in one continuous breath, with the camera position, the framing, the Dutch tilt, the subject placement, and the mood all woven together.

---

### THE FIVE-PARAGRAPH PROSE STRUCTURE (LOCKED)

Every Mode 3 prompt is composed as five paragraphs in this order. Paragraphs are not labeled in the output — they flow as continuous prose for the model.

**Paragraph 1 — Opening shot description.** One long sentence that establishes: the medium ("a cinematic anamorphic still photograph"), the framing register ("Dutch-tilted intimate hero composition"), the subject identification at high level ("a young Korean man standing in a dim converted private garage lounge at pre-dawn"), the camera position and angle in prose ("the camera positioned right behind him at shoulder height in a waist-up framing"), and the mood/intent ("quietly off-kilter held-breath feel"). This is the spine. Everything that follows hangs from this opening.

**Paragraph 2 — Character block.** Describes the character(s) in confident observational prose. Identity markers pulled from the attached reference written as visible facts in the frame ("dark layered mid-length tousled fringe falling across the back of his head, double small silver hoop earrings on each ear lobe catching faint warm spill, warm fair matte Korean skin"). Pose, attention, and held props woven in naturally ("a small black television remote held loosely in his right hand at his side... his head perfectly motionless, his eyes locked on the screen ahead of him").

**Paragraph 3 — World/environment block.** Describes the location as ambience and atmosphere, not architecture. The space's register — converted garage at pre-dawn, dawn cliffside, neon parking garage — matters more than counting structural elements. Anchor the world to the attached reference ("the converted garage lounge at pre-dawn carrying from the attached world reference"). Background subjects (a car silhouette in deep BG, a second character in the alcove) get positional language ("in the deeper background camera-left") not coordinates.

**Paragraph 4 — Subject anchor block.** Whatever the focal anchor of the shot is — the TV broadcast playing on the wall, the second car in BG, the dawn whisper on the horizon — gets its own paragraph. This is where any specific content (broadcast graphics, decals, signage, environmental detail) is described. If the shot has no focal anchor beyond the character, this paragraph folds into Paragraph 3.

**Paragraph 5 — Camera spec + finish.** Full cinema look in one continuous descriptive paragraph: capture register, lens character, diffusion/filtration look, film-stock rendition, grain register, grade, color cast, optical character (anamorphic oval bokeh, organic handheld breath, edge falloff, soft diffusion bloom if relevant) — all in plain-language look terms, never brand or model names — and the closing realism clause ("Real photographic frame captured on a real cinema camera, real anamorphic lens, real cotton tee, real human subject, real concrete and haze — no CGI, no rendered look, no digital cleanliness, no plastic surfaces, no AI smoothness, no skin smoothing, no glow, no halation bloom that reads as artificial, no glossy highlights").

The closing realism clause is mandatory. The list of "no X, no Y, no Z" at the very end is a load-bearing element — it tells the model what NOT to lean toward, and it does so AFTER all the positive description, where the model handles it as a quality filter rather than a conflicting instruction.

---

### KEY WRITING RULES FOR THE PROSE REGISTER

1. **No labeled blocks in output.** Never write "Block 1," "PARAGRAPH 2," "CRITICAL LIGHTING RULE," or any structural label in the prompt body. The structure is invisible — it lives in the writing order.

2. **No coordinate notation in the prompt body.** No `X: 38–62% / Y: 12–95%`. Replace with positional prose: "centered in the room," "in the deeper background camera-left," "filling the foreground," "anchored upper-left of the broadcast."

3. **No CRITICAL/IMPORTANT/MUST rules.** No "the cool wash MUST NOT catch the back wall." Replace with descriptive prose about what IS happening: "the cool broadcast wash catching only the immediate floor patch around his feet and a soft cool rim on his shoulders."

4. **No explicit negations as instructions.** Don't write "NO long sleeves, NOT factory tank-top construction." Write what IS there: "the sleeves cut off cleanly at the shoulder seam with raw unfinished armholes." The end-of-prompt realism clause is the ONLY place negations appear, and only as quality filters (no CGI, no plastic, no AI smoothness).

5. **References do the geometry work.** When the user attaches a world plate, write "carrying identically from the attached world reference" — don't re-enumerate the room geometry. The reference IS the geometry.

6. **References do the identity work.** When the user attaches a character reference sheet, write "carrying identically from the attached character reference" — don't re-describe every facial feature in the prompt. The reference IS the identity.

7. **The prompt narrates THE MOMENT.** What is the character doing right now? What is the camera doing right now? What is the light doing right now? That's the prompt's job. Continuity (room geometry, character identity, broadcast content) is reference work.

8. **The closing realism clause is non-negotiable.** Every Mode 3 prompt ends with the full cinema stack paragraph + the "Real photographic frame... no CGI, no plastic, no AI" close-out. This replaces the old locked tag block.

9. **The cinema mode register (M1/M2/M3/M4/M5) is invoked by DESCRIBING the actual look in plain language** in Paragraph 5 — not by writing "M1 Narrative" as a tag, and never by naming camera/lens/stock brands. Example: "Captured with a wide-latitude cinema look and a vintage 55mm-equivalent 2x anamorphic character at a wide aperture — oval bokeh, gentle horizontal squeeze, soft frame-edge falloff, a light diffusion bloom lifting highlights into a soft halation, color-negative daylight film rendition pushed slightly, with fine 35mm grain, in an M1 cinematic narrative register." The M-tag appears as a brief identifier at the end of the description, not as a standalone label.

10. **Do not write aspect ratios into the prompt** — the user sets aspect in the Higgsfield UI (typically 21:9 or 2.39:1 for cinematic plates).

---

### CANONICAL MODE 3 PROMPT — REFERENCE EXAMPLE

This is the locked register. Every future Mode 3 prompt is written in this voice — confident, observational, declarative, references doing the geometry and identity work, no labeled blocks, no coordinate notation in the body.

```
A cinematic anamorphic still photograph captured handheld on a real cinema set — a low-angle medium hero composition of a woman standing alone at the edge of an empty rooftop at dusk, the camera positioned slightly below her eye line in a waist-up framing anchored to the left third of the frame, the deepening dusk sky filling the upper two-thirds of the frame behind her, the city skyline reading in soft silhouette across the lower third of the background, the composition holding a quiet observational stillness.

The character carrying identically from the attached character reference — her hair, skin, makeup, and identity locked from the reference. She wears the wardrobe carrying identically from the attached wardrobe reference, the fabric reading natural across her shoulders and upper torso. Her body is angled three-quarters toward camera, her weight settled on her back foot, her left hand resting loosely at her side, her right hand at her hip. Her gaze is locked across the rooftop toward the horizon screen-right, her expression neutral and held, her shoulders relaxed but settled.

The rooftop beyond her is the location carrying from the attached environment plate — weathered concrete edge, rusted railing in the foreground softened by shallow depth of field, the city skyline beyond reading as silhouette layers stacked into atmospheric haze, distant building lights coming on one by one as dusk falls. Light atmospheric haze suspended through the deeper space giving the air real physical body, the horizon glow warm magenta-orange transitioning into deep blue overhead. Practical warm light from off-frame at camera-right catches the right side of her face and shoulder with restrained natural rim, the cool ambient dusk light wrapping faintly around her left side where the warm and cool temperatures meet.

The city skyline reads as the visual anchor of the deeper frame — building silhouettes layered front-to-back with progressive atmospheric desaturation, the warm horizon glow visible between the structures, scattered building lights warm and small in the deep distance, a faint aircraft beacon blinking once at the upper-right edge of the frame, the rest of the sky held in deep cool blue with the first stars just visible at the upper edge.

Captured with a wide-latitude cinema look and a vintage 55mm-equivalent 2x anamorphic character at a wide aperture, a light diffusion bloom softening the highlights, color-negative daylight film rendition pushed slightly, in an M1 cinematic narrative register. Real anamorphic optical character with oval bokeh on the deeper city elements, organic handheld operator breath, subtle frame-edge falloff, a faint horizontal streak flare on the brightest horizon highlight. Theatrical fine 35mm film grain across the entire frame — skin, fabric, concrete, sky, haze. Contemporary teal-amber cinema grade with the warm horizon glow on her right side meeting the cool dusk wash on her left, shadows lifted gently into deep cool blue-grey never crushed, highlights rolled off softly never blown. Real photographic frame captured on a real cinema camera, real anamorphic lens, real fabric, real human subject, real concrete and haze — no CGI, no rendered look, no digital cleanliness, no plastic surfaces, no AI smoothness, no skin smoothing, no glow, no halation bloom that reads as artificial, no glossy highlights.
```

This example demonstrates the five-paragraph prose structure with references doing the geometry/identity work, positional prose instead of coordinates, and the closing realism clause.

---

### THE OLD COORDINATE GRAMMAR (DEPRECATED)

The previous Mode 3 structure used labeled blocks, X/Y coordinate notation, CRITICAL LIGHTING RULES sections, explicit negations, and architectural room enumeration. **That grammar is deprecated for prose composition.** It made the model overcorrect and confuse spatial relationships.

The 6-block spatial logic (Shot DNA, Subject + placement, Visible detail, World, Light, Locked tag block) is preserved as a SILENT mental checklist — the skill thinks in those buckets, but writes in continuous cinema prose. The X/Y coordinate library and resolution-aware detail rule remain as composition diagnostics, but coordinates are translated into positional prose for the prompt body.

Positional prose translation table:

| Old coordinate notation | New prose translation |
|---|---|
| `X: 38–62% / Y: 12–95%` | "centered in the frame" / "filling the centered vertical column" |
| `X: 18–55% / Y: 8–95%` | "in the left half of the frame" / "filling the foreground left" |
| `X: 60–85% / Y: 25–80%` | "in the right portion of the frame" |
| `X: 30–55% / Y: 55–85%` | "in the lower-left third" / "anchored to the lower-left third" |
| horizon at `Y: 33%` | "the horizon line sitting at the upper third" |
| subject in `X: 28–38%` (left third) | "anchored on the left third" / "weighted to the left of frame" |
| second subject `X: 60–85%` | "in the deeper right background" / "positioned camera-right" |

---

## MODE 4 — GPT-2 DETAIL FACE SHOT (HIGGSFIELD GPT-2)

**When to use:** Only when the user explicitly asks for a chest-up portrait, face detail shot, or close-up where face/skin/eye fidelity matters most. Never suggested proactively for any other shot type.

**Gating behavior:**
- Wait for the user to ask for a detail/face/chest-up shot.
- Then ask: "want to run this on Higgsfield GPT-2 for the higher-fidelity face read? heads-up — GPT-2 uses more Higgsfield credits than Banana Pro." (Mention the credit cost only the first time per conversation. After that, just confirm "want this on GPT-2?")
- Wait for the green light. Then run the standard pre-prompt confirmation. Then deliver the prompt.

**Goal:** Maximum face fidelity. Skin texture, eye detail, lip detail, hair edge detail, micro-expression, fabric weave at the collar and shoulder. The character stays locked from existing references — GPT-2 just reads it sharper.

**Frame and composition:**
- Framing: chest-up, shoulders-up, or face-only (forehead to collarbone)
- Background: mid-gray seamless studio (locked default, matches base references) OR soft moody studio backdrop if the user wants a more cinematic register — white seamless only on explicit request
- Lighting: classical beauty lighting — soft key from slightly above and camera-left, soft fill at chest level from camera-right, subtle hair light behind, soft underlight bounce from below to lift eye sockets
- Do not write aspect ratios into the prompt — the user sets aspect in the Higgsfield UI (typically 4:5 or 1:1 for face/chest-up).

**Canonical Mode 4 (GPT-2) prompt structure:**

```
[Visual descriptor of the character — hair, makeup, wardrobe visible in frame from the chest up, jewelry visible at collar and ears, eye color and detail, lip detail, skin finish]. [Pose direction — head angle, shoulder angle, expression register].

[Background — mid-gray seamless studio (locked default) OR specified moody backdrop]. Classical beauty lighting — soft key from slightly above and camera-left at 35 degrees, soft fill at chest level from camera-right, subtle hair light behind defining the crown, soft underlight bounce lifting the eye sockets. [Framing — chest-up portrait / shoulders-up / face-only forehead-to-collarbone].

Extreme face fidelity. Real skin texture with visible pores, fine peach fuzz catching light along the jawline and upper lip, subtle subsurface scattering on the nose bridge cheeks and ears, micro-expression detail in the eyes and mouth corners, individual lash detail, real moisture and reflection in the iris with visible iris pattern, real lip texture with subtle natural lip lines, hair rendered strand by strand at the hairline with visible baby hairs and flyaways, fabric weave visible at the collar and shoulder.

[The cinema stack].
```

**Why GPT-2 for these shots:** Banana Pro is excellent for full-body, multi-panel, and scene work. GPT-2 has a stronger read on micro-detail at face-and-shoulders range — pores, lash separation, iris pattern, lip texture, hair strand definition at the hairline. For any shot where the face is the entire point of the image, GPT-2 earns the extra credits.

---

## MODE 5 — OUTFIT REPLACEMENT (BANANA PRO TWO-REFERENCE SWAP)

**When to use:** When the user wants to take an outfit and pose from one image and apply it to a different character. The outfit reference image has the wardrobe, styling, footwear, accessories, and body pose locked in. The character reference image has the face, bone structure, body type, skin tone, and hair locked in. The output combines them — the character from the second image now wears the outfit and holds the pose from the first image.

Trigger phrases include: "outfit replacement," "outfit swap," "put [character] in this outfit," "swap the face," "put this character in that fit," "replace the model with [character] wearing [outfit]," or any request that involves combining a wardrobe/pose reference with a separate character reference.

**Goal:** Maximum identity transfer of the character (from @image2) onto the outfit and pose (from @image1) with zero alteration to either side — the outfit stays exactly as shown, the character's identity stays exactly as shown, only the body underneath the outfit changes to match the new character.

**Reference attachment order (CRITICAL):**
- **@image1 = outfit reference** — the image containing the outfit, styling, footwear, accessories, and pose to keep
- **@image2 = character reference** — the image containing the face, bone structure, body type, skin tone, and hair to apply

This order is fixed. Do not swap. The prompt is written around this exact mapping and reversing it will break the swap.

**Pre-prompt confirmation rule applies.** Even though the prompt itself is short and locked, the user should confirm:
- Which reference is the outfit/pose source
- Which reference is the character/identity source
- That both references are uploaded and visible in chat

Use the standard pre-prompt check format — references first, then the two roles, then run.

**Canonical Mode 5 prompt (LOCKED — do not modify):**

```
Replace the character in @image1 with the character in @image2. Keep the outfit and pose from @image1 exactly. Match the face, bone structure, body type, skin tone, and hair from @image2. Clean mid-gray seamless studio background, even neutral mid-gray with no seam line, soft large-source studio lighting, skin and outfit rendering at their true natural tone against the neutral gray, natural film grain, full body framing.
```

**Why this prompt is locked:** Mode 5 does not use the cinema stack. The two reference images carry the photographic register on their own — adding texture stack language on top of a swap operation creates conflicting instructions and degrades the identity transfer. The lean prompt structure is the entire point of this mode. Trust the references.

**Background and lighting language is also locked.** The locked prompt outputs to a clean mid-gray seamless studio with soft large-source lighting — this is the canonical neutral output for character/outfit reference assets (white seamless only if the user explicitly asks for a white card). If the user wants the swap output dropped into a different environment, that becomes a Mode 3 scene plate built on top of the Mode 5 output (run Mode 5 first to produce the locked base, then Mode 3 to place it in the scene).

**Per-character or per-IP modifiers:** None. Mode 5 is character-and-IP-agnostic. The prompt does not name characters, does not specify nationality, does not adjust language per group or project. The two reference images carry all of the identity load. The skill ships the locked prompt unchanged regardless of what the character or outfit is.

**What Mode 5 is NOT for:**
- Building a new outfit from scratch on a locked character → use Mode 1A (Banana Pro full styling) or Mode 1B (Soul Cinema two-step)
- Generating multiple angles of a locked character in a locked outfit → use Mode 2 (6-panel character sheet)
- Placing a character in a cinematic environment → use Mode 3A
- Detail face shots → use Mode 4 (GPT-2)

Mode 5 is the single-purpose tool for: *here is an outfit on a model I don't care about, and here is the character I do care about, give me the character in that outfit.*

---

## UNIVERSAL PROMPT RULES (ALL MODES)

These apply to every prompt this skill produces, no exceptions:

1. **No character names in prompt output.** Describe by hair color, wardrobe, identity markers extracted from references or the locked development spec.
2. **No real brand names in prompt output.** Generic visual descriptors only.
3. **No `@image` tags or `<<<image_n>>>` placeholders.** Image attachment happens in the Higgsfield UI directly. The prompt is text-only.
4. **No internal production context.** No "carried through the world," no "matching the previous scene." Every prompt is standalone and self-contained.
5. **Pure visual description only.** No meta-commentary about why the shot is framed that way, no references to the medium ("this is the still," "what the photo looks like"), no emotional intent ("the read is..."). Every word describes a visible thing in the frame.
6. **No teeth-showing smiles** unless the user explicitly requests one. Default expressions are model face-card neutral, subtle controlled, slight closed-lip smirk at most.
7. **No negative prompts.** This skill does not output negative prompt blocks. Higgsfield workflow doesn't use them.
8. **Cinema stack baked in for Modes 0, 1, 2, 4, 5.** The cinema stack closes every Mode 0, 1, 2, 4, and 5 prompt (with Step 1B.1 outfit reference using the lighter close documented in that section, and Mode 5 using its own locked lean prompt). Mode 3 is the exception — see rule 9.
9. **Mode 3 uses the cinema-prose closing paragraph in place of the cinema stack AND locked tag block.** Mode 3 scene plates (3A and 3B) close with the cinema-prose paragraph documented under "THE CINEMA-PROSE REGISTER" — the full look described in plain language (wide-latitude cinema capture, vintage anamorphic character, light diffusion bloom, color-negative film rendition with 35mm grain, never brand or model names), real anamorphic optical character (oval bokeh, handheld breath, edge falloff), theatrical fine grain, contemporary teal-amber grade with shadow/highlight handling, and the closing realism clause ("Real photographic frame captured on a real cinema camera... no CGI, no plastic, no AI smoothness, no skin smoothing"). This closing paragraph replaces the cinema stack AND the old locked tag block for Mode 3. The old tag block remains documented as a deprecated fallback only.
10. **Single fenced code block on output.** Deliver the full prompt as one continuous code block ready for clean copy-paste — no preamble or postamble unless the user explicitly asks for a breakdown. (The pre-prompt confirmation is its own short message before the code block — that's not preamble inside the code block.)
11. **Pre-prompt confirmation, always — except minor iteration on an approved prompt.** Every full prompt is preceded by a bulleted "here's what I'm about to prompt, sound good?" check. **References listed first**, then character, outfit, backdrop/environment, framing. Wait for the green light. Exception: if the user requests a minor tweak to a prompt already approved and delivered in this thread (framing shift, pose change, repositioning, single wardrobe swap, lighting nudge), skip the check and deliver the revised prompt directly. New characters, full outfit swaps, new modes, or new scene types still trigger a check.
12. **No aspect ratios in prompt output.** Never write "3:4 vertical aspect ratio," "16:9 horizontal," "21:9 cinematic," "4:5 portrait," "2.39:1," or any other ratio spec inside the prompt body. The user sets aspect ratio in the Higgsfield UI directly. The prompt describes framing in plain language only ("full body," "chest-up portrait," "wide establishing shot," "medium two-shot") — never with a numerical ratio.

---

## INVENTORY EXTRACTION CHECKLIST (run silently before composing)

Before writing the final prompt, silently catalog:

- [ ] Mode selected (0 face lock / 1 single-image outfit / 2 six-panel / 3A character scene / 3B environment plate / 4 GPT-2 / 5 outfit replacement) and rationale
- [ ] Every uploaded reference image identified and listed by short visual descriptor (this becomes the first bullet of the pre-prompt check)
- [ ] If Mode 0: text spec for the new character is locked and approved, tool fork has been presented (Banana Pro / GPT-2 / Soul Cinema), user has picked, and the locked baseline wardrobe (plain black camisole for women, plain black ribbed tank for men) is included in the prompt. If Soul Cinema picked, running Step 0.1 (Soul Cinema face plate) before Step 0.2 (Banana Pro 3:4 headshot).
- [ ] If Mode 1: a Mode 0 face lock exists for the character (if new), OR a locked character reference exists (if existing)
- [ ] If Mode 2: a Mode 1 base outfit reference exists and is approved (if not, stop and build the base first)
- [ ] If Mode 4: user explicitly asked for face/chest-up and confirmed GPT-2
- [ ] If Mode 5: two reference images uploaded — outfit reference (becomes @image1) and character reference (becomes @image2), order confirmed with the user
- [ ] Every character described by visual markers only (hair, makeup, wardrobe, jewelry, body markers, pose, expression)
- [ ] If Mode 3: environment described as ambience (not architectural enumeration) — world plate reference carries geometry
- [ ] If Mode 3: matching cinema mode identified (M1/M2/M3/M4/M5) and woven into Paragraph 5 camera spec
- [ ] If Mode 3: subject placed in frame with positional prose (not X/Y coordinate notation) — rule-of-thirds anchored, not dead-center unless explicitly motivated
- [ ] If Mode 3: resolution-aware detail check passed — every visible detail is something the camera at this distance, lens, motion, and lighting can physically resolve; anything the camera couldn't see is dropped
- [ ] If Mode 3: prompt follows the FIVE-PARAGRAPH PROSE STRUCTURE (Opening shot / Character / World / Subject anchor / Camera spec + finish) — no labeled blocks in output
- [ ] If Mode 3: closing realism clause is in place (full camera package + M-mode + "Real photographic frame... no CGI, no plastic, no AI" quality filter)
- [ ] Pose, body angle, expression register chosen
- [ ] No names, no brands, no internal context, no meta-commentary
- [ ] Cinema stack will close the prompt (for Modes 0, 1A, 2, 4; with Mode 1B Step 1 using lighter close; Mode 5 using its locked lean prompt; Mode 3 using the cinema-prose closing paragraph)
- [ ] Pre-prompt confirmation delivered and confirmed — references listed FIRST in the bullet list

If anything needed for composition is missing from the user input, ask before writing.

---

## WHEN THE USER ASKS FOR A PROMPT

The flow is always: **confirm character → confirm what's about to be prompted → deliver the prompt in a fenced code block**.

The user pastes the code block straight into Higgsfield. Tool routing: Banana Pro / Nano Banana for Mode 0 Step 0.A (single-pass default), Mode 0 Step 0.2 (Soul Cinema path lock), Modes 1A, 2, 3, 5; GPT-2 for Mode 0 Step 0.B (highest fidelity single-pass) and Mode 4; Soul Cinema for Mode 0 Step 0.1 (iteration path) and Mode 1B. The user attaches the same reference images (or selects them from their Higgsfield character/environment library) inside the Higgsfield UI. The skill's job ends at the code block.

If the user requests multiple shots in one ask, deliver each in its own code block, sequentially numbered or labeled — but still run the pre-prompt confirmation once before delivering the batch.
