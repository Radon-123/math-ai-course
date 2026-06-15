# Q-Tensor Theory for Nematic Liquid Crystals

## 1. Introduction and Intuition

Nematic liquid crystals behave like a fluid full of tiny floating rods. Each molecule is rod-like and can rotate almost freely, but when enough rods tend to point in similar directions, the material develops orientational order without forming a crystal lattice.

The local state is best described by how these rods are distributed over all possible orientations on the unit sphere. This is why the probability density $\rho$ on $S^2$ is the primitive description, and why the Q-tensor is defined from the second moment of that distribution.

In applications where the molecular distribution is broad, multimodal, or biaxial, the simple director-only picture fails. The Q-tensor is the natural continuum descriptor for such cases because it captures the preferred axes of rod alignment and the anisotropy of the distribution.

### 1.1 Orientational statistics

Let $\mathbf{n}$ denote a unit rod direction on the sphere $S^2$. Physically, $\mathbf{n}$ represents the orientation axis of a rod-like molecule; it is not an arrow pointing from head to tail, but the local axis along which rods are aligned.

A nematic orientation distribution is described by a probability density $\rho(\mathbf{n})$ with

$$
\rho(\mathbf{n}) \ge 0, \qquad \int_{S^2} \rho(\mathbf{n}) \, d\Omega(\mathbf{n}) = 1,
$$

and head-tail symmetry

$$
\rho(-\mathbf{n}) = \rho(\mathbf{n}).
$$

This symmetry ensures that the physical state does not distinguish $\mathbf{n}$ from $-\mathbf{n}$.

### 1.2 Why a tensor? Why not a vector?

A director vector is ambiguous for nematics because $\mathbf{n}$ and $-\mathbf{n}$ represent the same physical orientation. A second-order tensor built from the second moment of $\rho$ is invariant under this sign change and captures the preferred axes of alignment.

If the orientation distribution is completely random, $\rho$ is uniform and the system is isotropic. If the distribution is anisotropic, the tensor carries information about the preferred directions and the shape of the distribution.

## 2. Core concepts of Q-tensor theory

### 2.1 Q as the second moment from isotropic background

The Q-tensor is defined directly from the probability density $\rho(\mathbf{n})$ by

$$
\mathbf{Q} = \int_{S^2} \left(\mathbf{n} \otimes \mathbf{n} - \tfrac{1}{3} \mathbf{I} \right) \rho(\mathbf{n}) \, d\Omega(\mathbf{n}).
$$

This definition has several important consequences:

- $\mathbf{Q}$ is symmetric because $\mathbf{n}\otimes\mathbf{n}$ is symmetric.
- $\mathbf{Q}$ is traceless because $\operatorname{tr}(\mathbf{n}\otimes\mathbf{n}) = 1$ and the isotropic subtraction contributes $-\tfrac{1}{3}\operatorname{tr}(\mathbf{I}) = -1$.
- If $\rho$ is uniform, then $\mathbf{Q}=\mathbf{0}$, which corresponds to the isotropic phase.
- If $\rho$ has preferred directions, then $\mathbf{Q}$ is nonzero and its eigenvectors give the principal alignment axes.

### 2.2 Interpretation of Q eigenstructure

Because $\mathbf{Q}$ is symmetric and traceless, it has three real eigenvalues $\lambda_1, \lambda_2, \lambda_3$ with

$$
\lambda_1 + \lambda_2 + \lambda_3 = 0.
$$

The eigenvectors define an orthogonal frame of preferred directions. If two eigenvalues coincide, the tensor is uniaxial and the remaining eigenvector gives the symmetry axis. If all three eigenvalues are distinct, the tensor is biaxial.

Positive eigenvalues indicate directions where the distribution is more concentrated than isotropic, while negative eigenvalues indicate directions where the density is reduced relative to the isotropic background.

### 2.3 Generic matrix form

A general symmetric, traceless Q-tensor in three dimensions can be written as:

$$
\mathbf{Q} = \begin{pmatrix}
Q_{11} & Q_{12} & Q_{13} \\
Q_{12} & Q_{22} & Q_{23} \\
Q_{13} & Q_{23} & -(Q_{11} + Q_{22})
\end{pmatrix}.
$$

