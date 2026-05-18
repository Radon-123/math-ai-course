# Power Series

Power series are a useful, alternative representation of differentiable functions. Let $f(x)$ be a analytic function, then we can expand this function as an infinite series as follows:

$$ f(x) = \sum_{n=0}^\infty C_n(x-a)^n = C_0 +C_1(x-a)+\dots+C_N(x-a)^N+\dots$$

Here $C_n$ are the series coefficients and $a$ is the center of the power series.

## Convergence
Although powerful, representing a function as an infinite series has a big drawback: convergence! Although its easy to write down a function as a series, special care needs to be taken to study where the series repersentation holds. In general, given a power series where $a=0$, if $\{|C_n|^\frac{1}{n}\}$ is a bounded sequence, then let $\rho=\limsup(|C_n|^\frac{1}{n})$. This value is directly related to $R$:
$$
R = 
\begin{cases} 
0 & \text{if } \rho=\infty \\
\frac{1}{\rho} & \text{if } 0 < \rho<\infty \\
\infty& \text{if } \rho = 0
\end{cases}
$$

 $R$ denotes the radius of convergence of the power series. $\forall x \in (-R,R)$ the power series representation for a function is guaranteed to absolutely converge. In contrast, $\forall x \in (-\infty,-R) \cup (R,\infty)$ the series representation fails to converge. At $|x|=R$, the series can either diverge or converge. 
 
 The below video showcases a power series approximation for $f(x)=arctan(x)$ which converges on $[-1,1]$. As the video details, when we add more terms in the series expansion, the approximation (the blue line) serves as a better and better approximation of the function over the interval of convergence. In contrast, outside the region of convergence, as more terms are added to the series, the approximation diverges away from the true behavior of $f(x)$



<div align="center">
 <video src="Powa.mp4" width="600" controls></video> 
 </div>

## Applications
On top of serving as efficient approximations for smooth functions, Power Series are useful tools for solving difficult Differential Equations.

### Solving Difficult ODEs
For instance, the Legendre Differential Equation $(1-x^2)y^{''}-2xy^{'}+\alpha(\alpha+1)y=0$, comes up in many different physical applications where spherical symmetry is at play (Quantum dynamics and Electrodynamics). This Ordinary Differential Equation can be solved by assuming the solution takes the form $y =\sum_{n=0}^\infty C_n x^n$, we can find a set of polynomials that satisfy the above Ordinary Differential Equation.


### Defining New Functions
Entirely new functions can be defined in terms of power series. Similar to the above section, another Ordinary Differential Equation that occurs frequently in science is Bessels Equation: $x^2y^{''}+xy^{'}+(x^2-\nu^2)y=0$. This differential equation comes up in many engineering applications when working in curvilinear coordinates. Just like with Legendre's Differential Equation, if we assume the solution takes the form $y =\sum_{n=0}^\infty C_n x^n$ and impose Bessel's equation, we get an entirely new function that is defined as a power series:

$$J_\nu (x) = \sum_{n=0}^\infty  \frac{(-1)^n}{n!\Gamma(1+\nu+n)}\left( \frac{x}{2} \right)^{2n+\nu} $$