# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
#Defining the target function (a square wave)
x = np.linspace(0, 2 * np.pi, 500)
y = np.sign(np.sin(x))

# %%
#Computing the nth partial sum of its fourier series
def fourier_series(n, x):
    sum = np.zeros_like(x)
    for k in range(1, n + 1):
        sum += (1 / (2 * k - 1)) * np.sin((2 * k - 1) * x)
    return (4 / np.pi) * sum

# %%
#Plotting the target function and the fourier series approximation for N = 1,3,5,10
plt.figure(figsize=(12, 8))
plt.plot(x, y, label="Target Function")
plt.plot(x, fourier_series(1, x), label="N=1")
plt.plot(x, fourier_series(3, x), label="N=3")
plt.plot(x, fourier_series(5, x), label="N=5")
plt.plot(x, fourier_series(10, x), label="N=10")
plt.legend()
plt.title("Fourier Series Approximation of a Square Wave")
plt.show()

# %%
#Plotting the L2 error between the target function and the fourier series approximation as a function of N
N_values = np.arange(1, 21)
errors = []
for N in N_values:
    approximation = fourier_series(N, x)
    error = np.sqrt(np.mean((y - approximation) ** 2))
    errors.append(error)

plt.figure(figsize=(12, 8))
plt.plot(N_values, errors, 'o-')
plt.xlabel("N")
plt.ylabel("L2 Error")
plt.title("Convergence of Fourier Series Approximation")
plt.show()


# %%