This matrix representation is the natural continuum field for nematic order, especially when the underlying distribution is complex or varies in space.

### 2.4 Maximum-entropy distributions and the Q-tensor

In many statistical models, the physical orientation distribution is assumed to minimize the Boltzmann–Shannon entropy subject to constraints imposed by observed moments like $\mathbf{Q}$.

The Boltzmann–Shannon entropy for a distribution $\rho$ is

$$
H[\rho] = \int_{S^2} \rho(\mathbf{n}) \log \rho(\mathbf{n}) \, d\Omega(\mathbf{n}).
$$

Given a fixed Q-tensor and normalization constraint, the optimal distribution that minimizes $H[\rho]$ has the exponential form

$$
\rho(\mathbf{n}) = \frac{1}{Z} \exp\left( \mathbf{\Lambda} : (\mathbf{n} \otimes \mathbf{n}) \right),
$$

where $\mathbf{\Lambda}$ is a symmetric Lagrange multiplier matrix and

$$
Z = \int_{S^2} \exp\left( \mathbf{\Lambda} : (\mathbf{n} \otimes \mathbf{n}) \right) \, d\Omega(\mathbf{n}).
$$

Because the Q constraint involves only the second moment $\mathbf{n}\otimes\mathbf{n}$, $\mathbf{\Lambda}$ and $\mathbf{Q}$ are simultaneously diagonalizable. In other words, the optimal $\rho$ is orthogonalized by the same eigenframe as $\mathbf{Q}$.

This property follows from the stationarity condition:

$$
0 = \delta\left( H[\rho] - \mu \int_{S^2} \rho \, d\Omega - \mathbf{\Lambda} : \left[ \int_{S^2} \left(\mathbf{n}\otimes\mathbf{n} - \tfrac{1}{3} \mathbf{I} \right) \rho(\mathbf{n}) \, d\Omega - \mathbf{Q} \right] \right).
$$

The variation gives

$$
\log \rho(\mathbf{n}) = \mu - 1 + \mathbf{\Lambda} : (\mathbf{n} \otimes \mathbf{n}),
$$

which leads to the exponential ansatz above. Since $\mathbf{\Lambda}$ is symmetric, it shares eigenvectors with the symmetric matrix $\mathbf{Q}$, and the distribution depends only on the projections of $\mathbf{n}$ onto those eigenvectors.

### 2.5 Why the probability distribution aligns with Q

If $\mathbf{Q}$ has eigenvectors $\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3$, then we can choose coordinates where

$$
\mathbf{Q} = \operatorname{diag}(\lambda_1, \lambda_2, \lambda_3),
$$

and the optimal distribution has the form

$$
\rho(\mathbf{n}) = \frac{1}{Z} \exp\left( \lambda_1 (n_1)^2 + \lambda_2 (n_2)^2 + \lambda_3 (n_3)^2 \right).
$$

Because this density depends only on squared projections onto the eigenvectors, the same orthogonal frame diagonalizes both $\mathbf{Q}$ and the maximum-entropy distribution. This is the key mathematical connection between $\mathbf{Q}$ and the optimal $\rho$.

## 3. Energy and equilibrium

A continuum nematic model uses a free energy functional over the Q-field. The simplest split is:

1. bulk energy density $f_B(\mathbf{Q})$ capturing local ordering preferences,
2. elastic energy density $f_E(\mathbf{Q}, \nabla \mathbf{Q})$ penalizing spatial distortion.

### 3.1 Bulk energy density

A common bulk energy is the Landau–de Gennes form:

$$
f_B(\mathbf{Q}) = \tfrac{A}{2}\operatorname{tr}(\mathbf{Q}^2) - \tfrac{B}{3}\operatorname{tr}(\mathbf{Q}^3) + \tfrac{C}{4}[\operatorname{tr}(\mathbf{Q}^2)]^2.
$$

This expression depends only on the invariants of $\mathbf{Q}$ and is compatible with the probabilistic definition because those invariants are functions of the second moment.

### 3.2 Elastic energy density

The simplest elastic penalty is the one-constant form:

$$
f_E = \tfrac{L}{2} \partial_k Q_{ij} \partial_k Q_{ij}.
$$

