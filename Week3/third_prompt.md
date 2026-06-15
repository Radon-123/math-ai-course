---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #ffffff
---

# Continuity — Graduate-level refresher

## Outline

- Definitions: epsilon–delta, sequential, topological
- Basic examples and types of discontinuities
- Key theorems and consequences
- Why continuity is a desired property
- Sketches and examples

---

## Epsilon–delta definition (display)

We say $f$ is continuous at $a$ if

$$
\lim_{x \to a} f(x) = f(a)
\iff
\forall\,\varepsilon>0\ \exists\,\delta>0\ \text{such that } |x-a|<\delta \Rightarrow |f(x)-f(a)|<\varepsilon.
$$

This is the primary analytic formulation used in real analysis.

---

## Sequential and topological characterizations

- Sequential: $f$ is continuous at $a$ iff for every sequence $(x_n)$ with $x_n\to a$ we have $f(x_n)\to f(a)$.
- Topological: $f$ is continuous iff for every open set $U$ the preimage $f^{-1}(U)$ is open.

These equivalent viewpoints are useful in different contexts.

---

## Examples: standard continuous functions

- Polynomials: $p(x)=\sum_{k=0}^n c_k x^k$ (continuous everywhere)
- Rational functions $r(x)=\frac{p(x)}{q(x)}$ on domains where $q(x)\neq 0$
- Trigonometric and exponential functions: $\sin x,\ \cos x,\ e^x$

---

## Types of discontinuities (illustrative)

- Jump discontinuity:
  $$f(x)=\begin{cases}1 & x<0\\ 2 & x\ge 0\end{cases}$$
- Removable discontinuity: $g(x)=\dfrac{x^2-1}{x-1}$ at $x=1$ (removable by redefining $g(1)=2$)
- Infinite (essential) discontinuity: $h(x)=\dfrac{1}{x}$ at $x=0$

---

## Algebraic closure and basic rules

If $f$ and $g$ are continuous at $a$ then the following are continuous at $a$ (when defined):

- $f+g$, $f-g$, $fg$
- $\dfrac{f}{g}$ provided $g(a)\neq 0$
- Composition $f\circ g$ when $g$ is continuous at $a$ and $f$ at $g(a)$

---

## Key theorems (consequences of continuity)

- Intermediate Value Theorem (IVT): If $f$ is continuous on $[a,b]$ and $N$ is between $f(a)$ and $f(b)$ then $\exists c\in[a,b]$ with $f(c)=N$.
- Extreme Value Theorem (EVT): A continuous function on a compact set attains its maximum and minimum.
- Continuous image of a compact set is compact; continuous image of a connected set is connected.
- Uniform continuity on compact domains: continuous $\Rightarrow$ uniformly continuous on compact sets.
- Continuous functions on $[a,b]$ are Riemann integrable.

---

## Why continuity is a desired property

- Stability: small changes in input produce small changes in output, which is crucial for modeling and numerical work.
- Structure preservation: continuity preserves topological properties (connectedness, compactness) and enables global conclusions from local data.
- Analytical convenience: many limit-interchange results, root-finding methods, and integration theorems assume continuity.
- Computability and approximation: continuous functions on compact sets can be uniformly approximated (Weierstrass approximation theorem for polynomials), enabling numerical approximation.
- Physical modeling: most physical quantities vary continuously; discontinuities often signal idealizations or phase changes.

---

## Sketch: IVT proof (idea)

Assume $f(a)<N<f(b)$ and let $S=\{x\in[a,b]:f(x)\le N\}$. Show $S$ is nonempty and bounded above, take $c=\sup S$, then use continuity at $c$ to conclude $f(c)=N$.

---

## Useful equivalences and checks

- To prove continuity at a point: use epsilon–delta or sequential criterion depending on convenience.
- To disprove continuity: produce sequences $x_n\to a$ with $f(x_n)$ not converging to $f(a)$ or show left/right limits differ.

---

## Further reading and exercises

- Rudin, Principles of Mathematical Analysis — continuity chapter review.
- Prove: continuous image of compact set is compact; continuous image of connected set is connected.
- Exercises: construct functions with prescribed types of discontinuities; prove uniform continuity on compact sets.

---

## Questions and discussion

Let's look at examples, proofs, or numerical illustrations you'd like to cover.

