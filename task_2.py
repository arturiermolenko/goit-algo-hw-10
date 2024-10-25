import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Визначення функції та межі інтегрування
def quadratic_function(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Монте-Карло
N = 10000
random_x = np.random.uniform(a, b, N)
random_y = np.random.uniform(0, quadratic_function(b), N)

# Точки під кривою
points_under_curve = random_y < quadratic_function(random_x)
monte_carlo_integral = (b - a) * quadratic_function(b) * np.sum(points_under_curve) / N

# Порівняння за допомогою функції SciPy quad
quad_result, quad_error = integrate.quad(quadratic_function, a, b)

x_vals = np.linspace(a, b, 400)
y_vals = quadratic_function(x_vals)

plt.plot(x_vals, y_vals, 'r', linewidth=2)
plt.fill_between(x_vals, y_vals, color='gray', alpha=0.3)
plt.scatter(random_x, random_y, c=points_under_curve, s=1, cmap='bwr', alpha=0.5)
plt.title(f"Monte Carlo: {monte_carlo_integral}\nSciPy Quad: {quad_result}")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()

print(f"Monte Carlo: {monte_carlo_integral}")
print(f"SciPy Quad: {quad_result}")
print(f"Difference: {abs(monte_carlo_integral - quad_result)}")