import numpy as np
import matplotlib.pyplot as plt

valores_x = np.array([2, 3, 5])
valores_y = np.array([6, 19, 99])

def interpocuad(x, x_vals, y_vals):
    total = 0
    n = len(x_vals)
    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if i != j:
                term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        total += term
    return total

x_estimar = 4
f4 = interpocuad(x_estimar, valores_x, valores_y)
print(f"f(4) estimado (cuadrática): {f4}")

f4_lineal = 59.0
error_relativo = abs((f4 - f4_lineal) / f4_lineal) * 100
print(f"Error relativo con respecto a la estimación lineal: {error_relativo}%")

x_line = np.linspace(2, 5, 200)
y_line = [interpocuad(x, valores_x, valores_y) for x in x_line]

plt.plot(valores_x, valores_y, 'o', label='Datos usados')
plt.plot(x_line, y_line, label='Interpolación cuadrática', color='yellow')
plt.plot(x_estimar, f4, 'ro', label='f(4) estimado')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación Cuadrática')
plt.legend()
plt.show()
