---
name: study-guide-workflow
description: 'Create a reusable skill for producing graduate-level study guides that combine intuition, mathematical structure, and worked problems.'
argument-hint: What advanced topic should this study guide cover in a study guide format?  
---
Related skill: `agent-customization`. Load and follow **skills.md** for template and principles.

Guide the user to create a reusable study guide template for an advanced mathematical or physical topic that includes:
- an intuitive physical picture,
- a clear statement of primitive variables and definitions,
- the main governing equations,
- worked examples with full solutions,
- practice problems with solutions,
- a conceptual connection to variational principles when relevant.

## Extract from Conversation
Review the conversation history and generalize the workflow:
- Begin with a physical metaphor or intuitive example (e.g. floating rods) to anchor the topic.
- Introduce the primitive description of the system or field, including notation and any probability distribution when appropriate.
- Define the main order parameter or tensor in a way that matches the user’s preferred formulation.
- Explain symmetry, invariants, and eigenstructure properties if the parameter is a matrix.
- Connect the formulation to an energy functional and calculus of variations if applicable.
- Include worked examples and practice problems with detailed, step-by-step solutions.
- Adapt to the user’s notation preferences and application context.

## Clarify if Needed
If the user’s intent is not yet clear, ask:
- Which graduate-level topic or physical system should the study guide address?
- Should the guide be based on probability distributions, tensors, differential equations, or another macroscopic description?
- What is the target audience: beginning graduate, advanced graduate, or research-level?
- Do you want the output to be a single Markdown file, a structured template, or both?
- Are there any notation conventions to enforce (e.g. `\rho`, `\mathbf{n}`, `Q`, `\mathbf{Q}`)?

## Iterate
1. Draft the study guide structure in `SKILL.md` with explicit section guidance.
2. Identify any missing scope, unclear notation, or assumptions and ask follow-up questions.
3. Refine the skill to specify the exact section order, level of detail, and problem format.
4. Summarize the final skill, propose example prompts that use it, and suggest related customization or prompt files to create next.
