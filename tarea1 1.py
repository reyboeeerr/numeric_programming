#rey antonio boer perez

import numpy as np

def multiplos_fila(N): 
    if not isinstance(N, int) or N <= 0:
        return "error, tiene que ser positivo y entero. "

    vector = np.random.randint(1, 10, N)

    matriz_crear = np.zeros((N, N), dtype=int)
    for i in range(N):
        for j in range(N):
            matriz_crear[i, j] = vector[i] * (j + 1)

    return matriz_crear

#N = int(input("introduce un numero: "))
N=5
resultado = multiplos_fila(N) 
print(resultado)