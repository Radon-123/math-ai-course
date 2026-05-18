---
marp: true
paginate: true
style: |
  section h2 {
    position: absolute;
    top: 50px;
    left: 75px;
    right: 75px;
  }
---

# Introduction to Power Series

**MATH 212 — Ryan ONeill**

---

## What are Power Series?

$$ f(x) = \sum_{n=0}^\infty C_n(x-a)^n = C_0 +C_1(x-a)+\dots+C_N(x-a)^N+\dots$$


$C_n$: The power series coefficients
$a$: The center of the power series

---

## Examples of Power Series:

$$\frac{1}{1-x}=\sum_{n=0}^\infty x^n$$
$$tan^{-1}(x) = \sum_{n=0}^\infty \frac{(-1)^nx^{2n+1}}{2n+1}$$

---

## Name of the Game:

For what values of x does the power series converge? To find out, follow the recipe:
- Apply a Convergence Test
  - Ratio Test
  - Root Test
- Form Interval of Convergence
- Test Interval endpoints separately
  
---

## Worked Example:

$$tan^{-1}(x) = \sum_{n=0}^\infty \frac{(-1)^nx^{2n+1}}{2n+1}$$

### Step 1: Apply Ratio Test

$$ \lim_{n\to\infty}\left | \frac{a_{n+1}}{a_n}  \right| =  \lim_{n\to\infty}\left | \frac{x^{2n+3}\cdot(2n+1)}{(2n+3)\cdot x^{2n+1}}  \right|= |x^2|\lim_{n\to\infty}\left | \frac{2n+3}{2n+1}  \right|=|x^2|<1$$

### Step 2: Form Interval

$$-1<x<1$$

### Step 3: Test Interval End Points

By the Alternating Series Test, the series converges at $x\in\{-1,1\}$

---

## Visualization of Convergence

<style scoped>
  section {
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>

<video src="Powa.mp4" autoplay muted loop playsinline width="700"></video>