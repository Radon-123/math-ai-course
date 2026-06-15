# The Cauchy-Riemann Equations: A Graduate Study Guide

## 1. Intuitive Physical Picture

Imagine a fluid flowing in a 2D plane. The velocity field has components $u(x,y)$ in the $x$-direction and $v(x,y)$ in the $y$-direction. For the flow to be **incompressible** (no mass accumulation or depletion), the fluid must satisfy the continuity equation:

$$\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = 0$$

Additionally, if the flow is **irrotational** (no spinning vorticity), the curl must vanish:

$$\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} = 0$$

These two conditions define **harmonic flow** in fluid dynamics. Remarkably, they are precisely the **Cauchy-Riemann equations** from complex analysis! This connection reveals that complex analytic functions describe irrotational, incompressible 2D flows—a profound link between mathematics and physics.

---

## 2. Primitive Variables and Definitions

### Complex Variable Framework

Let $z = x + iy$ where $i = \sqrt{-1}$. Consider a complex-valued function:

$$f(z) = u(x,y) + iv(x,y)$$

where:
- **$u(x,y)$**: real part (often a potential in physics)
- **$v(x,y)$**: imaginary part (often the stream function)

The complex derivative is defined as:

$$f'(z) = \lim_{h \to 0} \frac{f(z+h) - f(z)}{h}$$

For this limit to exist and be **independent of the direction** in which $h \to 0$, we must impose consistency conditions on $u$ and $v$.

### Key Notation

- $f(z)$: complex analytic function
- $\bar{z} = x - iy$: complex conjugate
- $u, v \in C^1$: continuously differentiable real functions
- **Analyticity (holomorphicity)**: $f$ is differentiable in the complex sense at every point in a domain

---

## 3. The Cauchy-Riemann Equations

### Statement

A function $f(z) = u(x,y) + iv(x,y)$ is **analytic** in a domain $D$ if and only if $u$ and $v$ satisfy:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$

$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

These are the **Cauchy-Riemann (CR) equations**.

### Geometric Interpretation

The CR equations encode **conformal mapping** properties:
- **Angle preservation**: Analytic functions preserve angles between curves
- **Local scaling**: The magnification factor is uniform in all directions at a point: $|f'(z)| = \sqrt{u_x^2 + u_y^2}$
- **Orientation preservation**: Unless $f'(z) = 0$

### Connection to Harmonic Functions

If $f = u + iv$ is analytic, then both $u$ and $v$ satisfy **Laplace's equation**:

$$\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

$$\nabla^2 v = \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} = 0$$

These are **harmonic functions**—they satisfy $\nabla^2 f = 0$ and model equilibrium potential fields (electrostatics, steady heat flow, incompressible flow).

### The Complex Derivative

When CR equations hold, the complex derivative exists:

$$f'(z) = \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x} = \frac{\partial v}{\partial y} - i\frac{\partial u}{\partial y}$$

---

## 4. Derivation from First Principles

### Setting Up the Problem

We require the complex derivative to exist:

$$f'(z_0) = \lim_{h \to 0} \frac{f(z_0 + h) - f(z_0)}{h}$$

Let $h = \Delta x + i\Delta y$. Expanding $f(z_0 + h)$ to first order:

$$f(z_0 + h) = u(x_0 + \Delta x, y_0 + \Delta y) + iv(x_0 + \Delta x, y_0 + \Delta y)$$

$$\approx u_0 + u_x \Delta x + u_y \Delta y + i(v_0 + v_x \Delta x + v_y \Delta y)$$

where subscripts denote partial derivatives.

### Path 1: Horizontal Approach ($\Delta y \to 0$)

$$f'(z_0) = \lim_{\Delta x \to 0} \frac{u_x \Delta x + i v_x \Delta x}{\Delta x} = u_x + i v_x$$

### Path 2: Vertical Approach ($\Delta x \to 0$)

$$f'(z_0) = \lim_{\Delta y \to 0} \frac{u_y \Delta y + i v_y \Delta y}{i\Delta y} = \frac{u_y + i v_y}{i} = v_y - i u_y$$

### Equating Both Paths

For $f'(z_0)$ to exist, these must be equal:

$$u_x + i v_x = v_y - i u_y$$

Equating real and imaginary parts:
- **Real**: $u_x = v_y$ ✓
- **Imaginary**: $v_x = -u_y$ ✓

These are the **Cauchy-Riemann equations**.

---

## 5. Worked Examples

### Example 1: Exponential Function

**Problem**: Show that $f(z) = e^z$ is analytic everywhere and find $f'(z)$.

**Solution**:

Let $z = x + iy$. Then:

$$f(z) = e^{x+iy} = e^x(\cos y + i\sin y) = e^x\cos y + ie^x\sin y$$

