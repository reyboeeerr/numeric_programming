import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv")

X = df['Experience Years']
Y = df['Salary']

a1 = ((X * Y).sum() - X.sum() * Y.sum() / len(X)) / ((X**2).sum() - (X.sum()**2) / len(X))
a0 = Y.mean() - a1 * X.mean()

print(f"Pendiente (a1): {a1}")
print(f"Ordenada al origen (a0): {a0}\n")

def estimar_salario(experiencia):
    return a0 + a1 * experiencia

print("Estimaciones de salario:")
for años in [15, 30, 50]:
    salario = estimar_salario(años)
    print(f"Con {años} años de experiencia se estima un salario de ${salario}")

x_linea = np.linspace(min(X), max(X), 100)
y_linea = estimar_salario(x_linea)

plt.plot(X, Y, 'o', label='Datos reales')
plt.plot(x_linea, y_linea, label='Línea de regresión', color='red')
plt.xlabel('Años de Experiencia')
plt.ylabel('Salario')
plt.title('Regresión Lineal: Salario vs Experiencia')
plt.grid(True)
plt.legend()
plt.show()

