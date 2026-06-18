---
name: lecture-to-marp-slides
description: Convert lecture idea Markdown files, topic outlines, rough teaching notes, or syllabus-style bullet lists into polished Marp Markdown slide decks for math, science, and technical lectures. Use when the user asks to generate, expand, revise, or format a lecture slide deck from a Markdown outline, especially when the output should be Marp-compatible with equations, examples, learning flow, exercises, and speaker-friendly slide pacing.
---

# Lecture To Marp Slides

## Overview

Turn a rough lecture idea file into a coherent Marp deck using Katex. Preserve the instructor's topic choices while adding the missing teaching structure: motivation, notation, definitions, worked formulas, algorithmic steps, examples, caveats, and short exercises.

## Workflow

1. Inspect the input lecture outline and identify:
   - target audience and prerequisite level
   - core concepts to cover
   - examples, equations, applications, and exercises already requested
   - spelling or terminology fixes needed in visible slide text
   - topics that need connective tissue for a teachable sequence

2. Choose a slide arc:
   - title and subtitle
   - lecture outline
   - motivation and applications
   - notation or setup before formulas
   - basic ideas before complicated examples
   - worked examples that turn bullets into concrete mathematics
   - problem classes or algorithms
   - limitations and practical tips
   - short exercises or discussion prompts

3. Draft the deck as a `.md` file with Marp frontmatter:

```markdown
---
marp: true
theme: default
paginate: true
class: lead
---
```

Use `---` between slides. Use `#` for the title slide and `##` for regular slide titles.

4. Expand sparse bullets into lecture-ready slides:
   - introduce notation before using it
   - define variables in equations
   - add one concrete example for each abstract method
   - split dense derivations across multiple slides
   - convert "cover X" bullets into "what X is, why it matters, how to compute/use it"
   - distinguish linear, nonlinear, elliptic, parabolic, hyperbolic, boundary-value, or initial-value cases when relevant

5. Validate the deck manually before finishing:
   - every slide is separated by `---`
   - LaTeX math delimiters are balanced
   - no slide is overloaded with too much prose
   - terminology is corrected without changing intended meaning
   - outline slide matches the produced deck
   - formulas use consistent symbols across slides
   - title, examples, and exercises match the requested audience level

## Math And Technical Lecture Heuristics

For undergraduate math and computational lectures:

- Start from intuition, then notation, then formulas.
- Prefer small canonical models before general operators.
- Show how continuous equations become algebraic systems or algorithms.
- Include boundary or initial conditions when presenting differential equations.
- Name stability or accuracy conditions when time-stepping or approximation methods appear.
- Use exercises that are directly actionable from the lecture, not broad essay prompts.

When the input contains a raw term such as `sin(x) y'` or `e^x y''`, turn it into a node-level discretization or worked formula rather than leaving it as a topic bullet.

## Slide Density

Aim for one teaching move per slide:

- concept introduction
- notation setup
- formula or stencil
- worked algebraic rearrangement
- algorithm comparison
- application example
- drawback or practical tip

If a slide has more than one large displayed equation plus several bullets, split it.

## Marp Formatting Rules

- Use Markdown bullets for lists and `$$...$$` for displayed equations.
- Keep equations readable in plain Markdown; avoid custom macros unless the user provided them.
- Use concise titles that describe the slide's teaching role.
- Do not include speaker notes unless the user asks.
- Do not use HTML, custom themes, or external assets unless requested.
- Keep the deck source self-contained.

## Reference Example

When converting a sparse undergraduate numerical methods outline, read `references/fdm-example.md` for a compact before/after pattern. Use it as a style reference, not as required content.

## Completion Checklist

- Output a complete Marp Markdown deck, not just an outline.
- Preserve the user's lecture intent and audience.
- Correct visible typos in generated slide text.
- Add missing explanations needed for the requested audience.
- Include examples or exercises when the input implies a teachable lecture rather than a short reference deck.
- Name the output file path in the final response.
