---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #ffffff
---

# Continuity — Graduate-level refresher

## Outline

- Analytic definitions: epsilon–delta and sequential
- Basic examples and types of discontinuities
- Fundamental consequences of continuity
- Why continuity is a desired property
- Recommended exercises

---

## Epsilon–delta definition

We say $f$ is continuous at $a$ if

$$
\lim_{x \to a} f(x) = f(a)
\iff
\forall\,\varepsilon>0\ \exists\,\delta>0\ \text{such that } |x-a|<\delta \Rightarrow |f(x)-f(a)|<\varepsilon.
$$

This is the primary analytic formulation used in real analysis.

---

## Sequential characterization

- $f$ is continuous at $a$ iff for every sequence $(x_n)$ with $x_n\to a$, we have $f(x_n)\to f(a)$.
- This is often useful when working with sequences or limits directly.

---

## Examples: standard continuous functions

- Polynomials: $p(x)=\sum_{k=0}^n c_k x^k$ (continuous everywhere)
- Rational functions $r(x)=\dfrac{p(x)}{q(x)}$ on domains where $q(x)\neq 0$
- Elementary transcendental functions: $\sin x$, $\cos x$, $e^x$

---

## Types of discontinuities

- Jump discontinuity:
  $$f(x)=\begin{cases}1 & x<0\\ 2 & x\ge 0\end{cases}$$
- Removable discontinuity: $g(x)=\dfrac{x^2-1}{x-1}$ at $x=1$ (removable by redefining $g(1)=2$)
- Infinite discontinuity: $h(x)=\dfrac{1}{x}$ at $x=0$

---

## Algebraic closure and basic rules

If $f$ and $g$ are continuous at $a$, then the following are continuous at $a$ when defined:

- $f+g$, $f-g$, $fg$
- $\dfrac{f}{g}$ provided $g(a)\neq 0$
- Composition $f\circ g$ when $g$ is continuous at $a$ and $f$ is continuous at $g(a)$

---

## Fundamental consequences of continuity

- Intermediate Value Theorem: If $f$ is continuous on $[a,b]$ and $N$ is between $f(a)$ and $f(b)$, then there exists $c\in[a,b]$ with $f(c)=N$.
- Extreme Value Theorem: If $f$ is continuous on $[a,b]$, then $f$ attains both a maximum and a minimum on $[a,b]$.
- Boundedness and attainability: a continuous $f$ on $[a,b]$ is bounded and attains its bounds.
- Uniform continuity on closed intervals: a continuous function on $[a,b]$ is uniformly continuous.
- Riemann integrability: a continuous function on $[a,b]$ is Riemann integrable.

---

## Why continuity is a desired property

- Stability: small changes in input produce small changes in output, which is essential for reliable analysis and computation.
- Predictability: continuous functions have no sudden jumps or holes, so their behavior is easier to understand and approximate.
- Consequence-driven: many classical theorems and numerical methods depend on continuity.
- Model fidelity: continuity matches many physical and geometric phenomena, making functions easier to interpret.
- Numerical approximation: continuous functions on intervals can be approximated accurately by polynomials or piecewise linear functions.

---

## Practical implications for analysis

- Root-finding algorithms like bisection rely on the Intermediate Value Theorem.
- Optimization over intervals relies on the existence of maxima and minima for continuous functions.
- Limit interchange and series convergence arguments often assume continuity.
- Continuity is the first regularity property needed before considering differentiability or integrability.

---

## Useful equivalences and checks

- To prove continuity at a point: choose the epsilon–delta definition for direct control or the sequential criterion if sequences are available.
- To disprove continuity: find sequences $x_n\to a$ with $f(x_n)$ not converging to $f(a)$, or show left/right limits differ at $a$.

---

## Recommended exercises

- Verify continuity of basic algebraic and transcendental functions.
- Classify discontinuities for piecewise-defined examples.
- Use the IVT to locate roots of continuous functions on intervals.
- Show a continuous function on $[a,b]$ is bounded and attains a max/min.

---

## Questions and discussion

Let's focus on examples, applications, or any aspect you want to revisit.

