---
name: lecture-production-suite
description: "Coordinate lecture-to-marp-slides, narrated-math-lecture-video, and math-teaching-widget to produce a complete math lecture package from a lecture plan file and widget idea: Marp slide deck, narrated slide video, and standalone interactive teaching widget."
---

# Lecture Production Suite

Use this coordinator skill when the user provides a lecture plan file plus a widget idea and wants a complete teaching package: a polished Marp slide deck, a narrated reading/video of that deck, and an interactive math teaching widget.

This skill coordinates three component skills in sequence:

- `$lecture-to-marp-slides` for the Marp deck.
- `$narrated-math-lecture-video` for narration, timing metadata, and video rendering.
- `$math-teaching-widget` for the standalone browser widget.

## Required Inputs

The ideal user request includes:

- a lecture plan file path, usually Markdown
- a widget idea, or at least a topic for a widget

If the lecture plan file is missing, ask for it. If the widget idea is missing but the topic is obvious from the lecture plan, choose a conservative widget idea that supports the central lecture concept and state that choice before building. If neither the topic nor the widget idea is clear, ask one concise question.

## Output Contract

Produce or update a project folder containing:

```text
lecture-package/
|-- slides/
|   `-- lecture-slides.md
|-- video/
|   |-- package.json
|   |-- remotion.config.ts
|   |-- scripts/
|   |-- src/
|   |-- public/
|   `-- out/
|-- widget/
|   `-- index.html
`-- README.md
```

Adapt names to the lecture topic when useful, but keep the three artifact areas clear: `slides`, `video`, and `widget`.

## Coordination Workflow

1. Inspect the lecture plan.
   - Read the user-provided file.
   - Identify audience, goals, prerequisites, core definitions, examples, formulas, and exercises.
   - Extract the central mathematical model or concept that should connect the slides and widget.

2. Create the slide deck with `$lecture-to-marp-slides`.
   - Read the `lecture-to-marp-slides/SKILL.md` instructions before drafting.
   - Use the lecture plan as the source of truth.
   - Write a complete Marp deck under `lecture-package/slides/`.
   - Keep slide math and notation consistent with any widget labels or equations.

3. Build the narration/video project with `$narrated-math-lecture-video`.
   - Read `narrated-math-lecture-video/SKILL.md` before implementation.
   - Use the generated Marp deck as input.
   - Create or update a Remotion project under `lecture-package/video/`.
   - Generate slide metadata locally.
   - Before running networked TTS, tell the user that `edge-tts` sends narration text to Microsoft Edge TTS services. If approval is unavailable or network access is blocked, leave the project ready to run and verify the visual/local checks.

4. Build the interactive widget with `$math-teaching-widget`.
   - Read `math-teaching-widget/SKILL.md` before implementation.
   - Use the user's widget idea when supplied.
   - If the idea is broad, refine it into a concrete direct-manipulation widget tied to the lecture's main concept.
   - Write a self-contained `lecture-package/widget/index.html` unless the user requests a framework.
   - Use notation and parameter names that match the deck.

5. Add integration notes.
   - Create `lecture-package/README.md`.
   - Include paths to the slide deck, widget, and video project.
   - Include commands for local validation and rendering.
   - Include any limitations, especially if narration MP3s or final MP4 were not generated because networked TTS, browser download, or dependency installation was not approved.

## Artifact Handoff Rules

- The Marp deck is the source for narration and should be created before the video project.
- The widget should reinforce the same notation and examples used in the deck.
- Do not silently change the lecture topic to fit a favorite widget pattern.
- If the widget reveals a better notation or example, update the slides for consistency.
- Keep generated output organized so users can use each artifact independently.

## Implementation Guidance

- Prefer project-local folders and scripts; avoid global installs.
- Preserve existing project conventions if a lecture package already exists.
- Keep all generated lecture assets inside the package folder unless the user asks for a different layout.
- Use ASCII filenames and directory names.
- Avoid external assets for the widget unless explicitly requested.
- Use focused validation rather than broad rewrites.

## Validation Checklist

Before finishing, verify as much as the environment allows:

- The Marp deck has valid frontmatter with `marp: true`.
- Slides are separated by `---`.
- The video project can parse/build slide metadata.
- Narration generation script parses with Node.
- TypeScript checks pass when dependencies are installed.
- The widget HTML is self-contained.
- Embedded widget JavaScript parses.
- README commands match the actual package layout.

If a step cannot be completed, leave the artifact runnable and explain the exact missing dependency or approval.

## Final Response

Report:

- slide deck path
- narrated video project path and final MP4 path if rendered
- widget path
- validation commands run and their results
- any required follow-up such as approving networked TTS or running dependency installation
