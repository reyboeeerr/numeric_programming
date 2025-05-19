import numpy as np

A = np.array([[1,1,-2],[0,1,3],[1,0,-1]])
b = np.array([-2,7,-1])

def er(vr, vn):
    return abs((vr - vn) / vr) * 100

x1_v, x2_v, x3_v = 0, 0, 0
n_iter = 3

for k in range(1, n_iter + 1):
    x1 = (-A[0, 1] * x2_v - A[0, 2] * x3_v + b[0]) / A[0, 0]
    x2 = (-A[1, 0] * x1_v - A[1, 2] * x3_v + b[1]) / A[1, 1]
    x3 = (-A[2, 0] * x1_v - A[2, 1] * x2_v + b[2]) / A[2, 2]

    print(f'i={k}   |    x1={x1:.4f}   |    x2={x2:.4f}   |   x3={x3:.4f}\n')
    print(f'error x1={er(x1, x1_v):.4f}    |     error x2={er(x2, x2_v):.4f}     |     error x3={er(x3, x3_v):.4f}\n')
    
    x1_v, x2_v, x3_v = x1, x2, x3