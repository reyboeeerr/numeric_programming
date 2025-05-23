import numpy as np
import matplotlib.pyplot as plt

valores_x = np.array([1, 2, 3, 5, 7])
valores_y = np.array([3, 6, 19, 99, 291])

def coeffs(x, y):
    n = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j - 1:n - 1]) / (x[j:n] - x[0:n - j])
    return coef

def eval(x_eval, x_data, coef):
    n = len(coef)
    result = coef[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x_eval - x_data[i]) + coef[i]
    return result

coef = coeffs(valores_x, valores_y)
x_estimar = 4
f4 = eval(x_estimar, valores_x, coef)
print(f"f(4) estimado (Newton grado 4): {f4}")

x_line = np.linspace(1, 7, 300)
y_line = [eval(x, valores_x, coef) for x in x_line]

plt.plot(valores_x, valores_y, 'o', label='Datos usados')
plt.plot(x_line, y_line, label='Interpolación Newton grado 4', color='purple')
plt.plot(x_estimar, f4, 'ro', label='f(4) estimado')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación de Newton (grado 4)')
plt.legend()
plt.show()