Thus:
- $u(x,y) = e^x \cos y$
- $v(x,y) = e^x \sin y$

**Checking CR equations**:

$$u_x = e^x \cos y, \quad v_y = e^x \cos y \quad \Rightarrow \quad u_x = v_y \quad \checkmark$$

$$u_y = -e^x \sin y, \quad v_x = e^x \sin y \quad \Rightarrow \quad u_y = -v_x \quad \checkmark$$

Since both equations hold and all partial derivatives are continuous everywhere, $e^z$ is analytic on $\mathbb{C}$.

**The derivative**:

$$f'(z) = u_x + iv_x = e^x\cos y + ie^x\sin y = e^z$$

---

### Example 2: Power Function

**Problem**: Determine where $f(z) = z^2$ is analytic.

**Solution**:

$$f(z) = (x+iy)^2 = x^2 - y^2 + 2ixy$$

Thus:
- $u(x,y) = x^2 - y^2$
- $v(x,y) = 2xy$

**Checking CR equations**:

$$u_x = 2x, \quad v_y = 2x \quad \Rightarrow \quad u_x = v_y \quad \checkmark$$

$$u_y = -2y, \quad v_x = 2y \quad \Rightarrow \quad u_y = -v_x \quad \checkmark$$

Both equations hold for **all** $(x,y)$, so $z^2$ is analytic everywhere on $\mathbb{C}$.

**The derivative**:

$$f'(z) = 2x + i(2y) = 2(x+iy) = 2z$$

---

### Example 3: Non-Analytic Function

**Problem**: Show that $f(z) = \bar{z} = x - iy$ is **not analytic**.

**Solution**:

Here:
- $u(x,y) = x$
- $v(x,y) = -y$

**Checking CR equations**:

$$u_x = 1, \quad v_y = -1 \quad \Rightarrow \quad u_x \neq v_y \quad \times$$

The first CR equation fails. Alternatively, the second equation gives:

$$u_y = 0, \quad v_x = 0 \quad \Rightarrow \quad u_y = -v_x \quad \checkmark$$

Since only one equation holds (not both), the function is **not analytic anywhere**. Intuitively, $\bar{z}$ reverses orientation and thus cannot be holomorphic.

---

### Example 4: Harmonic Potential Problem

**Problem**: Let $u(x,y) = x^2 - y^2$ (the real part of $f(z) = z^2$). Find the harmonic conjugate $v(x,y)$ using CR equations.

**Solution**:

The harmonic conjugate $v$ must satisfy the CR equations with the given $u$. We have:

$$u_x = 2x, \quad u_y = -2y$$

From the first CR equation:

$$v_y = u_x = 2x$$

Integrating with respect to $y$:

$$v(x,y) = \int 2x \, dy = 2xy + g(x)$$

where $g(x)$ is an arbitrary function of $x$ alone.

From the second CR equation:

$$v_x = -u_y = 2y$$

Taking the partial derivative of our expression for $v$:

$$v_x = 2y + g'(x) = 2y$$

This requires $g'(x) = 0$, so $g(x) = C$ (constant). Thus:

$$v(x,y) = 2xy + C$$

(Choosing $C=0$ for the principal branch, we recover $v(x,y) = 2xy$ from $f(z) = z^2$.)

---

## 6. Practice Problems

### Problem 1: Polynomial Functions
**Difficulty**: Beginner

Verify that $f(z) = 2z^3 - 5z + 1$ satisfies the Cauchy-Riemann equations at all points. Find $f'(z)$.

<details>
<summary>Solution</summary>

Write $f(z) = 2(x^3 - 3xy^2) + i(6x^2y - 2y^3) - 5x + 1 + i(-5y)$.

Then:
- $u = 2x^3 - 6xy^2 - 5x + 1$
- $v = 6x^2y - 2y^3 - 5y$

Check:
$$u_x = 6x^2 - 6y^2 - 5 = v_y$$
$$u_y = -12xy = -v_x$$

Both hold for all $(x,y)$, so $f$ is entire (analytic everywhere).

By the formula:
$$f'(z) = 6z^2 - 5$$

</details>

---

### Problem 2: Trigonometric Function
**Difficulty**: Intermediate

Show that $f(z) = \cos z$ is analytic everywhere and compute $f'(z)$.

<details>
<summary>Solution</summary>

Recall:
$$\cos z = \frac{e^{iz} + e^{-iz}}{2} = \cos x \cosh y - i\sin x \sinh y$$

Thus:
- $u = \cos x \cosh y$
- $v = -\sin x \sinh y$

Check:
$$u_x = -\sin x \cosh y = v_y$$
$$u_y = \cos x \sinh y = -v_x$$

Both CR equations hold. The derivative is:
$$f'(z) = u_x + iv_x = -\sin x \cosh y + i\sin x \sinh y = -\sin z$$

