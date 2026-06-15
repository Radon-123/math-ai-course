# Interesting 2D Potentials for the Time-Dependent Schrödinger Equation

## 1. Physical intuition behind interesting 2D potentials

In two dimensions, the time-dependent Schrödinger equation (TDSE) describes how a quantum particle moves across a plane. The potential energy landscape $V(x,y)$ controls the regions where the particle is likely to be found, how it scatters, and whether it becomes localized or spreads out.

- A smooth well traps the particle in a region, like a quantum bowl containing electrons in a 2D semiconductor.
- A barrier forms a dividing ridge that can reflect or transmit the wave packet, similar to tunneling through a membrane or a potential step in a quantum dot device.
- Periodic potentials generate band structure and diffraction, analogous to electrons moving through a crystal lattice in two dimensions.
- A rotating or anisotropic potential can model quantum vortices, angular momentum coupling, or confinement with preferred axes.

Physically, these potentials are useful for modeling:
- electrons in 2D materials like graphene or quantum wells,
- atomic Bose-Einstein condensates in pancake-shaped traps,
- quantum billiards and microwave resonator analogs,
- nanoscale devices where motion in one plane dominates.


## 2. Mathematical definitions of interesting 2D potentials

The TDSE in 2D is

$$
 i\hbar \frac{\partial \Psi(x,y,t)}{\partial t} = -\frac{\hbar^2}{2m} \left( \frac{\partial^2 \Psi}{\partial x^2} + \frac{\partial^2 \Psi}{\partial y^2} \right) + V(x,y)\Psi(x,y,t).
$$

Common potentials to explore include:

1. **2D isotropic harmonic oscillator**
   $$V(x,y) = \frac{1}{2} m \omega^2 (x^2 + y^2).$$

2. **2D anisotropic harmonic oscillator**
   $$V(x,y) = \frac{1}{2} m (\omega_x^2 x^2 + \omega_y^2 y^2).$$

3. **2D infinite square well**
   $$V(x,y) = \begin{cases}0, & 0 < x < L_x,\ 0 < y < L_y, \\ \infty, & \text{otherwise.}\ \end{cases}$$

4. **2D potential barrier or step**
   $$V(x,y) = V_0 \Theta(x - a),$$
   where $\Theta$ is the Heaviside step, modeling a sharp ridge at $x=a$.

5. **2D Gaussian well/barrier**
   $$V(x,y) = V_0 \exp\left(-\frac{(x-x_0)^2 + (y-y_0)^2}{2\sigma^2}\right).$$

6. **2D periodic lattice potential**
   $$V(x,y) = V_0 [\cos(k_x x) + \cos(k_y y)].$$

7. **2D ring or radial trap**
   $$V(r) = \frac{1}{2} m \omega^2 (r - r_0)^2, \qquad r = \sqrt{x^2 + y^2}.$$ 

Each potential highlights a different physical regime: confinement, tunneling, periodic structure, or rotational symmetry.


## 3. Worked examples linking the mathematics to physics

### Example 1: Gaussian barrier and wave packet scattering

**Problem:** A Gaussian wave packet is incident on a 2D Gaussian barrier in the $x$ direction:

$$V(x,y) = V_0 \exp\left(-\frac{x^2 + y^2}{2\sigma^2}\right).$$

**Physical intuition:** This models a localized obstacle in the plane. A wave packet coming from the left can partially transmit, reflect, or diffract around the barrier.

**Solution outline:**

1. Start with a wave packet centered at $(x_0,y_0)$ with momentum $\mathbf{p}_0 = (p_{x0},0)$:
   $$\Psi(x,y,0) = A \exp\left(-\frac{(x-x_0)^2 + (y-y_0)^2}{4\sigma_0^2} + \frac{i p_{x0} x}{\hbar}\right).$$

2. The TDSE evolves the packet under the kinetic and potential terms. For short time, use the split-step approximation:
   - First apply half the potential phase: $\Psi \to \Psi \exp\left(-\frac{i}{\hbar} \frac{\Delta t}{2} V(x,y)\right)$.
   - Then apply kinetic evolution in Fourier space.
   - Finally apply the remaining potential phase.

