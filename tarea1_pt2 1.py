#rey antonio boer perez

import numpy as np

def multiplos_columna(N): 
    if not isinstance(N, int) or N <= 0:
        return "error, tiene que ser positivo y entero. "

    vector = np.random.randint(1, 10, N)

    matriz_crear = np.zeros((N, N), dtype=int)
    for i in range(N):
        for j in range(N):
            matriz_crear[i, j] = vector[j] * (i + 1)

    return matriz_crear

#N = int(input("introduce un numero: "))
N=8
resultado = multiplos_columna(N) 
print(resultado)