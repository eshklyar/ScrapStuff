import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = x**3 - 6*x**2 + 11*x - 6

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Cubic Polynomial: f(x) = x^3 - 6x^2 + 11x - 6')
plt.grid(True)
plt.show()