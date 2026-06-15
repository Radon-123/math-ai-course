---
marp: true
theme: default
class: lead
paginate: true

# Continuity

### Understanding continuous functions and limits

---

## What is continuity?

A function \(f(x)\) is continuous at a point \(a\) if:

- \(\lim_{x \to a} f(x)\) exists
- \(f(a)\) is defined
- \(\lim_{x \to a} f(x) = f(a)\)

---

## One-sided continuity

A function is continuous at \(a\) when both one-sided limits match the value:

- Left-hand limit: \(\lim_{x \to a^-} f(x)\)
- Right-hand limit: \(\lim_{x \to a^+} f(x)\)

If both exist and equal \(f(a)\), continuity holds.

---

## Continuity on an interval

A function is continuous on an interval if it is continuous at every point in that interval.

Common continuous functions:

- Polynomials
- Rational functions on their domains
- Exponential and logarithmic functions
- Trigonometric functions on their natural domains

---

## Discontinuities

Types of discontinuities:

1. Removable
   - \(f(a)\) is undefined or mismatched, but limit exists.
2. Jump
   - Left and right limits differ.
3. Infinite
   - Limit goes to infinity.

---

## Epsilon-Delta definition

\(f(x)\) is continuous at \(a\) if for every \(\varepsilon > 0\), there is a \(\delta > 0\) such that:

\[
|x - a| < \delta \implies |f(x) - f(a)| < \varepsilon
\]

This formalizes "small change in input gives small change in output." 

---

## Graphical intuition

- Smooth curves with no gaps or jumps are continuous.
- A hole can still be fixed by redefining \(f(a)\).
- A jump or vertical asymptote means discontinuity.

---

## Example: continuity check

Let \(f(x) = \begin{cases}
 x^2 & x \neq 2\\
 5 & x = 2
\end{cases}\)

- \(\lim_{x \to 2} f(x) = 4\)
- \(f(2) = 5\)

Conclusion: \(f\) is not continuous at \(x = 2\).

---

## Why continuity matters

- Enables evaluation by substitution
- Supports the Intermediate Value Theorem
- Ensures predictable behavior of functions
- Crucial for calculus, modeling, and real-world systems

---

## Key takeaways

- Continuity means limits and value agree.
- Use one-sided and epsilon-delta tests when needed.
- Watch for removable, jump, and infinite discontinuities.
- Continuous functions are fundamental to calculus.