This penalizes spatial gradients of the Q-field and encourages smooth variations of the orientation distribution.

### 3.3 Total free energy

The equilibrium Q-field minimizes

$$
\mathcal{F}[\mathbf{Q}] = \int_{\Omega} \left( f_B(\mathbf{Q}) + f_E(\mathbf{Q},\nabla\mathbf{Q}) \right) \, dV,
$$

subject to boundary conditions on $\mathbf{Q}$ at $\partial\Omega$.

## 4. Worked practice problems

### Worked Problem 1: Computing Q from a simple distribution

**Problem:**

Let $\rho(\mathbf{n})$ be supported on the two antipodal directions $\mathbf{e}_z = (0,0,1)$ and $-\mathbf{e}_z$, with equal weight. That is,

$$
\rho(\mathbf{n}) = \tfrac{1}{2}\delta(\mathbf{n}-\mathbf{e}_z) + \tfrac{1}{2}\delta(\mathbf{n}+\mathbf{e}_z).
$$

Compute the corresponding Q-tensor.

**Solution:**

The second moment is

$$
\int_{S^2} \mathbf{n}\otimes\mathbf{n} \, \rho(\mathbf{n}) \, d\Omega(\mathbf{n}) = \tfrac{1}{2} \mathbf{e}_z \otimes \mathbf{e}_z + \tfrac{1}{2} (-\mathbf{e}_z) \otimes (-\mathbf{e}_z) = \mathbf{e}_z \otimes \mathbf{e}_z.
$$

Thus

$$
\mathbf{Q} = \mathbf{e}_z \otimes \mathbf{e}_z - \tfrac{1}{3} \mathbf{I}
= \begin{pmatrix}
-\tfrac{1}{3} & 0 & 0 \\
0 & -\tfrac{1}{3} & 0 \\
0 & 0 & \tfrac{2}{3}
\end{pmatrix}.
$$

This tensor is symmetric and traceless, and its eigenvectors are the Cartesian axes. The eigenvalues are $(-\tfrac{1}{3}, -\tfrac{1}{3}, \tfrac{2}{3})$, showing a preferred alignment along $\mathbf{e}_z$.

### Worked Problem 2: Optimal distribution for fixed Q

**Problem:**

Suppose a Q-tensor has eigenvalues $\lambda_1, \lambda_2, \lambda_3$ and corresponding orthonormal eigenvectors $\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3$. Show that the maximum-entropy distribution constrained by this Q must be diagonal in the same eigenbasis.

**Solution:**

The entropy minimization problem with fixed Q can be written using a Lagrangian functional

$$
\mathcal{L}[\rho,\mathbf{\Lambda},\mu] = H[\rho] - \mu\left(\int_{S^2} \rho \, d\Omega - 1\right) - \mathbf{\Lambda} : \left( \int_{S^2} \left(\mathbf{n}\otimes\mathbf{n} - \tfrac{1}{3} \mathbf{I} \right) \rho(\mathbf{n}) \, d\Omega - \mathbf{Q} \right).
$$

Taking the variation with respect to $\rho$ gives the stationarity condition

$$
\delta \mathcal{L} = \int_{S^2} \left( \log \rho(\mathbf{n}) + 1 - \mu - \mathbf{\Lambda} : (\mathbf{n}\otimes\mathbf{n}) \right) \delta \rho(\mathbf{n}) \, d\Omega = 0.
$$

For all admissible $\delta\rho$, this yields

$$
\log \rho(\mathbf{n}) = \mu - 1 + \mathbf{\Lambda} : (\mathbf{n}\otimes\mathbf{n}).
$$

Exponentiating gives the exponential-family form

$$
\rho(\mathbf{n}) = \frac{1}{Z} \exp\left( \mathbf{\Lambda} : (\mathbf{n}\otimes\mathbf{n}) \right),
$$

with $Z$ chosen to normalize the density.

The moment constraint then relates $\mathbf{Q}$ to $\mathbf{\Lambda}$ through the average of $\mathbf{n}\otimes\mathbf{n}$ under $\rho$. Because $\mathbf{Q}$ and $\mathbf{\Lambda}$ are both symmetric, the resulting relation implies they commute: if they did not commute, the moment tensor produced by the exponential distribution would not be symmetric in the same basis as $\mathbf{Q}$.

