---
name: study-guide-generator
description: Create graduate-level study guides on mathematical and physics topics with intuition-first pedagogy, formal definitions, worked examples, and variational connections.
argument-hint: User is asking for a study guide, practice problems, educational material, or structured introduction to a mathematical or physics topic. Requires topic name and context.
---

# Study Guide Generation Skill

## Purpose

Generate comprehensive, graduate-level study guides in Markdown format that introduce complex mathematical or physics topics through intuition before formal theory. Each guide combines conceptual understanding, rigorous mathematics, worked examples, and connections to calculus of variations or broader mathematical frameworks.

## Target Audience

First-year PhD students or advanced undergraduates in physics, engineering, applied mathematics, or related fields who have foundational knowledge but need a structured introduction to a specialized topic.

## Output Structure

### 1. **Introduction and Intuition** (Section 1)
- **Opening motivation:** Use concrete, physical imagery (e.g., "floating rods," "molecular arrangement") to make the topic accessible.
- **Why this approach matters:** Briefly explain why the topic deserves its own framework (e.g., why Q-tensor instead of director vectors).
- **Subsections:**
  - `1.1 Building intuition`: Describe the physical or conceptual motivation without formal math.
  - `1.2 Why [framework/abstraction]`: Explain the benefit of the chosen mathematical representation.

### 2. **Core Concepts** (Section 2)
- **Definitions:** State the central objects and definitions cleanly, with notation and domain specified.
  - Identify the key variables, functions, or structures that the guide will use.
  - Clarify any assumptions or constraints on those objects.
- **Interpretation:** Explain what each core concept means intuitively or geometrically.
- **Properties:** List essential properties, identities, invariants, or classification criteria that the concept obeys.
- **Equivalent formulations:** If there are multiple natural ways to describe the same idea, compare them and explain when each formulation is useful.
- **Simple example:** Provide a short illustrative example that makes the abstract definition concrete.

### 3. **Governing principles and main relations** (Section 3)
- **Primary relations:** Present the main equations, theorems, or rules that govern the topic.
  - This may include differential equations, algebraic identities, functional relations, or axiomatic statements.
- **Derivation or motivation:** Explain where the main relations come from and why they are important.
- **Consequences:** Describe the key consequences, special cases, or limits of the governing relations.
- **Connections:** Note how the main relations tie back to the core definitions and why they matter for understanding the topic.
- **Variational or extremal viewpoint:** If the subject admits an energy, action, or optimization interpretation, mention it as one of several possible perspectives without making it mandatory.

### 4. **Worked Practice Problems** (Section 4)
Create **exactly 2 fully solved problems** with clear pedagogical progression:

#### Problem 1: Computational/Concrete
- **Characteristic:** Compute the main object from a simple, explicit input (e.g., a delta distribution, a simple tensor).
- **Solution:** Step-by-step calculations showing eigenvalues, matrix forms, or integral evaluations.
- **Interpretation:** Explain what the result means physically or mathematically.

#### Problem 2: Theoretical/Optimization
- **Characteristic:** Prove a key property or derive an optimal structure (e.g., maximum-entropy distribution, variational solution).
- **Solution:** Expand all steps:
  - Set up the optimization or constraint problem.
  - Derive stationarity conditions.
  - Show existence of solution and uniqueness properties.
  - Highlight why the framework works (e.g., simultaneous diagonalization).
- **Interpretation:** Emphasize the conceptual insight.

### 5. **Practice Problems with Solutions** (Section 5)
Provide **exactly 3 graded problems** with solutions of varying depth:

- **Problem 1 (Computational):** Direct calculation with moderately detailed solution; tests understanding of the definition.
- **Problem 2 (Conceptual):** Prove a structural property (e.g., tracelessness, symmetry); solution shows key steps but assumes comfort with linear algebra.
- **Problem 3 (Mixed):** Combine computation and conceptual reasoning; describe general form of solution without fully computing.

### 6. **Connections to familiar concepts** (Section 6)
- **Related frameworks:** Connect the topic to a mathematical or physical idea students may already know (e.g. optimization, complex analysis, linear algebra, geometry, differential equations).
- **Analogies:** Use a familiar concept to build intuition for why the main ideas behave the way they do.
- **Translation:** Show how the topic's objects or relations map onto the more familiar framework.
- **Optional extension:** If a variational or extremal interpretation exists, present it as one possible viewpoint among others.

