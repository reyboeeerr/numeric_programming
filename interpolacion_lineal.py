import numpy as np
import matplotlib.pyplot as plt

x1, x2 = 3, 5
y1, y2 = 19, 99

def interpolacion_lineal(x):
    return y1 + ((y2 - y1) / (x2 - x1)) * (x - x1)

x_estimar = 4
f4 = interpolacion_lineal(x_estimar)
print(f"f(4) estimado (lineal): {f4}")

x_vals = np.array([x1, x2])
y_vals = np.array([y1, y2])
x_line = np.linspace(2.5, 5.5, 100)
y_line = interpolacion_lineal(x_line)

plt.plot(x_vals, y_vals, 'o', label='Datos usados')
plt.plot(x_line, y_line, label='Interpolación lineal', color='yellow')
plt.plot(x_estimar, f4, 'ro', label='f(4) estimado')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación Lineal')
plt.legend()
plt.show()
