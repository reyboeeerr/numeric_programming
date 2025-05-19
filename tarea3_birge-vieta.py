import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, -5, 5, -1])
xcero = 0.8
b = np.empty(len(a))
c = np.empty(len(a)) 

iteraciones = 10

n = len(a)

for i in range(1, iteraciones+1):
    for j in range(n):
        if j==0:
            b[j] = a[j]
            c[j] = a[j]
        else:
            b[j] = a[j]+xcero*b[j-1]
            c[j] = b[j]+xcero*c[j-1]
        xceroviejo = xcero
    xcero = xcero - (b[n-1]/c[n-2])
    print(f'\n Iteracion: {i}')
    print(f'xi = {xceroviejo}')
    print(b)
    print(c)