A more direct way to see the shared eigenframe is to diagonalize $\mathbf{Q}$. Write

$$
\mathbf{Q} = \operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)
$$

in its eigenbasis, and assume $\mathbf{\Lambda}$ is also symmetric. The distribution can then be written as

$$
\rho(\mathbf{n}) = \frac{1}{Z} \exp\left( \mu_1 n_1^2 + \mu_2 n_2^2 + \mu_3 n_3^2 \right)
$$

with $\mathbf{\Lambda} = \operatorname{diag}(\mu_1,\mu_2,\mu_3)$ in that same basis. Because the constraint uses only second-moment components, the form of $\rho$ remains diagonal in the $\mathbf{Q}$ eigenframe.

That is, the optimal $\rho$ depends only on the squared projections $n_i^2$ onto the eigenvectors of $\mathbf{Q}$, and therefore the same orthogonal basis diagonalizes both the maximum-entropy distribution and $\mathbf{Q}$. The head-tail symmetry $\rho(-\mathbf{n}) = \rho(\mathbf{n})$ is automatic because the exponent involves only $n_i^2$.

## 5. Practice problems with solutions

### Practice Problem 1

**Problem:**

Let $\rho(\mathbf{n})$ be the normalized distribution on $S^2$ defined by

$$
\rho(\mathbf{n}) = \frac{1}{4\pi} \left( 1 + \alpha (\mathbf{n} \cdot \mathbf{e}_z)^2 \right),
$$

with $\alpha > -1$ so that $\rho$ remains nonnegative. Compute $\mathbf{Q}$ and determine whether it is uniaxial or biaxial.

**Solution:**

The given form is axisymmetric about $\mathbf{e}_z$, so the off-diagonal components of $\mathbf{Q}$ vanish and the $x$ and $y$ components are equal. This means $\mathbf{Q}$ has the form

$$
\mathbf{Q} = \operatorname{diag}(q,q,-2q)
$$

for some scalar $q$, making it uniaxial with symmetry axis $\mathbf{e}_z$.

First determine the normalization constant for $\rho$:

$$
Z = \int_{S^2} \left(1 + \alpha n_z^2\right) \, d\Omega = 4\pi\left(1 + \tfrac{\alpha}{3}\right).
$$

Then compute $q$ using the definition

$$
Q_{zz} = \int_{S^2} \left(n_z^2 - \tfrac{1}{3} \right) \rho(\mathbf{n}) \, d\Omega(\mathbf{n}).
$$

Because $\rho(\mathbf{n})$ is axisymmetric, the required integrals are standard:

- $\int_{S^2} n_z^2 \, d\Omega = \tfrac{4\pi}{3}$,
- $\int_{S^2} n_z^4 \, d\Omega = \tfrac{4\pi}{5}$.

Hence,

$$
Q_{zz} = \frac{1}{Z} \left( \frac{4\pi}{3} + \alpha \cdot \frac{4\pi}{5} \right) - \frac{1}{3}
= \frac{1}{1 + \alpha/3} \left( \frac{1}{3} + \frac{\alpha}{5} \right) - \frac{1}{3}.
$$

Similarly,

$$
Q_{xx} = Q_{yy} = \frac{1}{1 + \alpha/3} \left( \frac{1}{3} + \frac{\alpha}{15} \right) - \frac{1}{3}.
$$

These expressions satisfy $Q_{xx} + Q_{yy} + Q_{zz} = 0$ by construction, and because the $x$ and $y$ values are equal, $\mathbf{Q}$ is uniaxial.

The key point is that the distribution is elongated along $\mathbf{e}_z$, giving a larger second moment in the $z$ direction than in the transverse directions. The Q-tensor therefore has a single distinguished axis and two equal transverse eigenvalues, which is the defining signature of uniaxial order.

### Practice Problem 2

**Problem:**

Show that a uniform distribution $\rho(\mathbf{n}) = 1/(4\pi)$ gives $\mathbf{Q}=\mathbf{0}$.

**Solution:**

For the uniform distribution,

