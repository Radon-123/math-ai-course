# Lecture Plan: Numerically Solving ODEs with Multistep Methods

## Audience

Undergraduate students with prior exposure to calculus, basic differential equations, and introductory numerical methods.

## Rough Outline

1. **Start with the initial value problem**
   - Introduce a first-order ODE in the form:
     \[
     y'(t)=f(t,y), \qquad y(t_0)=y_0
     \]
   - Explain that the goal is to approximate \(y(t)\) at a sequence of time points.
   - Contrast exact symbolic solutions with numerical approximations.

2. **Review one-step methods as a foundation**
   - Briefly revisit Euler's method and Runge-Kutta methods.
   - Emphasize that one-step methods compute \(y_{n+1}\) using only the current value \(y_n\).
   - Use this as motivation for asking whether previous solution values can improve accuracy.

3. **Introduce the main idea of multistep methods**
   - Explain that multistep methods use several earlier points, such as \(y_n\), \(y_{n-1}\), and \(y_{n-2}\).
   - Present the general intuition: past slopes help predict the next value.
   - Discuss why these methods need starting values from another method, often Runge-Kutta.

4. **Derive an explicit Adams-Bashforth method**
   - Build the idea from integrating the ODE:
     \[
     y_{n+1}=y_n+\int_{t_n}^{t_{n+1}} f(t,y(t))\,dt
     \]
   - Approximate the integrand using previous slope values.
   - Present the two-step Adams-Bashforth formula:
     \[
     y_{n+1}=y_n+\frac{h}{2}\left(3f_n-f_{n-1}\right)
     \]

5. **Compare explicit and implicit multistep methods**
   - Explain that explicit methods use known past information only.
   - Introduce implicit methods, such as Adams-Moulton or backward differentiation formulas, where \(y_{n+1}\) appears in the formula.
   - Discuss the tradeoff: implicit methods require solving an equation but can be more stable.

6. **Discuss accuracy, stability, and step size**
   - Define local error and global error at an intuitive level.
   - Show that using more past points can increase order, but not automatically make a method reliable.
   - Introduce stability as a key concern, especially for long-time simulations and stiff equations.

7. **Work through a simple numerical example**
   - Apply a two-step Adams-Bashforth method to a simple ODE such as \(y'=-2y\), \(y(0)=1\).
   - Generate the first starting value with Euler's method or a Runge-Kutta method.
   - Compare the numerical solution with the exact solution \(y(t)=e^{-2t}\) and discuss the observed error.

## Learning Goal

By the end of the lecture, students should understand how multistep methods use information from several previous time steps, how explicit and implicit versions differ, and why accuracy and stability both matter when numerically solving ODEs.