### 7. **Summary and Study Advice** (Section 7)
- **Key takeaways:** 3–5 bullet points of core concepts.
- **Practice path:** Recommend which problems to tackle in what order.
- **Connections:** Suggest related topics or advanced directions.

## Writing Principles

### Notation and Formatting
- Use `$...$` for inline math, `$$...$$` for display equations.
- Define symbols clearly on first use.
- Use bold for key terms: `**maximum entropy**`, `**Q-tensor**`.
- Link concepts with phrases like "Recall that..." or "Compare this to..."

### Pedagogical Flow
1. **Intuition first:** Always begin with a physical picture before equations.
2. **Motivation for abstraction:** Explain *why* a more complex formalism is needed.
3. **Graduated complexity:** Progress from concrete examples to general theory.
4. **Worked examples:** Every new major concept should have a fully worked example nearby.

### Example Usage
When introducing a distribution $\rho$, first describe what it represents (e.g., "probability that a molecule points in direction $\mathbf{n}$"), then write the constraints ($\int \rho = 1$, $\rho(-\mathbf{n}) = \rho(\mathbf{n})$), then show how it connects to the main object.

### Avoid
- Unexplained abbreviations or jargon.
- Proofs without geometric or physical motivation.
- Problems that require external references or tools.
- Overly long sections (break into subsections if > 400 words).

## Topic Selection

### Good candidates for this skill:
- Liquid crystal theories (Oseen–Frank, Landau–de Gennes, disclinations).
- Variational PDEs (elliptic regularity, minimizers of convex functionals).
- Statistical mechanics models (spin systems, maximum entropy, canonical ensembles).
- Continuum mechanics (stress tensors, strain energy, hyperelasticity).
- Field theories (scalar fields, gauge fields, Yang–Mills).

### Less suitable:
- Purely computational/algorithmic topics (unless framed with theory).
- Highly specialized subtopics with no motivation.
- Topics requiring numerical simulation to understand.

## Prompting Strategy

### Initial Prompt Template
```
Create a graduate-level study guide for [TOPIC] following this structure:
1. Introduction with intuitive description (use [PHYSICAL ANALOGY if applicable])
2. Core concepts section defining [PRIMARY OBJECT]
3. Governing principles section describing the main relations or equations
4. Two worked problems: one computational, one theoretical
5. Three practice problems with solutions
6. Connections section relating the topic to another familiar mathematical or physical framework
7. Summary with study advice

Use $ for inline math, $$ for display. Assume the reader knows [PREREQUISITES].
```

### Refinement Prompts
- "Expand the solution to [Problem X] with more detail on [STEP Y]."
- "Add a subsection connecting [CONCEPT A] to [CONCEPT B]."
- "Include a brief historical or motivational note on [TOPIC]."

## Quality Checklist

- [ ] Introduction uses concrete imagery and builds intuition.
- [ ] Core concepts section is mathematically precise and complete.
- [ ] All notation is defined on first use.
- [ ] 2 worked problems are fully solved with interpretations.
- [ ] 3 practice problems span computational, conceptual, and mixed difficulty.
- [ ] Connections section is present and relates the topic to another familiar mathematical or physical framework.
- [ ] Summary summarizes, not merely repeats.
- [ ] All math uses KaTeX with $ and $$ delimiters.
- [ ] No external references needed to follow the content.

## Related Skills and Next Steps

- **`agent-customization`**: Create custom agents or prompts for topic-specific variants.
- **`study-guide-workflow`**: Extend this skill with additional sections (numerical methods, historical context, open problems).
- **`math-tutor`**: Adapt for teaching specific subdisciplines (PDEs, numerical analysis, etc.).

## Example Topics to Try

1. **Fokker–Planck equations and mean-field limits**
2. **Variational formulations of elliptic PDEs**
3. **Homogenization and effective properties**
4. **Nonlinear elasticity and hyperelasticity**
5. **Statistical mechanics of polymer systems**
6. **Calculus of variations: existence and uniqueness**
7. **Gradient flows and Wasserstein geometry**
8. **Hamiltonian mechanics and symplectic structures**
