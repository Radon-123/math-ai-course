# Q-Tensor Theory for Nematic Liquid Crystals

## 1. Introduction and Intuition

Nematic liquid crystals are materials with molecules that tend to align along a preferred direction, but without positional order like a crystal. The simplest description uses a unit vector called the director $\mathbf{n}$, but this misses important features such as:

- head-tail symmetry: $\mathbf{n}$ and $-\mathbf{n}$ describe the same orientation,
- defects where the direction changes abruptly or is undefined,
- biaxial order and varying degrees of alignment.

The Q-tensor provides a richer description while still capturing the core physics of nematic phases.

### 1.1 Building intuition

Think of a small volume of liquid crystal as a group of rod-like molecules. If they are completely random, the local orientation is isotropic. If they are strongly aligned, a preferred direction emerges. The Q-tensor encodes both:

- the preferred alignment axis,
- how well the rods are aligned.

In a nematic, alignment is usually symmetric under $\mathbf{n} \to -\mathbf{n}$. That means the observable order should not depend on the arrow direction. A matrix can represent this symmetry naturally.

### 1.2 Why a tensor instead of a vector?

A vector orientation is ambiguous for nematics because it changes sign under the same physical state. The Q-tensor is a second-order tensor that is invariant under sign reversal and can describe:

- uniaxial order: one dominant direction,
- biaxial order: two different preferred directions,
- local strength of order and defects.

The tensor also fits well with continuum energy approaches, where spatial gradients of the order parameter matter.

## 2. Core concepts of Q-tensor theory

### 2.1 The Q-tensor definition

For a uniaxial nematic, define the Q-tensor as:

$$
\mathbf{Q} = S\left(\mathbf{n}\otimes\mathbf{n} - \tfrac{1}{3}\mathbf{I}\right),
$$

where:

- $S$ is the scalar order parameter, typically $0 \le S \le 1$,
- $\mathbf{n}$ is the nematic director with $|\mathbf{n}| = 1$,
- $\mathbf{I}$ is the identity matrix.

This matrix is symmetric and traceless by construction.

#### 2.1.1 Probability distribution interpretation

A more fundamental definition starts from a probability density $f(\mathbf{u})$ on the unit sphere $S^2$, where $\mathbf{u}$ is a molecular orientation vector and $f(-\mathbf{u}) = f(\mathbf{u})$ enforces head-tail symmetry. The Q-tensor is then the second moment of the distribution relative to the isotropic state:

$$
\mathbf{Q} = \int_{S^2} \left(\mathbf{u}\otimes\mathbf{u} - \tfrac{1}{3} \mathbf{I}\right) f(\mathbf{u}) \, d\Omega(\mathbf{u}).
$$

This integral definition automatically produces a symmetric traceless tensor. The term $\mathbf{u}\otimes\mathbf{u}$ captures the directional second moment, and subtracting $\tfrac{1}{3}\mathbf{I}$ removes the isotropic contribution.

If the distribution is uniaxial and axially symmetric about a director $\mathbf{n}$, then the tensor has the form

$$
\mathbf{Q} = S\left(\mathbf{n}\otimes\mathbf{n} - \tfrac{1}{3}\mathbf{I}\right),
$$

where the scalar order parameter is

$$
S = \int_{S^2} \left( \frac{3}{2}(\mathbf{u}\cdot\mathbf{n})^2 - \frac{1}{2} \right) f(\mathbf{u}) \, d\Omega(\mathbf{u}).
$$

This shows that $S$ is not an independent primitive variable; rather, it quantifies how strongly the orientation distribution is concentrated along $\mathbf{n}$.

The probabilistic definition is often more natural in statistical mechanics, while the reduced uniaxial form is the simplest continuum representation for many macroscopic problems.

### 2.2 Physical interpretation

- $\mathbf{n}$ is the nematic director with $|\mathbf{n}| = 1$,
- $\mathbf{I}$ is the identity matrix.