3. As the packet approaches the barrier, the amplitude in the high-potential region decreases and the phase accumulates.

4. If $V_0$ is comparable to the packet energy $E = p_{x0}^2/(2m)$, the packet partially reflects and partially transmits.

**Key math physics connection:** The exponential phase factor from the potential is

$$\exp\left(-\frac{iV_0 \Delta t}{2\hbar} e^{-\frac{x^2+y^2}{2\sigma^2}}\right),$$

which shows how the barrier locally distorts the phase. Spatially varying phase becomes momentum-space scattering, leading to diffraction and reflection.

### Example 2: 2D anisotropic harmonic oscillator and separated motion

**Problem:** Solve the stationary states for the 2D anisotropic harmonic oscillator

$$V(x,y) = \frac{1}{2} m (\omega_x^2 x^2 + \omega_y^2 y^2)$$

and interpret the result physically.

**Physical intuition:** This describes a particle confined more strongly in one direction than the other, like an elliptical quantum dot or a particle in a rectangular trap with different stiffness along each axis.

**Solution steps:**

1. Separate variables by assuming $\Psi(x,y,t) = \psi_x(x) \psi_y(y) e^{-iEt/\hbar}.$

2. The time-independent Schrödinger equation becomes two 1D harmonic oscillators:

   $$-\frac{\hbar^2}{2m} \psi_x'' + \frac{1}{2}m\omega_x^2 x^2 \psi_x = E_x \psi_x,$$

   $$-\frac{\hbar^2}{2m} \psi_y'' + \frac{1}{2}m\omega_y^2 y^2 \psi_y = E_y \psi_y,$$

   with $E = E_x + E_y$.

3. Solutions are Hermite-Gauss functions:

   $$\psi_{n_x}(x) = N_{n_x} H_{n_x}\left(\sqrt{\frac{m\omega_x}{\hbar}} x\right) e^{-m\omega_x x^2/(2\hbar)},$$

   $$\psi_{n_y}(y) = N_{n_y} H_{n_y}\left(\sqrt{\frac{m\omega_y}{\hbar}} y\right) e^{-m\omega_y y^2/(2\hbar)}.$$

4. The energy eigenvalues are

   $$E_{n_x,n_y} = \hbar\omega_x \left(n_x + \tfrac12\right) + \hbar\omega_y \left(n_y + \tfrac12\right).$$

**Why this matters physically:** The particle behaves like two independent oscillators, one in $x$ and one in $y$. The difference between $\omega_x$ and $\omega_y$ gives an anisotropic energy spacing, which is directly measurable in spectroscopy or in the mode structure of a trapped condensate.

### Example 3: 2D periodic cosine potential and band-like behavior

**Problem:** Consider the periodic potential

$$V(x,y) = V_0 [\cos(k x) + \cos(k y)].$$

**Physical intuition:** This is a simple model of a 2D crystal lattice potential. A particle moving in this potential can experience constructive and destructive interference from lattice periodicity, producing Bloch waves.

**Solution outline:**

1. In a periodic potential, eigenstates are Bloch states:
   $$\Psi_{\mathbf{k}}(x,y) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{\mathbf{k}}(x,y),$$
   where $u_{\mathbf{k}}$ has the same periodicity as the lattice.

2. Expand $u_{\mathbf{k}}$ as a Fourier series in lattice wavevectors $\mathbf{G} = (n_x k, n_y k)$.

3. The Schrödinger equation becomes a matrix equation for Fourier coefficients. The periodic cosine terms couple plane waves separated by $\pm k$ in each direction.

4. At the Brillouin zone boundary, the coupling opens gaps, showing that energy eigenvalues are not continuous but split into bands. Physically, this is the origin of allowed bands and forbidden gaps for electrons in a 2D crystal.

**Takeaway:** A 2D periodic potential encodes a generalized version of the Kronig-Penney model. It helps connect TDSE behavior to band theory, where the dispersion relation depends on both $k_x$ and $k_y$.


## 4. Other interesting applications and connections

