import numpy as np

A = np.array([[1, -0.1, -0.2],[0.1, 7, -0.3], [0.3, -0.2, -10]])
b = np.array([7.85, 19.3, 71.4])

x = np.zeros(len(b))
n_iter = 5

for k in range(1, n_iter + 1):
    x_anterior = x 
    for i in range(len(b)):
        suma = sum(A[i, j] * x[j] for j in range(len(b)) if j != i)
        x[i] = (b[i] - suma) / A[i, i]
    
    print(f'I = {k}: x1={x[0]:.4f}, x2={x[1]:.4f}, x3={x[2]:.4f}')

print('\nResultado final (aproximación):')
print(f"x1 = {x[0]:.4f}, x2 = {x[1]:.4f}, x3 = {x[2]:.4f}")