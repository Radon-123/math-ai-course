---
marp: true
theme: default
paginate: true
class: lead
---

# Finite Difference Method (FDM)

Understanding and implementing finite differences for ODEs & PDEs

---

## Lecture Outline

- Motivation & Applications
- Grid and notation  
- Nonlinear vs Linear differences  
- Boundary value examples: Schrödinger and Poisson Equations
- Parabolic problems 



---

## Why use FDM?

- Works naturally on regular, rectangular domains.
- Produces sparse linear systems that computers can solve efficiently.
- Good introduction to numerical PDEs 

---

## Grid and notation

Domain: $[a,b]$, divide into $N$ intervals with spacing $h=\frac{b-a}{N}$. Grid points: $x_i=a+i h$ for $i=0,1,\dots,N$. Interior nodes: $i=1,\dots,N-1$; boundary nodes: $i=0,N$. Unknown function values are written as $u_i\approx u(x_i)$.

Typical finite-difference stencils use neighboring node values, e.g., $x_{i\pm1}=x_i\pm h$.

---

## Finite Difference: Basic Idea

Using the grid notation, derivatives at node $x_i$ are approximated with nearby values.

- Forward difference at $x_i$: $u'(x_i)\approx \dfrac{u_{i+1}-u_i}{h}$
- Backward difference at $x_i$: $u'(x_i)\approx \dfrac{u_i-u_{i-1}}{h}$
- Central difference at $x_i$: $u'(x_i)\approx \dfrac{u_{i+1}-u_{i-1}}{2h}$

---

## Second Derivative (Central, 2nd order)

For a grid function $u_i\approx u(x_i)$:
$$u''(x_i)\approx \frac{u_{i+1}-2u_i+u_{i-1}}{h^2}.$$ 

This is the 3-point stencil in 1D, and it leads to a tridiagonal linear system when applied across interior nodes.

---

## Example: Discretize terms (actual formulas)

At node $x_i$ with spacing $h$:

- $\sin(x)$: $\sin(x_i)$.
- $\sin(x)\,u'$ (central difference):
  $$\sin(x_i)\,u'(x_i)\approx \sin(x_i)\frac{u_{i+1}-u_{i-1}}{2h}.$$ 
- $e^{x}\,u''$ (central 2nd order):
  $$e^{x_i}\,u''(x_i)\approx e^{x_i}\frac{u_{i+1}-2u_i+u_{i-1}}{h^2}.$$ 

Substitute these at each interior node $x_i$ to form algebraic equations for the unknowns $u_i$.

---

## Constructing a Simple Linear System (1D)

Consider the model problem $-y''(x)+q(x)y(x)=r(x)$ on $[a,b]$ with Dirichlet BCs $y(a)=\alpha$, $y(b)=\beta$. At interior node $x_i$ using $y''_i\approx (y_{i+1}-2y_i+y_{i-1})/h^2$ and $q_i=q(x_i)$, $r_i=r(x_i)$ we obtain

$$-\frac{y_{i+1}-2y_i+y_{i-1}}{h^2}+q(x_i) y_i = r(x_i).$$ 

---

## Constructing a Simple Linear System (1D) — algebraic form

Rearrange to the algebraic form:

$$\left(\frac{2}{h^2}+q(x_i)\right)y_i - \frac{1}{h^2}y_{i-1} - \frac{1}{h^2}y_{i+1} = r(x_i).$$ 

The boundary values $y_0=\alpha$ and $y_N=\beta$ appear in the equations for the first and last interior nodes. For example, at $i=1$ the term $y_{i-1}$ is known as $\alpha$, and at $i=N-1$ the term $y_{i+1}$ is known as $\beta$. These known values move to the right-hand side of the discrete equations, while the interior unknowns $y_1,\dots,y_{N-1}$ remain as the primary unknown vector.

---

## Linear vs Nonlinear (simple example)

Linear discrete equations have unknowns that appear linearly (e.g., from $y''+y=f$). A simple nonlinear example is a term $y\,y'$: discretizing with a central difference at $x_i$ gives

$$y_i\,y'(x_i)\approx y_i\frac{y_{i+1}-y_{i-1}}{2h},$$

which is nonlinear in the vector $\{y_j\}$. Nonlinear discrete systems are typically solved with fixed-point iteration or Newton's method applied to the residual; Newton requires assembling (or approximating) the Jacobian of the discrete system.

---

## Boundary Value Problem: Schrödinger (discretize, more detail)

