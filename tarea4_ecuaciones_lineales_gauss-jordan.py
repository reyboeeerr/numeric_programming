import numpy as np

a = np.array([[1,1,1],[1,2,5],[1,4,25]])
b = np.array([6,12,36])
x = np.linalg.solve(a, b)

a2 = np.array([[4,-2,1],[-2,4,-2],[1,-2,4]])
b2 = np.array([11,-16,17])
x2 = np.linalg.solve(a2, b2)

print(f' sistema1 = {x} \n')
print(f' sistema2 = {x2} \n')