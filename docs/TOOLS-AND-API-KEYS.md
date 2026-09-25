# Tools, accounts, and API keys

Nate uses **ElevenLabs Scribe for transcription** and **Kie.ai for generated video
and image assets**. These are his preferred services, not requirements for every
edit. Bring your own accounts and credits, and configure only what you use.

## What you need

| Tool or service | When you need it | Setup and cost |
| --- | --- | --- |
| Codex or Claude Code | Following the agent-guided editing skills | Your own assistant access. External service API credits are separate. |
| Node.js 22+, npm, Git, FFmpeg with ffprobe, and Chrome/Chromium | Local editing, preview, and rendering | Install on your computer. See [setup](SETUP.md). |
| HyperFrames and GSAP | Video compositions and animation | Installed by `npm ci`. Rendering runs locally. Some templates use online fonts or CDNs; localize selected assets for final rendering. |
| ElevenLabs Scribe | Nate's default for speech transcription | Your own key with `speech_to_text` access and available usage. The included helper sends audio to ElevenLabs. |
| OpenAI Whisper API | Alternative cloud transcription | Your own OpenAI API key and API billing. Ask the assistant to configure the call and normalize its word timestamps. |
| Local Whisper or whisper.cpp | Alternative transcription on your computer | Separate runtime and model installation. No cloud transcription key; needs model downloads, disk space, and local compute. |
| Kie.ai | Optional generated moving B-roll, images, and other supported assets | Your own account, key, and credits. Existing footage and supplied assets can be used instead. |
| Your footage, logos, fonts, music, and sound effects | Building the actual edit | Supply assets you can use. The kit does not include a stock-media or music subscription. |

The synthetic starter and checks need no paid transcription or generation API.
Choose a provider only when the next stage needs it.

## ElevenLabs: the included helper

Create a key in [ElevenLabs API settings](https://elevenlabs.io/app/settings/api-keys)
and put it in the root `.env` as `ELEVENLABS_API_KEY`. Then run:

```sh
node scripts/transcribe-elevenlabs.mjs video-projects/my-video/assets/raw.mp4
```

The helper writes word-level JSON beside the input. Reuse a verified transcript
instead of paying to transcribe the same take again. See the official
[Scribe API documentation](https://elevenlabs.io/docs/api-reference/speech-to-text/convert)
for current model options and usage details.

## Whisper and other transcription alternatives

You can prompt the assistant to use another provider. The bundled
`transcribe-elevenlabs.mjs` script itself only calls ElevenLabs; changing the key
does not switch its provider.

For the OpenAI API, use `whisper-1`, `response_format="verbose_json"`, and
`timestamp_granularities=["word"]`. Store `OPENAI_API_KEY` locally. Check current
upload limits before sending long recordings; split audio when needed and retain
chunk offsets. See [OpenAI's guide](https://developers.openai.com/api/docs/guides/speech-to-text).

For local transcription, ask the assistant to configure
[OpenAI Whisper](https://github.com/openai/whisper) or
[whisper.cpp](https://github.com/ggml-org/whisper.cpp). Python Whisper requires
Python and model dependencies; whisper.cpp has its own installation. Neither is
installed by `npm ci`.

The cutting tools require this common format, with **word-level times in seconds**
on the exact source recording's timeline:

```json
{
  "text": "Hello world.",
  "audio_duration_secs": 2.0,
  "words": [
    { "text": "Hello", "start": 0.2, "end": 0.6 },
    { "text": "world.", "start": 0.7, "end": 1.2 }
  ]
}
```

Ask the assistant to map a provider's `word` field to `text` when necessary,
preserve numeric start/end times, and get full source duration from ffprobe.
Paragraphs, SRT subtitles, and segment-only transcripts do not supply the required
word timing. Request word timestamps or perform alignment; do not invent timing.
Later edits must retime words using their EDL. Short-form plans additionally track
`sourceStart` and `sourceEnd`.

Copy either prompt:

> Use OpenAI Whisper instead of ElevenLabs for this recording. Use my locally
> configured API key, request word timestamps, and normalize the result for this
> kit before cutting. Preserve the source and verify timing against its audio.

> Use local Whisper for transcription. Check its installation and model downloads
> first, then normalize the word timestamps for this kit. Keep transcription local
> and use my supplied footage and assets without paid generation.

## Kie.ai: generated video and assets

Nate uses [Kie.ai](https://kie.ai/) for generated video and image assets. Set
`KIE_API_KEY` in `.env` if you choose it. Follow the
[official API guide](https://docs.kie.ai/) for keys, model-specific requests,
task status, and credits.

The short-form skill describes a Kie workflow; the kit does **not** bundle a
universal Kie generation script or connected account. The `motion-showreel` skill
includes a small client (`scripts/kie.mjs`) for its three showreel assets: Suno
instrumental music, Seedream stills from a logo reference, and Kling camera moves.
Ask the assistant to configure your selected model using current documentation. Adding a key alone does not
create an integration. Model inputs, formats, availability, and credit costs vary.

Prepare the proposed assets and expected cost before paid work that you have not
already authorized. Keep task IDs, reuse successful outputs, and save chosen
results inside your private project's assets. Inspect their motion, duration,
aspect ratio, and framing in the final edit.

> Use Kie.ai for moving B-roll in the approved scenes. Check my local configuration
> and current model documentation, then show me the assets you propose and expected
> credit cost. Reuse existing footage wherever it fits.

## Other optional tools referenced by bundled skills

These are workflow options, not a claim that every example used them:

- **Narration:** HyperFrames guides describe local Kokoro TTS with extra runtime
  and model setup. ElevenLabs and HeyGen TTS are also mentioned; each needs your
  service access and a configured API or connector.
- **Website capture:** Gemini can optionally provide richer image descriptions.
  Basic capture does not require that key.
- **Other transcription:** the framework reference mentions Groq Whisper. It
  needs its own key and the same transcript normalization checks.
- **Older integration examples:** ClickUp or OpenAI access is needed only when
  your selected project actually calls those services.
- **Sound effects:** `motion-showreel` can generate an SFX kit with ElevenLabs
  sound generation (`scripts/sfx.mjs`). It uses `ELEVENLABS_API_KEY`; the key needs
  sound-effects access as well as `speech_to_text`. Your own SFX library works too.
- **Helper runtimes:** some optional scripts require Python. Playwright is
  included for relevant browser workflows; browser binaries may need installation.

A skill's mention of an MCP tool does not install that integration. Ask the
assistant to check which connectors or API clients are available first.

## Configure only what you use

`npm run setup` creates `.env` from [`.env.example`](../.env.example) if absent.
Leave unused entries blank. Existing `.env` files are preserved, so add newly
needed entries yourself. The ElevenLabs helper loads the root `.env`; other
providers need their own client or environment loading configured by the assistant.
Keep credentials out of compositions, screenshots, and commits.

Check current provider pricing and your balance before paid calls. The student
kit does not include transcription, generation, voiceover, or assistant credits.
