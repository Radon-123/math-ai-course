# Integration by parts

## Definition
Integration by parts is a useful technique for manipulating integrals. Given $\int_\Omega v(\nabla \cdot F)$ we can use integration by parts to obtain the following alternative expression for our integral: 

$$\int_\Omega v(\nabla \cdot F) = -\int_\Omega (\nabla v) \cdot F + \int_{\partial \Omega} v (F \cdot n)$$

This identity relates a volume integral over the region $\Omega$ to a surface integral over its boundary $\partial \Omega$, and an additional integral over the region $\Omega$ where the gradient of $v$ is considered. It is especially helpful when the integrand is easier to differentiate than to integrate, and it is a fundamental tool in deriving weak formulations for differential equations. For the formula to hold, the functions involved are assumed to be sufficiently smooth and the domain must have a well-defined outward normal vector $n$ on its boundary.

## Example Weak form of Poisson's Equation
Consider Poisson's equation: $-\Delta u = f$ in $\Omega$ with boundary condition $u=0$ on $\partial \Omega$. To derive the weak form of this equation, we multiply both sides by a test function $v$ that vanishes on the boundary $\partial \Omega$ and integrate over the domain $\Omega$:    
$$\int_\Omega -\Delta u \cdot v = \int_\Omega f \cdot v$$
Applying integration by parts to the left-hand side, we get:
$$\int_\Omega -\Delta u \cdot v = \int_\Omega \nabla u \cdot \nabla v$$
Thus, the weak form of Poisson's equation can be expressed as:
$$\int_\Omega \nabla u \cdot \nabla v = \int_\Omega f \cdot v$$
This weak formulation is particularly useful for numerical methods such as the finite element method, where we seek to find an approximate solution $u$ in a suitable function space that satisfies this integral equation for all test functions $v$ in that space.

### Conculsion
In all, integration by parts is a useful technique for evaluating integrals and deriving the weak form of diffrent PDEs. This is why it is an important part of any mathemetians tool kit!