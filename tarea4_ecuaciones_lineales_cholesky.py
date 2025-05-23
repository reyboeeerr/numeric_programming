import numpy as np

A = np.array([[1, 1, 1],[1, 2, 5],[1, 5, 25]])

A2 = np.array([[4, -2, 1],[-2, 4, -2],[1, -2, 4]])

L = np.zeros((3, 3))

for i in range(3): 
    for j in range(i + 1):
        if i == j: 
            L[i, j] = np.sqrt(A[i, i] - sum(L[i, k] ** 2 for k in range(j)))
        else: 
            L[i, j] = (A[i, j] - sum(L[i, k] * L[j, k] for k in range(j))) / L[j, j]

A_chida = np.matmul(L, L.T)

L2 = np.zeros((3, 3))

for i in range(3): 
    for j in range(i + 1):
        if i == j:
            L2[i, j] = np.sqrt(A2[i, i] - sum(L2[i, k] ** 2 for k in range(j)))
        else:  
            L2[i, j] = (A2[i, j] - sum(L2[i, k] * L2[j, k] for k in range(j))) / L2[j, j]

A2_chida = np.matmul(L2, L2.T)

# Resultados
print(f'Primera matriz A:\n{A}')
print(f'Triangular inferior L (primera matriz):\n{L}')
print(f' A (L * L.T):\n{A_chida}\n')

print(f'Segunda matriz A2:\n{A2}')
print(f'Triangular inferior L2 (segunda matriz):\n{L2}')
print(f'A2 (L2 * L2.T):\n{A2_chida}\n')