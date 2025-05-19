# rey antonio boer perez, metodo simpson 1/3 

import numpy as np
from sympy import symbols, integrate, cos, exp

x = symbols('x')
fun1_sym = (1-x*cos(x**2))
fun2_sym = -x**2-(x/2) + 4
fun3_sym = exp(-x**2)

fun1 = lambda x: (1-x*cos(x**2))
fun2 = lambda x: -x**2-(x/2) + 4
fun3 = lambda x: np.exp(-x**2)

a = [1, 1, 1]
b = [2, 2,2]
funs = [fun1, fun2, fun3]

def simps1_3(f, a, b):
    x1 = (b-a)/2
    I = (b-a)*((f(a)+4*f(x1)+f(b))/6)
    return round(I, 4)


print('Valores analíticos:')
funs_sym = [fun1_sym, fun2_sym, fun3_sym]
for i, funcion in enumerate(funs_sym):
    integral_analitica = integrate(funcion, (x, a[i], b[i]))
    print(f'La integral analítica de la función {i + 1} es: {integral_analitica}')

print('\n*** Valores Simpson *********')
for i in range(len(a)):
    integral_simpson = simps1_3(funs[i], a[i], b[i])
    print(f'La integral de la función {i + 1} con Simpson 1/3 es: {integral_simpson}')
    
     
