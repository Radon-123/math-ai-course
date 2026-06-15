---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #ffffff
---

# Continuity

## Understanding continuous functions

---

## What is continuity?

A function $$f(x)$$ is *continuous* at a point $$a$$ if:

- $$f(a)$$ is defined
- $$\lim_{x \to a} f(x)$$ exists
- $$\lim_{x \to a} f(x) = f(a)$$

If $$f$$ is continuous at every point in an interval, we call it continuous on that interval.

---

## Why continuity matters

- Continuous functions behave predictably: small input changes produce small output changes.
- Many calculus theorems require continuity, including the Intermediate Value Theorem and the Extreme Value Theorem.
- Continuity ensures there are no sudden jumps, holes, or infinite spikes in the graph.
- It is essential for modeling real-world processes that change smoothly.

---

## Visual intuition

- No jumps
- No holes
- No sudden breaks

Continuous functions can be drawn without lifting your pen.

---

## Example: continuous functions

- Polynomials: $$f(x) = x^2 - 3x + 2$$
- Rational functions where denominator $$\neq 0$$
- Sine and cosine: $$\sin x$$, $$\cos x$$
- Exponential functions: $$e^x$$

---

## Example: discontinuities

- Jump discontinuity:
  $$f(x) = \begin{cases}1 & x < 0 \\\ 2 & x \ge 0\end{cases}$$
- Removable discontinuity:
  $$g(x) = \frac{x^2 - 1}{x - 1}$$ at $$x = 1$$
- Infinite discontinuity:
  $$h(x) = \frac{1}{x}$$ at $$x = 0$$

---

## Continuity rules

If $$f$$ and $$g$$ are continuous at $$a$$, then:

- $$f + g$$ is continuous at $$a$$
- $$f - g$$ is continuous at $$a$$
- $$fg$$ is continuous at $$a$$
- $$\frac{f}{g}$$ is continuous at $$a$$ if $$g(a) \neq 0$$
- Composition $$f(g(x))$$ is continuous if both are continuous

---

## Continuity on intervals

- A function is continuous on an interval if it is continuous at every point in that interval.
- Open interval: continuity at every interior point.
- Closed interval: continuity at interior points and appropriate one-sided limits at endpoints.

---

## Intermediate Value Theorem

If $$f$$ is continuous on $$[a, b]$$ and $$N$$ is between $$f(a)$$ and $$f(b)$$, then there exists $$c \in [a, b]$$ such that $$f(c) = N$$.

This guarantees roots and intermediate values for continuous functions.

---

## Example: applying the IVT

If $$f(1) = -2$$ and $$f(3) = 5$$, then for any $$N$$ between $$-2$$ and $$5$$, there is a $$c \in [1,3]$$ with $$f(c)=N$$.

In particular, there is a root in $$[1,3]$$ because 0 lies between $$-2$$ and $$5$$.

---

## Continuity and limits

Continuity means we can evaluate limits simply by plugging in the point:

$$\lim_{x \to a} f(x) = f(a)$$

But if a function is discontinuous, the limit may not equal the function value or may not exist.

---

## Summary

- Continuity means no gaps, jumps, or holes at a point.
- Check: value exists, limit exists, and value equals limit.
- Continuous functions obey useful algebraic rules.
- The Intermediate Value Theorem is a powerful consequence.

---

## Questions?

Let's explore more continuity examples and graphs.