</details>

---

### Problem 3: Identifying Non-Analytic Regions
**Difficulty**: Intermediate

For $f(z) = |z|^2 = x^2 + y^2$, determine where (if anywhere) $f$ is analytic.

<details>
<summary>Solution</summary>

Here $u = x^2 + y^2$ and $v = 0$. Check CR equations:

$$u_x = 2x, \quad v_y = 0 \Rightarrow u_x \neq v_y \text{ (except at } x=0\text{)}$$

Only at the origin do the CR equations hold, and even there the partial derivatives don't form a consistent complex derivative in a neighborhood. Thus, $|z|^2$ is **nowhere analytic**.

</details>

---

### Problem 4: Finding the Harmonic Conjugate
**Difficulty**: Intermediate

Given $u(x,y) = e^x \cos y$, find the harmonic conjugate $v(x,y)$ and write $f(z)$.

<details>
<summary>Solution</summary>

From CR equations:
$$v_y = u_x = e^x \cos y$$

Integrate with respect to $y$:
$$v = \int e^x \cos y \, dy = e^x \sin y + g(x)$$

Use the second CR equation:
$$v_x = -u_y = e^x \sin y$$

From our expression:
$$v_x = e^x \sin y + g'(x) = e^x \sin y$$

So $g'(x) = 0$, giving $g(x) = C$. Taking $C=0$:

$$v(x,y) = e^x \sin y$$

Therefore:
$$f(z) = e^x \cos y + ie^x \sin y = e^{x+iy} = e^z$$

</details>

---

### Problem 5: Checking Conformality
**Difficulty**: Advanced

Show that $f(z) = z^2$ maps vertical and horizontal lines to parabolas and verify that it preserves the angle between them (up to orientation).

<details>
<summary>Solution</summary>

Under $w = z^2 = (x+iy)^2 = x^2 - y^2 + 2ixy$, let $u = x^2 - y^2$, $v = 2xy$.

**Vertical line** $x = c$:
- Eliminate $x$: $u = c^2 - y^2$, $v = 2cy$
- From the second: $y = v/(2c)$
- Substituting: $u = c^2 - v^2/(4c^2)$ → parabola in the $uv$-plane

**Horizontal line** $y = d$:
- Eliminate $y$: $u = x^2 - d^2$, $v = 2xd$
- From the second: $x = v/(2d)$
- Substituting: $u = v^2/(4d^2) - d^2$ → parabola

**Angle preservation**: At $z_0 = x_0 + iy_0$, the complex derivative is $f'(z_0) = 2z_0$. Since $f'(z_0) \neq 0$ for $z_0 \neq 0$, the mapping is locally conformal (angles are preserved).

</details>

---

## 7. Key Theorems and Results

### Theorem: Cauchy-Goursat
If $f$ is analytic in a simply-connected domain $D$, then:

$$\oint_\gamma f(z) \, dz = 0$$

for any closed contour $\gamma$ in $D$. This is the foundation of complex analysis.

### Theorem: Maximum Modulus
If $f$ is analytic in a domain $D$ and continuous on its boundary, then the maximum of $|f(z)|$ occurs on the boundary, not in the interior.

### Theorem: Liouville
If $f$ is entire (analytic on all of $\mathbb{C}$) and bounded, then $f$ is constant.

---

## 8. Physical Interpretation: Fluid Dynamics

Consider a 2D incompressible, irrotational flow with velocity $\mathbf{v} = (u, v)$. The CR equations ensure:

1. **Incompressibility**: $\nabla \cdot \mathbf{v} = u_x + v_y = 0$
2. **Irrotationality**: $\nabla \times \mathbf{v} = v_x - u_y = 0$

In this case:
- $u$ is related to the **velocity potential** $\phi$ (via $u = -\partial\phi/\partial x$)
- $v$ is related to the **stream function** $\psi$ (via $v = \partial\psi/\partial y$)

And $f(z) = \phi + i\psi$ is analytic! This means:
- Equipotential lines ($\phi = \text{const}$) are orthogonal to streamlines ($\psi = \text{const}$)
- The flow obeys conservation laws derived from complex analysis

---

## 9. Summary and Next Steps

**Core Ideas**:
1. The CR equations are equivalent to complex differentiability
2. Analytic functions are precisely those that describe conformal (angle-preserving) mappings
3. Real and imaginary parts of analytic functions are harmonic
4. Complex analysis connects to fundamental physics (fluids, electromagnetics, quantum mechanics)

**Master these skills**:
- Verify CR equations algebraically
- Derive harmonic conjugates
- Identify domains of analyticity
- Apply to physical problems

**Further study**: Contour integration, residue calculus, conformal mapping applications to boundary value problems.

