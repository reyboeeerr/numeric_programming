import numpy as np

a = np.array([[1,1,1],[1,2,5],[1,4,25]])
b = np.array([6,12,36])

a2 = np.array([[4,-2,1],[-2,4,-2],[1,-2,4]])
b2 = np.array([11,-16,17])

x = np.linalg.inv(a)
x2 = np.linalg.inv(a2)

fin = np.matmul(x, b)
fin2 = np.matmul(x2, b2)

print(f' inv_sistema1 =')
print(f' {x}             solucion = {fin}\n')
print(f' inv_sistema2 =')
print(f' {x2}            solucion2 = {fin2} \n')