This matrix is symmetric and traceless by construction.

### 2.2 Physical interpretation

- If $S = 0$, the state is isotropic: $\mathbf{Q} = \mathbf{0}$.
- If $S > 0$, alignment occurs along $\mathbf{n}$.
- If $S < 0$, the system is oblate with a plane of alignment perpendicular to $\mathbf{n}$.

The eigenvectors of $\mathbf{Q}$ give principal directions of preferred orientation, and eigenvalues quantify the order strength.

### 2.3 General form and biaxiality

A general Q-tensor in three dimensions is a traceless, symmetric 3×3 matrix:

$$
\mathbf{Q} = \begin{pmatrix}
Q_{11} & Q_{12} & Q_{13} \\
Q_{12} & Q_{22} & Q_{23} \\
Q_{13} & Q_{23} & -(Q_{11} + Q_{22})
\end{pmatrix}.
$$

A generic nematic state can be biaxial if the three eigenvalues are distinct. The trace-free condition ensures the correct physical degrees of freedom.

### 2.4 Defects and smooth order

Defects are regions where the director field cannot be defined continuously. The Q-tensor can represent defect cores without singular vector direction because it remains a smooth matrix field even when eigenvectors rotate or degenerate.

## 3. Energy and equilibrium

A complete continuum model uses a free energy functional with two parts:

1. Bulk/free energy density $f_B(\mathbf{Q})$ that favors certain local order,
2. Elastic energy density $f_E(\mathbf{Q},\nabla \mathbf{Q})$ that penalizes spatial distortions.

### 3.1 Landau–de Gennes bulk energy

A common form is:

$$
f_B(\mathbf{Q}) = \tfrac{A}{2}\operatorname{tr}(\mathbf{Q}^2) - \tfrac{B}{3}\operatorname{tr}(\mathbf{Q}^3) + \tfrac{C}{4}[\operatorname{tr}(\mathbf{Q}^2)]^2.
$$

Parameters $A,B,C$ control phase behavior:

- $A$ typically varies with temperature,
- $B$ drives nematic ordering,
- $C$ stabilizes the energy for large order.

### 3.2 Elastic free energy

For spatial variations, the simplest one-constant elastic energy is:

$$
f_E = \tfrac{L}{2} \partial_k Q_{ij} \partial_k Q_{ij},
$$

summed over repeated indices. More general forms allow anisotropic elastic constants, but the one-constant model is useful for intuition.

### 3.3 Total energy functional

The equilibrium configuration minimizes the functional:

$$
\mathcal{F}[\mathbf{Q}] = \int_{\Omega} \left( f_B(\mathbf{Q}) + f_E(\mathbf{Q},\nabla\mathbf{Q}) \right) \, dV,
$$

subject to appropriate boundary conditions on $\mathbf{Q}$ at $\partial\Omega$.

## 4. Worked practice problems

### Worked Problem 1: Uniaxial Q-tensor eigenstructure

**Problem:**

Given a uniaxial Q-tensor in $\mathbb{R}^3$:

$$
\mathbf{Q} = S\left(\mathbf{n}\otimes\mathbf{n} - \tfrac{1}{3}\mathbf{I}\right)
$$

with $\mathbf{n} = (\tfrac{1}{\sqrt{2}},\tfrac{1}{\sqrt{2}},0)$ and $S>0$, find the eigenvalues and eigenvectors of $\mathbf{Q}$.

**Solution:**

1. Compute $\mathbf{n}\otimes\mathbf{n}$:

$$
\mathbf{n}\otimes\mathbf{n} = \begin{pmatrix}
\tfrac{1}{2} & \tfrac{1}{2} & 0 \\
\tfrac{1}{2} & \tfrac{1}{2} & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

2. Subtract $\tfrac{1}{3}\mathbf{I}$:

$$
\mathbf{Q} = S\begin{pmatrix}
\tfrac{1}{2}-\tfrac{1}{3} & \tfrac{1}{2} & 0 \\
\tfrac{1}{2} & \tfrac{1}{2}-\tfrac{1}{3} & 0 \\
0 & 0 & -\tfrac{1}{3}
\end{pmatrix} = S\begin{pmatrix}
\tfrac{1}{6} & \tfrac{1}{2} & 0 \\
\tfrac{1}{2} & \tfrac{1}{6} & 0 \\
0 & 0 & -\tfrac{1}{3}
\end{pmatrix}.
$$

3. Solve the eigenvalue problem for the 2×2 block:

The block is $S\begin{pmatrix}1/6 & 1/2 \\ 1/2 & 1/6\end{pmatrix}$.

- Sum of diagonal entries: $S(1/6+1/6)=S/3$.
- Determinant: $S^2((1/6)^2 - (1/2)^2) = S^2(1/36 - 1/4) = -S^2(8/36) = -2S^2/9$.

Eigenvalues of the block solve $\lambda^2 - (S/3)\lambda - 2S^2/9 = 0$.

Compute:

$$
\lambda = \frac{S/3 \pm \sqrt{(S/3)^2 + 8S^2/9}}{2} = \frac{S/3 \pm \sqrt{S^2/9 + 8S^2/9}}{2} = \frac{S/3 \pm S}{2}.
$$

So eigenvalues are:

- $\lambda_1 = \frac{S/3 + S}{2} = \frac{2S}{3}$,
- $\lambda_2 = \frac{S/3 - S}{2} = -\frac{S}{3}$.

The third eigenvalue is from the $-S/3$ entry in the third coordinate.

Thus the eigenvalues are $2S/3, -S/3, -S/3$.

4. Find eigenvectors:

- For $\lambda_1 = 2S/3$, the 2×2 block eigenvector is $(1,1,0)$, which normalized gives $(1/\sqrt{2},1/\sqrt{2},0) = \mathbf{n}$.
- For $\lambda_2 = -S/3$, one eigenvector in the 2×2 plane is $(1,-1,0)$.
- The third eigenvector is $(0,0,1)$.

**Interpretation:**

The dominant orientation is along $\mathbf{n}$ with eigenvalue $2S/3$, while the two perpendicular directions share the smaller eigenvalue $-S/3$. This shows the Q-tensor captures uniaxial nematic order consistently.

### Worked Problem 2: Minimizing the one-constant energy in one dimension

**Problem:**

Consider a one-dimensional nematic slab $x\in[0,L]$ with a uniaxial Q-tensor of the form

$$
\mathbf{Q}(x) = S\left(\mathbf{n}(x)\otimes\mathbf{n}(x) - \tfrac{1}{3}\mathbf{I}\right),
$$

where $S$ is constant and $\mathbf{n}(x)=\big(\cos \theta(x), \sin\theta(x), 0\big)$. Assume the elastic energy density is $\tfrac{L}{2}|\partial_x \mathbf{Q}|^2$ and boundary conditions $\theta(0)=0$, $\theta(L)=\pi/2$. Find the equilibrium $\theta(x)$.

**Solution:**

1. Compute $|\partial_x \mathbf{Q}|^2$: because $S$ is constant,

$$
\partial_x \mathbf{Q} = S\left(\partial_x\mathbf{n}\otimes\mathbf{n} + \mathbf{n}\otimes\partial_x\mathbf{n}\right).
$$

We only need the magnitude squared. Since $|\mathbf{n}| = 1$ and $\partial_x\mathbf{n} = \theta'(x)(-\sin\theta,\cos\theta,0)$, we get

