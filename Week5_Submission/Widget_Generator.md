---
name: math-teaching-widget
description: Create self-contained interactive HTML/JavaScript teaching widgets for math topics. Use when the user asks for a visual math demo, educational animation, browser-based manipulative, canvas/SVG visualization, or reusable widget for a specified math concept; also use when the user gives a broad math topic and wants help choosing an interactive implementation idea.
---

# Math Teaching Widget

## Overview

Build a standalone browser widget that teaches a math idea through direct manipulation: sliders, toggles, canvas/SVG drawing, and concise mathematical readouts. Prefer a single self-contained HTML file with embedded CSS and JavaScript unless the user asks for a framework.

## Clarify the Topic

If the user specifies both the math topic and the desired interaction, implement it directly.

If the user gives a math topic but no concrete widget idea, suggest 3-5 specific interactive ideas and ask the user to pick one or suggest a new one. Keep the suggestions tied to the topic and varied in cognitive goal:

- one geometric or visual intuition widget
- one parameter-sweep widget
- one numerical approximation widget, if relevant
- one comparison or error-analysis widget, if relevant
- one game-like or challenge widget, if appropriate

If the user does not specify a topic at all, ask for the math topic before building.

Example response for an underspecified topic:

```text
For linear algebra, a few good widget directions are:
- Vector projection: drag a vector and watch its projection onto a line.
- Eigenvectors: transform a grid with a 2x2 matrix and highlight directions that only stretch.
- Least squares: move data points and see the best-fit line update.
- Matrix multiplication: animate how one linear map followed by another composes.

Which one should I build, or do you want a different idea?
```

## Implementation Workflow

1. Inspect the workspace and choose a clean output location.
   - If the user requests a new folder, create one with a short descriptive name.
   - If editing an existing widget, preserve its style and behavior unless the user asks for a redesign.

2. Define the teaching model before coding.
   - Name the mathematical object being shown.
   - Decide which quantities are fixed and which are controlled by the user.
   - Choose a stable numerical or analytic method.
   - Decide what visual features make the concept legible: axes, samples, curves, residuals, grids, labels, error, phase, or comparison traces.

3. Build the widget as a self-contained HTML file.
   - Use embedded `<style>` and `<script>`.
   - Avoid external libraries, CDNs, external images, web fonts, and build tooling unless the user explicitly allows them.
   - Use `<canvas>` for animated plots, fields, particles, simulations, or dense drawings.
   - Use inline SVG only when crisp geometry or annotations are easier than canvas.

4. Add controls that match the mathematical parameters.
   - Use sliders for continuous or integer parameters.
   - Use checkboxes/toggles for binary display options.
   - Use select menus or segmented controls for modes or formulas.
   - Show live numeric readouts next to controls.
   - Keep labels short but mathematically precise.

5. Add a live mathematical readout.
   - Display the current equation, transformation, recurrence, matrix, or approximation under or near the visualization.
   - Update the readout whenever controls change.
   - Use notation that matches the labels in the widget.

6. Animate state changes.
   - Ease from the previous state to the new target after control changes.
   - Keep animation educational rather than decorative: show convergence, deformation, traversal, accumulation, or approximation improvement.
   - Avoid motion that obscures the final mathematical object.

7. Validate the artifact.
   - Check that the HTML contains no unwanted external references.
   - Parse the embedded JavaScript when possible with `new Function(...)` or equivalent.
   - Open or inspect the file if a browser/tooling path is available.
   - Confirm all requested controls exist and affect the displayed math.

## Design Guidelines

- Make the first screen the actual widget, not a landing page.
- Keep the layout focused: visualization dominant, controls adjacent or below.
- Put legends where they do not cover axes, data, equations, or control surfaces.
- Use stable dimensions for canvases and controls so labels and animation do not shift the layout.
- Avoid long explanatory text inside the app. Use concise captions and mathematical labels.
- Make the visual encoding clear: distinguish current solution, target/exact solution, samples, boundaries, errors, or constraints with color and shape.
- Ensure the widget works on desktop and mobile viewports.

## Math Modeling Patterns

Use the simplest correct model that teaches the topic.

- **Analytic formulas**: compute directly when closed forms are available and stable.
- **Finite differences**: use for 1D boundary value problems, heat/wave equation demos, derivative approximations, and error-vs-grid-size widgets.
- **Numerical iteration**: use for convergence demos, fixed-point iteration, Newton's method, gradient descent, Markov chains, and recurrence relations.
- **Linear algebra transforms**: draw basis vectors, a grid, sample points, eigen-directions, determinant area, or singular-value axes.
- **Calculus demos**: animate tangent/secant lines, Riemann sums, Taylor polynomials, gradient fields, or optimization paths.
- **Probability demos**: animate sampling, histograms, law of large numbers, Bayes updates, random walks, or distribution parameters.

When using numerical methods, prefer stable bounded defaults and clamp dangerous values. Explain instability visually only when that is the purpose of the widget.

## Example: 1D Poisson Widget Pattern

For a 1D Dirichlet Poisson problem, a good widget structure is:

- Model: `-D u''(x) = f(x)` on `[0,1]`, with `u(0)=a`, `u(1)=b`.
- Controls: number of interior domain points `n`, left boundary `a`, right boundary `b`, diffusion coefficient `D`, and forcing parameters.
- Computation: solve the tridiagonal finite-difference system for the exact discrete solution.
- Visualization: draw axes, grid samples, boundary points, and a smooth connected solution curve.
- Readout: update the equation under the graph.
- Animation: ease the displayed curve toward the newly solved target after slider changes.

Use this pattern as a reference, not a template to force onto unrelated topics.

## Completion Checklist

Before finishing:

- The widget is in the requested location, usually a new folder with `index.html`.
- The file is self-contained unless the user requested otherwise.
- The math topic and core equation/model are visible in the UI.
- Every control has an output readout and visibly changes the math.
- The canvas/SVG drawing is responsive and does not clip important labels or legends.
- The embedded JavaScript parses without syntax errors.
- The final response names the file path and summarizes the implemented interactions.
