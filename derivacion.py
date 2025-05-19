# rey antonio boer perez, derivacion numerica

import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: 1-x*np.cos(x**2)
h = [0.2, 0.1]
xi = 1.8

def derivada_adelante(fx, xi, h):
    fxim1 = fx(xi+h)
    fxim2 = fx(xi+2*h)
    return (-fxim2+4*fxim1-3*fx(xi))/(2*h)

def derivada_atras(fx, xi, h):
    fxim1 = fx(xi-h)
    fxim2 = fx(xi-2*h)
    return (3*fx(xi)-4*fxim1+fxim2)/(2*h)

def derivada_centrada(fx, xi, h):
    fxip1 = fx(xi+h)
    fxip2 = fx(xi+2*h)
    fxim1 = fx(xi-h)
    fxim2 = fx(xi-2*h)
    return (-fxip2+8*fxip1-8*fxim1+fxim2)/(12*h)

""" profe, me aparecia que derivative ya no estaba disponble en scipy, asi que investigue como hacer
 la derivada de otra forma y encontre este metodo de aproximaciones finitas """
 
def derivada(fx, xi, h):
    return (fx(xi+h)-fx(xi-h))/(2*h)

def graficar_tangente(fx, xi, h):
    pendiente = derivada(fx, xi, h[0])
    recta_tangente = lambda x: pendiente*(x-xi)+fx(xi) 
    
    x = np.linspace(xi-2, xi+2, 100)
    plt.plot(x, fx(x), label='f(x)')
    plt.plot(x, recta_tangente(x), '--', label=f'Tangente en x={xi}')
    plt.scatter(xi, fx(xi), color='purple', label=f'Punto ({xi}, f({xi}))')
    plt.axhline(0, color='black')
    plt.title(f'Recta tangente en el punto x={xi}')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

print('*********** Valores analíticos **************\n')
for h_i in h:
    print(f'La derivada con diferencias finitas en x={xi} y h={h_i} es: {derivada(fx, xi, h_i)}')

print('\n*********** Valores numéricos **************\n')
for h_i in h:
    print(f'La derivada hacia adelante con h={h_i} es: {derivada_adelante(fx, xi, h_i)}')
    print(f'La derivada hacia atrás con h={h_i} es: {derivada_atras(fx, xi, h_i)}')
    print(f'La derivada centrada con h={h_i} es: {derivada_centrada(fx, xi, h_i)}')

graficar_tangente(fx, xi, h)