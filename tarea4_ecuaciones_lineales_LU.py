import numpy as np

A = np.array([[1,1,-2],[0,1,3],[1,0,-1]])

L=np.zeros((3,3))
U=np.zeros((3,3))

L[0][0] = 1
L[1][1] = 1
L[2][2] = 1
U[0,:] = A[0,:]

L[1][0] = A[1][0]/U[0][0]
U[1][1] = A[1][1]-L[1][0]*U[0][1]
U[1][2] = A[1][2]-L[1][0]*U[0][2]
L[2][0] = A[2][0]/U[0][0]
L[2][1] = (A[2][1]-L[2][0]*U[0][1])/U[1][1]
U[2][2] = A[2][2]-L[2][0]*U[0][2]-L[2][1]*U[1][2]

x = np.matmul(L, U)

A2 = np.array([[4,-2,1],[-2,4,-2],[1,-2,4]])

L2=np.zeros((3,3))
U2=np.zeros((3,3))

L2[0][0] = 1
L2[1][1] = 1
L2[2][2] = 1
U2[0,:] = A2[0,:]

L2[1][0] = A2[1][0]/U2[0][0]
U2[1][1] = A2[1][1]-L2[1][0]*U2[0][1]
U2[1][2] = A2[1][2]-L2[1][0]*U2[0][2]
L2[2][0] = A2[2][0]/U2[0][0]
L2[2][1] = (A2[2][1]-L2[2][0]*U2[0][1])/U2[1][1]
U2[2][2] = A2[2][2]-L2[2][0]*U2[0][2]-L2[2][1]*U2[1][2]

x2 = np.matmul(L2, U2)

print(f' triangular inferior 1: \n {L}\n')
print(f' triangular superior 1: \n {U}\n')
print(f' solucion 1 = \n{x}\n')

print(f' triangular inferior 2: \n {L2}\n')
print(f' triangular superior 2: \n {U2}\n')
print(f' solucion 2 = \n{x2}\n')