$$
|\partial_x \mathbf{Q}|^2 = 2S^2|\partial_x\mathbf{n}|^2 = 2S^2[\theta'(x)]^2.
$$

2. The elastic energy becomes

$$
\mathcal{F}[\theta] = \int_0^L \frac{L}{2} \cdot 2S^2[\theta'(x)]^2 \, dx = LS^2 \int_0^L [\theta'(x)]^2 \, dx.
$$

3. This is a classical variational problem for minimizing $\int_0^L[\theta'(x)]^2 dx$ with fixed endpoints. The Euler–Lagrange equation is

$$
\frac{d}{dx}(2\theta') = 0 \quad \Rightarrow \quad \theta''(x) = 0.
$$

4. Integrate twice:

$$
\theta(x) = ax + b.
$$

Apply boundary conditions:

- $\theta(0)=b=0$,
- $\theta(L)=aL=\pi/2$, so $a=\pi/(2L)$.

5. Final result:

$$
\theta(x) = \frac{\pi}{2L} x.
$$

**Interpretation:**

The minimal-energy configuration rotates uniformly from $0$ to $\pi/2$, showing the Q-tensor energy favors smooth director variation when only elastic penalties are present.

## 5. Practice problems with solutions

### Practice Problem 1

**Problem:**

For a two-dimensional nematic with Q-tensor

$$
\mathbf{Q} = \begin{pmatrix} q & 0 \\ 0 & -q \end{pmatrix},
$$

verify that this tensor is traceless, symmetric, and describe the director orientation and order parameter if it is uniaxial.

**Solution:**

- Symmetry: clearly $Q_{12}=Q_{21}=0$, so $\mathbf{Q}=\mathbf{Q}^T$.
- Trace: $q + (-q) = 0$, so it is traceless.

If it is uniaxial, it corresponds to

$$
\mathbf{Q} = S\left(\mathbf{n}\otimes\mathbf{n} - \tfrac{1}{2}\mathbf{I}\right)
$$

in 2D. Comparing with the given tensor, a suitable director is $\mathbf{n} = (1,0)$ and the order parameter is $S = 2q$. This satisfies

$$
S\begin{pmatrix}1 - 1/2 & 0 \\
0 & 0 - 1/2\end{pmatrix} = \begin{pmatrix} q & 0 \\
0 & -q \end{pmatrix}.
$$

### Practice Problem 2

**Problem:**

For a Q-tensor in three dimensions with eigenvalues $\lambda_1=\tfrac{2S}{3}$, $\lambda_2=\lambda_3=-\tfrac{S}{3}$, show that $\operatorname{tr}(\mathbf{Q}^3) = \tfrac{2S^3}{9}$.

**Solution:**

For any symmetric matrix with eigenvalues $\lambda_i$, $\operatorname{tr}(\mathbf{Q}^3) = \sum_i \lambda_i^3$. Then

$$
\lambda_1^3 + \lambda_2^3 + \lambda_3^3 = \left( \frac{2S}{3} \right)^3 + 2\left( -\frac{S}{3} \right)^3 = \frac{8S^3}{27} - 2\frac{S^3}{27} = \frac{6S^3}{27} = \frac{2S^3}{9}.
$$

### Practice Problem 3

**Problem:**

Assume the bulk energy density is $f_B(\mathbf{Q}) = \tfrac{A}{2}\operatorname{tr}(\mathbf{Q}^2) + \tfrac{C}{4}[\operatorname{tr}(\mathbf{Q}^2)]^2$ with $B=0$. For a uniaxial Q-tensor with eigenvalues $2S/3, -S/3, -S/3$, find the value of $S$ that minimizes $f_B$ for $A<0$ and $C>0$.

**Solution:**

First compute $\operatorname{tr}(\mathbf{Q}^2)$:

$$
\operatorname{tr}(\mathbf{Q}^2) = \left(\frac{2S}{3}\right)^2 + 2\left(-\frac{S}{3}\right)^2 = \frac{4S^2}{9} + 2\frac{S^2}{9} = \frac{6S^2}{9} = \frac{2S^2}{3}.
$$

Then

$$
f_B(S) = \frac{A}{2}\cdot \frac{2S^2}{3} + \frac{C}{4} \left(\frac{2S^2}{3}\right)^2 = \frac{A S^2}{3} + \frac{C S^4}{9}.
$$

Minimize by setting derivative to zero:

$$
\frac{df_B}{dS} = \frac{2A S}{3} + \frac{4C S^3}{9} = \frac{2S}{9}(3A + 2C S^2) = 0.
$$

Nonzero solution satisfies $3A + 2C S^2 = 0$, so

$$
S^2 = -\frac{3A}{2C}.
$$

With $A<0$ and $C>0$, this yields a positive order parameter magnitude:

$$
S = \sqrt{-\frac{3A}{2C}}.
$$

The stable minimum occurs at this positive $S$; the isotropic state $S=0$ is a local maximum or saddle when $A<0$.

## 6. Calculus of variations and the Q-tensor

The Q-tensor theory is naturally formulated using calculus of variations because equilibrium states minimize an energy functional over a field space.

### 6.1 Functional setting

We seek $\mathbf{Q}: \Omega \to \mathbb{R}^{3\times3}_{\text{sym},0}$ that minimizes

$$
\mathcal{F}[\mathbf{Q}] = \int_{\Omega} \left( f_B(\mathbf{Q}) + f_E(\mathbf{Q}, \nabla \mathbf{Q}) \right) dV.
$$

The admissible space is typically a Sobolev space such as $H^1(\Omega;\mathbb{R}^{3\times3})$ restricted to symmetric traceless matrices and satisfying boundary conditions.

### 6.2 Euler–Lagrange equations

For the simplest elastic energy, variation of $\mathcal{F}$ with respect to $Q_{ij}$ yields:

$$
L \Delta Q_{ij} = \frac{\partial f_B}{\partial Q_{ij}},
$$

with the Laplacian applied componentwise. For the Landau–de Gennes bulk energy,

$$
\frac{\partial f_B}{\partial Q_{ij}} = A Q_{ij} - B\left(Q_{ik}Q_{kj}\right) + C\operatorname{tr}(Q^2) Q_{ij}.
$$

Thus the equilibrium PDE is

$$
L \Delta Q_{ij} = A Q_{ij} - B Q_{ik}Q_{kj} + C\operatorname{tr}(Q^2) Q_{ij}.
$$

This is a nonlinear elliptic system that couples all components of $\mathbf{Q}$.

### 6.3 Boundary conditions and admissible variations

Common boundary conditions include:

- Dirichlet: specify $\mathbf{Q}$ on $\partial\Omega$,
- Neumann-type: specify natural boundary flux from the elastic term.

Admissible variations $\delta\mathbf{Q}$ must preserve symmetry and tracelessness, and vanish on the boundary for Dirichlet problems.

### 6.4 Defects as variational solutions

Because $\mathbf{Q}$ is a matrix field, defects correspond to points or lines where minimizers are singular or where order drops to zero. The variational framework can capture defect cores through energy concentration rather than requiring a discontinuous director field.

### 6.5 Example: energy of a radial hedgehog defect

In the simplest radial hedgehog configuration,

$$
\mathbf{Q}(r) = S(r) \left( \hat{r}\otimes\hat{r} - \tfrac{1}{3}\mathbf{I} \right),
$$

the calculus of variations reduces the problem to minimizing an energy for the scalar profile $S(r)$ with radial derivatives. This illustrates how the Q-tensor formulation turns a vector defect problem into a well-posed variational problem.

## 7. Summary and study advice

- Start with the idea that the Q-tensor encodes both direction and degree of alignment.
- Remember that Q-tensors are symmetric and traceless, and that uniaxial states reduce to the familiar director form.
- Connect energy minimization directly to the calculus of variations: the equilibrium field solves Euler–Lagrange equations for the Q-tensor functional.
- Practice eigenvalue computations and simple elastic minimization problems to build intuition.

For deeper study, compare the Q-tensor formulation with director-based Oseen–Frank theory, and examine how defects are represented differently in each approach.