---
marp: true
theme: default
paginate: true
class: lead
---

# Numerically Solving ODEs with Multistep Methods

From one-step approximations to Adams-Bashforth methods

---

## Today's Goal

By the end, you should be able to:

- Describe a first-order initial value problem
- Explain how one-step and multistep methods differ
- Use the two-step Adams-Bashforth formula
- Compare explicit and implicit multistep methods
- Connect step size to accuracy and stability

---

## The Initial Value Problem

We start with

$$
y'(t)=f(t,y), \qquad y(t_0)=y_0.
$$

The unknown is the function \(y(t)\).

The data are:

- the derivative rule \(f(t,y)\)
- the initial time \(t_0\)
- the initial value \(y_0\)

---

## What A Numerical Method Produces

Choose a step size \(h\) and grid points

$$
t_n=t_0+nh.
$$

Instead of finding the whole function exactly, we compute approximations

$$
y_n \approx y(t_n).
$$

The method is a recipe for advancing from known values to new values.

---

## Why Not Just Solve Exactly?

Some ODEs have closed form solutions, such as

$$
y'=-2y, \qquad y(0)=1,
$$

whose exact solution is

$$
y(t)=e^{-2t}.
$$

Many models do not have convenient symbolic solutions, especially nonlinear, forced, or coupled systems.

---

## One-Step Methods

A one-step method computes $y_{n+1}$ from the current state  $y_n$.

Euler's method:

$$
y_{n+1}=y_n+h f(t_n,y_n).
$$

The slope at the current point predicts the next value.

---

## Runge-Kutta As A Better One-Step Method

Runge-Kutta methods still use only one stored solution value, but sample several slopes inside the step.

Classical RK4 combines four slopes:

$$
y_{n+1}=y_n+\frac{h}{6}(k_1+2k_2+2k_3+k_4).
$$

This usually gives much smaller error than Euler for the same \(h\).

---

## The Multistep Question

If we already computed previous values, should we use them?

For example, at time $t_n$ we may know:

$$
y_n,\quad y_{n-1},\quad y_{n-2}.
$$

Past slopes can help estimate the next area under $f(t,y(t))$.

---

## Integral Form Of The ODE

Integrate both sides from $t_n$ to $t_{n+1}$:

$$
y(t_{n+1})=y(t_n)+\int_{t_n}^{t_{n+1}} f(t,y(t))\,dt.
$$

A numerical method approximates the integral.

The question is: what information should approximate the integrand?

---

## Slope Notation

Write

$$
f_n=f(t_n,y_n).
$$

Then Euler's method is

$$
y_{n+1}=y_n+h f_n.
$$

A multistep method combines several earlier slope values, such as $f_n$ and $f_{n-1}$.

---

## Two-Step Adams-Bashforth

Approximate $f(t,y(t))$ on $[t_n,t_{n+1}]$ by a line through the two previous slope values.

This gives the explicit formula

$$
y_{n+1}=y_n+\frac{h}{2}\left(3f_n-f_{n-1}\right).
$$

It is called the two-step Adams-Bashforth method, or AB2.

---

## Why AB2 Needs A Starter

AB2 needs both $f_n$ and $f_{n-1}$.

At $n=0$, we only know $y_0$.

Common fix:

1. Use Euler, Heun, or RK4 to compute $y_1$
2. Compute $f_0=f(t_0,y_0)$ and $f_1=f(t_1,y_1)$
3. Start AB2 at $n=1$

---

## Worked Model Problem

Use

$$
y'=-2y,\qquad y(0)=1,
$$

with exact solution $y(t)=e^{-2t}$.

Here

$$
f(t,y)=-2y.
$$

This model is simple enough to check errors, but still shows step-size effects.

---

## AB2 Update For The Model

For \(f_n=-2y_n\), AB2 becomes

$$
y_{n+1}
=y_n+\frac{h}{2}\left(3(-2y_n)-(-2y_{n-1})\right).
$$

Simplify:

$$
y_{n+1}=y_n+h(-3y_n+y_{n-1}).
$$

---

## One Numerical Step

Let $h=0.25$, $y_0=1$.

Use Euler for the starter:

$$
y_1=y_0+h(-2y_0)=1+0.25(-2)=0.5.
$$

Then AB2 gives

$$
y_2=0.5+0.25(-3(0.5)+1)=0.375.
$$

The exact value is $e^{-1}\approx 0.3679$.

---

## Explicit Versus Implicit

Explicit multistep methods use known values only.

Example:

$$
y_{n+1}=y_n+\frac{h}{2}(3f_n-f_{n-1}).
$$

Implicit methods include the unknown future value, such as an Adams-Moulton formula:

$$
y_{n+1}=y_n+\frac{h}{2}(f_{n+1}+f_n).
$$

---

## The Tradeoff

Explicit methods:

- are usually cheaper per step
- are straightforward to implement
- may require smaller $h$ for stability

Implicit methods:

- require solving an equation for $y_{n+1}$ 
- are often more stable on stiff problems
- cost more per step, but may allow larger steps

---

## Accuracy And Step Size

Local error measures the error introduced in one step.

Global error measures the accumulated error over many steps.

Smaller \(h\) usually improves accuracy, but:

- more steps mean more computation
- roundoff can accumulate
- stability can still fail for some methods and ODEs

---

## Stability Intuition

For the test equation

$$
y'=\lambda y,
$$

a stable method should not create artificial growth when the true solution decays.

If $\lambda<0$, the exact solution decays:

$$
y(t)=y_0 e^{\lambda t}.
$$

Large steps can make a numerical method oscillate or grow anyway.

---

## What To Watch In Practice

When choosing a method and step size, ask:

- Does the numerical solution change much if \(h\) is halved?
- Does the solution show artificial oscillation or growth?
- Is the problem stiff?
- Is the cost of each step worth the stability or accuracy gained?

---

## Short Exercise

For

$$
y'=-2y,\qquad y(0)=1,
$$

take $h=0.1$.

1. Use Euler to compute $y_1$
2. Use AB2 to compute $y_2$
3. Compare with $e^{-0.2}$
4. Predict what happens if $h$ is doubled

---

## Key Takeaways

- Numerical ODE solvers approximate values $y_n$ on a grid
- One-step methods use only the current state
- Multistep methods reuse previous slopes or values
- AB2 is explicit and needs a starter value
- Accuracy and stability both depend strongly on step size