$$
\int_{S^2} \mathbf{n}\otimes\mathbf{n} \, d\Omega(\mathbf{n}) = \tfrac{1}{3} \mathbf{I}.
$$

Substituting into the definition of $\mathbf{Q}$ gives

$$
\mathbf{Q} = \tfrac{1}{3} \mathbf{I} - \tfrac{1}{3} \mathbf{I} = \mathbf{0}.
$$

This is the isotropic limit of nematic ordering.

### Practice Problem 3

**Problem:**

A Q-tensor has eigenvalues $(0.2, -0.1, -0.1)$ in an orthonormal basis. Describe the general form of the maximum-entropy distribution that produces this Q, and explain why the same basis diagonalizes both $\mathbf{Q}$ and the distribution.

**Solution:**

In the eigenbasis of $\mathbf{Q}$, the optimal distribution is

$$
\rho(\mathbf{n}) = \frac{1}{Z} \exp\left( \mu_1 n_1^2 + \mu_2 n_2^2 + \mu_3 n_3^2 \right)
$$

for some parameters $\mu_i$ determined by the eigenvalues. The distribution depends only on squared projections onto the eigenvectors, so it is invariant under $\mathbf{n} \mapsto -\mathbf{n}$ and is diagonal in the same basis as $\mathbf{Q}$. Thus the optimal $\rho$ and $\mathbf{Q}$ share the same orthogonal frame.

## 6. Calculus of variations and the Q-tensor

The Q-tensor theory is inherently variational because equilibrium states arise from minimizing a free energy over the space of admissible Q-fields.

### 6.1 Functional setting

We seek $\mathbf{Q}: \Omega \to \mathbb{R}^{3\times3}_{\text{sym},0}$ that minimizes

$$
\mathcal{F}[\mathbf{Q}] = \int_{\Omega} \left( f_B(\mathbf{Q}) + f_E(\mathbf{Q}, \nabla \mathbf{Q}) \right) dV.
$$

The admissible space is typically $H^1(\Omega;\mathbb{R}^{3\times3})$ with symmetry and traceless constraints, together with boundary conditions.

### 6.2 Euler–Lagrange equations

For the one-constant elastic energy, the variational derivative gives

$$
L \Delta Q_{ij} = \frac{\partial f_B}{\partial Q_{ij}},
$$

with $\Delta$ acting componentwise. For the standard bulk energy,

$$
\frac{\partial f_B}{\partial Q_{ij}} = A Q_{ij} - B Q_{ik} Q_{kj} + C \operatorname{tr}(Q^2) Q_{ij}.
$$

This yields the nonlinear elliptic system

$$
L \Delta Q_{ij} = A Q_{ij} - B Q_{ik}Q_{kj} + C \operatorname{tr}(Q^2) Q_{ij}.
$$

### 6.3 Defects and variational solutions

The Q-field can describe defects as regions where the energy concentrates and the tensor becomes degenerate. Because $\mathbf{Q}$ does not force a single director direction, it can represent defect cores without a singular vector field.

### 6.4 Entropy constraints in a variational framework

When the nematic state is derived from an underlying distribution, the variational problem can be viewed as a constrained minimization.

- The free energy depends on $\mathbf{Q}$,
- the distribution $\rho$ is chosen to minimize entropy subject to matching $\mathbf{Q}$,
- the optimal $\rho$ is aligned with the eigenframe of $\mathbf{Q}$.

This coupling of continuum energy and statistical entropy emphasizes that $\mathbf{Q}$ is the natural macroscopic variable for nematic liquid crystals.

## 7. Summary and study advice

- Use $\rho(\mathbf{n})$ on $S^2$ as the primitive description of nematic orientation.
- Define $\mathbf{Q}$ by the second moment relative to the isotropic background.
- Remember that $\mathbf{Q}$ is symmetric, traceless, and carries the same eigenframe as the minimum-entropy distribution.
- Practice relating specific distributions to their Q-tensors and computing eigenstructure.
- Think of the variational problem as minimizing bulk+elastic energy over Q, with the underlying distribution determined by entropy.

For deeper study, compare this Q-tensor approach with director-based theories, and examine how the maximum-entropy distribution changes when Q is biaxial versus uniaxial.