Time-independent 1D Schrödinger equation:
$$-\frac{\hbar^2}{2m}y''(x)+V(x)y(x)=E y(x),\quad x\in[a,b],$$
with boundary conditions (e.g., $y(a)=y(b)=0$). Using central differences for $y''$ and grid spacing $h$ leads to the matrix eigenproblem
$$H\mathbf{y}=E\mathbf{y},$$
where the discrete Hamiltonian $H$ uses the central-difference approximation for $y''$ and the potential values $V(x_i)$ at each grid point.

Solve the eigenvalue problem $H\mathbf{y}=E\mathbf{y}$ to obtain allowed energies $E$ and eigenfunctions $\mathbf{y}$ approximating continuous solutions.

---

## Boundary Value Problem: Poisson (1D)

1D Poisson with Dirichlet BCs: $u''(x)=f(x)$ on $[a,b]$, $u(a)=\alpha$, $u(b)=\beta$.
Discretize at interior $x_i$:
$$\frac{u_{i+1}-2u_i+u_{i-1}}{h^2}=f(x_i).$$ 
Rearrange to
$$-u_{i-1}+2u_i-u_{i+1}=h^2 f(x_i),$$
which becomes a linear system for the interior unknowns; boundary values appear in the right-hand side.

---

## Parabolic Problem: Heat equation — PDE and discretization

We consider the 1D heat equation on $x\in[0,1]$ with Dirichlet BCs:
$$u_t=\alpha u_{xx},\qquad u(0,t)=u(1,t)=0,\qquad u(x,0)=u_0(x).$$

We discretize in space and in time:
- Space: $x_i=i h$, $i=0,\dots,N$, with $h=1/N$ and $u_i^n\approx u(x_i,t^n)$.
- Time: $t^n=n\Delta t$, $n=0,1,2,\dots$.

Unknowns are the grid values $u_i^n$ at each time level and interior spatial node.

---

## Parabolic Problem: Heat equation — time-stepping schemes

Explicit Forward Euler (time + central space):
$$u^{n+1}_i = u^n_i + \lambda\,(u^n_{i+1}-2u^n_i+u^n_{i-1}),\qquad \lambda=\frac{\alpha\Delta t}{h^2}.$$ 
Stability constraint for the explicit scheme: $\lambda\le 1/2$ (i.e. $\Delta t\le h^2/(2\alpha)$).

Backward (implicit) Euler (requires solve each step):
$$u^{n+1}_i - \lambda\,(u^{n+1}_{i+1}-2u^{n+1}_i+u^{n+1}_{i-1}) = u^n_i,$$
which is unconditionally stable but needs a linear solve per time step.

Crank–Nicolson (second-order in time): average explicit and implicit terms; it is more accurate and requires solving a linear system per step.

---

## Stability & Accuracy

- Order in space comes from the stencil (e.g., central difference is 2nd order).
- Time-stepping order affects temporal accuracy (explicit vs implicit, 1st vs 2nd order).
- Always check stability (use Fourier/CFL analysis for constant-coefficient problems); see the heat-equation slide for a concrete CFL constraint example.

---


 
## Hyperbolic Problems: Wave equation (PDE)

1D wave equation (second-order in time):
$$
u_{tt} = c^2 u_{xx},\qquad x\in[a,b],\ t>0.
$$

Initial conditions: $u(x,0)=u_0(x)$ and $u_t(x,0)=v_0(x)$. Boundary conditions must also be specified (Dirichlet, Neumann, or periodic).

We discretize both in space and in time: space grid $x_i=i h$ and time levels $t^n=n\Delta t$.

---

## Hyperbolic Problems: Wave equation (discrete scheme & stability)

Using central differences in time and central second differences in space yields the standard explicit update at interior node $x_i$:
$$
u^{n+1}_i = 2u^n_i - u^{n-1}_i + \mu\left(u^n_{i+1}-2u^n_i+u^n_{i-1}\right),\qquad \mu=\left(\frac{c\Delta t}{h}\right)^2.
$$

Stability (CFL) for this centered scheme requires
$$\frac{c\Delta t}{h}\le 1.$$

Hyperbolic problems propagate waves; choose $\Delta t$ and $h$ to control numerical dispersion and satisfy stability constraints.

---
## Drawbacks & Practical Tips

- Difficulties with irregular geometry and unstructured meshes
- High accuracy demands very fine meshes (costly)
- Use adaptive mesh refinement or switch to finite element methods for complex domains
- Preconditioners are essential for large linear systems

---

## Short Exercises

1. Discretize $y''+y=0$ on $[0,\pi]$ with Dirichlet BCs; compute eigenvalues numerically.
2. Implement Forward and Backward Euler for the heat equation and compare stability.
3. Discretize Poisson on a unit square and solve with Gauss–Seidel.

 



