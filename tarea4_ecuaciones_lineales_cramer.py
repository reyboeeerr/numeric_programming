import numpy as np

a = np.array([[1,1,1],[1,2,5],[1,4,25]])
b = np.array([6,12,36])

a2 = np.array([[4,-2,1],[-2,4,-2],[1,-2,4]])
b2 = np.array([11,-16,17])
 
 
dg = np.linalg.det(a)
dg2 = np.linalg.det(a2)
 
dx =  np.linalg.det(np.array([[6,1,1],[12,2,5],[36,4,25]]))
dx2 = np.linalg.det(np.array([[11,-2,1],[-16,4,-2],[17,-2,4]])) 
dy = np.linalg.det(np.array([[1,6,1],[1,12,5],[1,36,25]]))
dy2 = np.linalg.det(np.array([[4,11,1],[-2,-16,-2],[1,17,4]]))
 
dz = np.linalg.det(np.array([[1,1,6],[1,2,12],[1,4,36]]))
dz2 = np.linalg.det(np.array([[4,-2,11],[-2,4,-16],[1,-2,17]]))
 
x = dx/dg
y = dy/dg
z = dz/dg
 
x2 = dx2/dg2
y2 = dy2/dg2
z2 = dz2/dg2
 
print(f' det general1 = {dg}    |    det x = {dx}    |    det y = {dy}    |    det z = {dz}                  |    solucion: x = {x}, y = {y}, z = {z}')
print(f' det general2 = {dg2}    |    det x2 = {dx2}   |    det y2 = {dy2}                |    det z2 = {dz2}   |    solucion2: x = {x2}, y = {y2}, z = {z2}')