- **Quantum billiards:** Use hard-wall 2D wells or stadium-shaped potentials to study classical chaos vs. quantum eigenstate statistics.
- **Graphene-like Dirac physics:** Near a honeycomb lattice potential, low-energy states can behave like massless Dirac particles in 2D.
- **Magnetic traps and vortices:** Combine 2D harmonic confinement with rotation to model vortex lattices in atomic BECs.
- **Quantum dots:** Anisotropic oscillator potentials approximate electron confinement in semiconductor quantum dots and explain discrete optical transitions.
- **Surface adsorption:** Localized Gaussian wells model electrons bound to surface defects or adatoms in 2D materials.
- **Tunneling and resonance:** A potential barrier in 2D can show resonance transmission and wave packet splitting, useful for quantum transport and mesoscopic devices.

These applications link directly to classical mechanics concepts such as separable systems, resonance, and stability, as well as to electromagnetic wave propagation in periodic media.


## 5. Practice problems with solutions

### Problem 1: 2D circular well ground state

**Task:** For a particle of mass $m$ in a circular infinite well of radius $R$:

$$V(r) = \begin{cases}0, & r < R, \\ \infty, & r \ge R, \end{cases}$$

find the ground-state energy and the form of the radial wavefunction.

**Solution:**

1. In polar coordinates, separation gives $\Psi(r,\theta) = R(r) e^{im\theta}.$
2. The radial equation is
   $$\frac{1}{r} \frac{d}{dr} \left(r \frac{dR}{dr} \right) + \left( \frac{2mE}{\hbar^2} - \frac{m^2}{r^2} \right)R = 0.$$
3. For the ground state $m=0$, the solution is a Bessel function: $R(r) = A J_0(kr)$ with $k = \sqrt{2mE}/\hbar.$
4. Boundary condition $R(R)=0$ gives the first zero of $J_0$, call it $\alpha_{0,1} \approx 2.4048.$
5. Thus the ground-state energy is
   $$E = \frac{\hbar^2 \alpha_{0,1}^2}{2mR^2}.$$

### Problem 2: 2D anisotropic oscillator energy splitting

**Task:** If $\omega_x = 2\omega_y$, compute the energies of the first four lowest states and describe how eigenstates group.

**Solution:**

1. Energies are $E_{n_x,n_y} = \hbar\omega_x(n_x+\tfrac12) + \hbar\omega_y(n_y+\tfrac12).$
2. Substitute $\omega_x = 2\omega_y$:
   - $E_{0,0} = \tfrac{5}{2} \hbar \omega_y$.
   - $E_{1,0} = \tfrac{9}{2} \hbar \omega_y$.
   - $E_{0,1} = \tfrac{7}{2} \hbar \omega_y$.
   - $E_{2,0} = \tfrac{13}{2} \hbar \omega_y$.
3. The first excited state is $(0,1)$, and the second is $(1,0)$, showing anisotropy lifts degeneracy present in the isotropic case.

### Problem 3: Gaussian barrier transmission estimate

**Task:** Estimate whether a Gaussian wave packet with energy $E$ will transmit through a Gaussian barrier with height $V_0 = 1.5 E$ and width $\sigma$.

**Solution:**

1. If $V_0 > E$, classically the particle cannot cross, but quantum-mechanically tunneling is possible.
2. In 1D, the WKB approximate transmission through a barrier of width $d$ is
   $$T \approx \exp\left(-2 \int_{x_1}^{x_2} \frac{\sqrt{2m(V(x)-E)}}{\hbar} dx \right).$$
3. For a Gaussian barrier, the classically forbidden region satisfies $V(x,y) > E$, so the exponent is dominated by the region near the center.
4. This means transmission is small but nonzero, especially if $\sigma$ is comparable to the packet width and $V_0$ is only modestly larger than $E$.

**Interpretation:** The packet can still partially tunnel, and the transmitted component will be lower amplitude and broadened. The 2D structure also allows some spreading around the barrier edge.


## 6. Clarification check

Would you like me to build a specific 2D potential and show the full numerical split-step method for the TDSE? If you want, I can also compare these potentials with the 1D cases you already know.