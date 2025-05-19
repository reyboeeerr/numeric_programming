# rey antonio boer perez, metodo simpson 6/8 

import numpy as np
from sympy import symbols, integrate, cos, exp
import matplotlib.pyplot as plt

x = symbols('x')
fun1_sym = 2*cos(2*x)
fun2_sym = -x**2-(x/2) + 4
fun3_sym = exp(-x**2)

fun1 = lambda x: 2*np.cos(2*x)
fun2 = lambda x: -x**2-(x/2) + 4
fun3 = lambda x: np.exp(-x**2)

a = [0, 0.5, 0]
b = [np.pi/4, 1.5,1]
funs = [fun1, fun2, fun3]

def simps1_3(f, a, b):
    x1 = (a+b)/3
    x2 = a+2*x1
    I = (b-a)*((f(a)+3*f(x1)+3*f(x2)+f(b))/8)
    return round(I, 4)

def graficar_funcion_area1(fun1, a, b):
    x = np.linspace(a, b, 1000)
    y = fun1(x)
    plt.plot(x, y, label='f(x)')
    plt.fill_between(x, y, where=(y >= 0), color='lightgreen', alpha=0.5, label='area bajo la curva')
    plt.axhline(0, color='black')
    plt.title('area bajo la curva de f(x)1')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
    
def graficar_funcion_area2(fun2, a, b):
    x = np.linspace(a, b, 1000)
    y = fun2(x)
    plt.plot(x, y, label='f(x)')
    plt.fill_between(x, y, where=(y >= 0), color='lightgreen', alpha=0.5, label='area bajo la curva')
    plt.axhline(0, color='black')
    plt.title('area bajo la curva de f(x)2')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

def graficar_funcion_area3(fun3, a, b):
    x = np.linspace(a, b, 1000)
    y = fun3(x)
    plt.plot(x, y, label='f(x)')
    plt.fill_between(x, y, where=(y >= 0), color='lightgreen', alpha=0.5, label='area bajo la curva')
    plt.axhline(0, color='black')
    plt.title('area bajo la curva de f(x)3')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()


print('Valores analíticos:')
funs_sym = [fun1_sym, fun2_sym, fun3_sym]
for i, funcion in enumerate(funs_sym):
    integral_analitica = integrate(funcion, (x, a[i], b[i]))
    print(f'La integral analítica de la función {i + 1} es: {integral_analitica}')

print('\n*** Valores Simpson *********')
for i in range(len(a)):
    integral_simpson = simps1_3(funs[i], a[i], b[i])
    print(f'La integral de la función {i + 1} con Simpson 1/3 es: {integral_simpson}')
    
graficar_funcion_area1(fun1, -2, 2)
graficar_funcion_area2(fun2, -2, 2)
graficar_funcion_area3(fun3, -2, 2)