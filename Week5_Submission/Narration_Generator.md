---
name: narrated-math-lecture-video
description: Create a narrated math lecture video from a Marp Markdown slide deck using Remotion, one generated MP3 narration file per slide, and local audio/video stitching. Use when the user provides or references a Marp deck and asks for a lecture video, narrated slide video, Remotion render, edge-tts narration, or synchronized math slides with voiceover.
---

# Narrated Math Lecture Video

Use this skill to turn a Marp Markdown deck into a Remotion math lecture video with per-slide lecture audio. The expected output is a runnable project that parses the deck, creates a lecturer-style script for each slide, generates one MP3 per slide, syncs slide durations to the MP3 lengths, and renders a final MP4 locally.

## Core Workflow

1. Inspect the workspace.
   - Find the Marp deck, usually a `.md` file with frontmatter containing `marp: true`.
   - Check whether a Remotion/React project already exists. If not, scaffold a minimal one.
   - Prefer existing project conventions when present.

2. Parse the Marp deck.
   - Strip the frontmatter.
   - Split slides on Marp separators: lines containing `---`.
   - Preserve each slide's Markdown for visual rendering.
   - Produce a lecturer-style narration script for each slide, not a plain reading of the slide.
   - Use stripped slide text only as a fallback seed; enrich it with explanation, transitions, intuition, and spoken equation interpretation.

3. Build the Remotion composition.
   - Use one `Sequence` per slide.
   - Render slide Markdown with math support, for example `react-markdown`, `remark-math`, `rehype-katex`, and KaTeX CSS.
   - Add one `Audio` component per slide when its local MP3 exists.
   - Drive `durationInFrames` from generated slide metadata.

4. Generate narration.
   - Create one MP3 per slide, e.g. `public/narration/slide-01.mp3`.
   - Speak from the enriched script for each slide.
   - Write narration metadata, e.g. `public/generated/narration.json`, with `{id, file, durationSeconds}` per slide.
   - Rebuild slide timing metadata after narration so visuals match actual audio durations.

5. Render locally.
   - Install project npm dependencies before rendering so `node_modules/.bin/remotion` exists.
   - Use `npm run render` or `npm run render:with-narration` to stitch visuals and local MP3 files into the final MP4.
   - Store generated output in `out/`.

## Important TTS Note

`edge-tts` creates local MP3 files, but it is not offline TTS. It sends the narration text to Microsoft Edge TTS services to synthesize the speech. Tell the user this clearly before running networked narration generation if workspace content may be private.

After MP3 files exist, duration measurement and Remotion rendering should be local.

## Recommended Project Shape

Use this shape when scaffolding from scratch:

```text
.
|-- package.json
|-- remotion.config.ts
|-- tsconfig.json
|-- Lecture_Slides.md or deck.md
|-- scripts/
|   |-- build-slides.mjs
|   |-- generate-narration.mjs
|   `-- setup-tts.mjs
|-- src/
|   |-- index.ts
|   |-- Root.tsx
|   `-- lecture/
|       |-- FdmLecture.tsx
|       |-- SlideScene.tsx
|       |-- style.css
|       `-- types.ts
|-- public/
|   |-- generated/
|   |   |-- slides.json
|   |   `-- narration.json
|   `-- narration/
|       |-- slide-01.mp3
|       `-- slide-02.mp3
`-- out/
    `-- lecture.mp4
```

Generated directories such as `out`, `public/generated`, `public/narration`, `node_modules`, and `.venv` should usually be gitignored.

## Package Scripts

Provide scripts like these:

```json
{
  "scripts": {
    "build:slides": "node scripts/build-slides.mjs",
    "setup:tts": "node scripts/setup-tts.mjs",
    "narration": "node scripts/generate-narration.mjs",
    "studio": "npm run build:slides && remotion studio src/index.ts",
    "render": "npm run build:slides && remotion render src/index.ts FdmLecture out/lecture.mp4",
    "render:with-narration": "npm run build:slides && npm run narration && remotion render src/index.ts FdmLecture out/lecture.mp4",
    "typecheck": "tsc --noEmit"
  }
}
```

Do not assume the Remotion CLI is globally installed. In npm scripts, `remotion` resolves from `node_modules/.bin/remotion`, which only exists after `npm install`. When scaffolding a new project, either run `npm install` with approval if network access is needed, or clearly tell the user to run it before `npm run render`.

Recommended dependencies:

```text
remotion
@remotion/cli
@remotion/renderer
react
react-dom
typescript
react-markdown
remark-gfm
remark-math
rehype-katex
katex
```

## Dependency Setup

For a fresh project, include setup instructions in the package README:

```bash
cd video
npm install
npm run build:slides
npm run render
```

If generating narration with `edge-tts`, also include:

```bash
npm run setup:tts
npm run render:with-narration
```

`setup-tts.mjs` should create `.venv`, install `edge-tts`, and leave the project-local binary discoverable at `.venv/bin/edge-tts`. Request approval before running this setup when it needs to download packages.

## Slide Metadata

`build-slides.mjs` should write `public/generated/slides.json`:

```json
{
  "fps": 30,
  "slides": [
    {
      "id": "slide-01",
      "number": 1,
      "title": "Finite Difference Method",
      "markdown": "# Finite Difference Method",
      "narration": "In this slide, we are setting up the main idea. A finite difference method replaces a continuous derivative with a nearby algebraic approximation, so a differential equation becomes something a computer can step through. Keep an eye on what information is local and what information comes from neighboring grid points.",
      "audioSrc": "/narration/slide-01.mp3",
      "durationSeconds": 8,
      "durationFrames": 240
    }
  ]
}
```

If narration metadata exists, use the real audio duration plus a small padding, such as `0.5` to `1.0` seconds. If audio does not exist yet, estimate duration from word count.

## Lecture-Style Narration

Narration should sound like an instructor teaching from the slide, not like text-to-speech reading bullets.

For each slide:

- Write a compact teaching script, usually 45-90 seconds for content slides and 20-45 seconds for title, outline, or recap slides.
- Start from the slide's visible content, then add relevant context: motivation, intuition, transitions, examples, warnings, or common student confusions.
- Explain equations verbally in meaning-first language. Do not just read symbols; say what the terms represent and why the formula matters.
- Connect to the previous slide and prepare the next slide when helpful.
- Keep the script faithful to the slide and lecture plan; do not introduce a separate mini-lecture that the slide does not support.
- Avoid phrases like "this slide says" unless useful. Prefer natural lecture language: "The key move here is..." or "Notice what changes..."
- Store the full teaching script in each slide's `narration` field. Keep `markdown` as the visual slide source.

Implementation pattern:

- If the deck is being generated in the same task, have Codex write lecturer scripts while creating slide metadata.
- If a script must be generated programmatically, allow a `scripts/narration-overrides.mjs` or JSON map keyed by slide id, and fall back to cleaned Markdown only for slides without an authored script.
- Never overwrite an existing authored narration script with auto-cleaned slide text unless the user asks to regenerate narration.

## Narration Script Requirements

`generate-narration.mjs` should:

- Find `edge-tts` from `.venv/bin/edge-tts`, `.venv/bin/python -m edge_tts`, `edge-tts`, or `python3 -m edge_tts`.
- Generate missing or zero-byte MP3s.
- Keep existing non-empty MP3s to avoid repeating paid/remote/service calls.
- Use environment variables such as `EDGE_TTS_VOICE` and `EDGE_TTS_RATE`.
- Measure durations locally with `ffprobe`, not `@remotion/media-utils#getAudioDurationInSeconds`.

Use `ffprobe` from Node:

```js
const result = spawnSync(
  'ffprobe',
  [
    '-v',
    'error',
    '-show_entries',
    'format=duration',
    '-of',
    'default=noprint_wrappers=1:nokey=1',
    filePath
  ],
  {encoding: 'utf8'}
);
```

Do not use `getAudioDurationInSeconds()` in a Node script; it is browser-only and can fail with an error like "getAudioDuration() is only available in the browser."

## Remotion Composition Pattern

Use a root composition that imports generated slide JSON:

```tsx
const totalFrames = slideData.slides.reduce(
  (sum, slide) => sum + slide.durationFrames,
  0
);
```

Render each slide as a sequence:

```tsx
let cursor = 0;

return (
  <AbsoluteFill>
    {slides.map((slide) => {
      const from = cursor;
      cursor += slide.durationFrames;

      return (
        <Sequence key={slide.id} from={from} durationInFrames={slide.durationFrames}>
          <SlideScene slide={slide} totalSlides={slides.length} />
          {slide.audioSrc ? <Audio src={staticFile(slide.audioSrc)} /> : null}
        </Sequence>
      );
    })}
  </AbsoluteFill>
);
```

## Visual Guidance

For math lectures:

- Use clean, high-contrast layouts and large readable math.
- Render equations with KaTeX.
- Include subtle slide progress and slide numbers.
- Avoid decorative clutter that competes with formulas.
- Ensure dense slides still fit at 1920x1080. If needed, reduce font sizes for slides with many equations or list items.

## Validation

Run these checks where applicable:

```bash
npm install
test -x node_modules/.bin/remotion
npm run build:slides
npm run typecheck
node --check scripts/generate-narration.mjs
npm run render
```

Also inspect `public/generated/slides.json` and confirm representative `narration` fields contain instructor-style commentary rather than only stripped slide text.

For narrated output:

```bash
npm run render:with-narration
```

If networked TTS is blocked or not approved, still verify the visual-only render with estimated timings and explain that real MP3 generation requires the user's approval to send narration text to the TTS provider.

## Common Failure Modes

- **`sh: 1: remotion: not found`:** npm dependencies were not installed in the video project. Run `npm install`, then confirm `node_modules/.bin/remotion` exists before rendering.
- **Only one MP3 exists:** narration generation likely crashed after the first slide. Fix the error and rerun; the script should keep existing MP3s and continue.
- **Zero-byte MP3:** treat it as missing and regenerate it.
- **`edge-tts was not found`:** provide or run a `setup:tts` script that creates `.venv` and installs `edge-tts`, then rerun narration.
- **Browser-only duration error:** replace Remotion media-utils duration calls in Node scripts with `ffprobe`.
- **Remotion Chrome download fails:** rerun with network approval if allowed.
- **Narration sounds like slide reading:** replace auto-cleaned narration with authored lecture scripts that explain why each slide matters, how formulas should be interpreted, and how the current slide connects to the lecture arc.
- **Math speech sounds awkward:** improve the LaTeX-to-speech cleanup for common course notation before regenerating MP3s.
