import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: np.cos(x/2)-np.sin(2*x)

xr = -2.1913
a = 3
b = 3.5

n_i = 5

for i in range(1,n_i+1):
    av = a
    bv = b
    xi = (a+b)/2
    fa = fx(a)
    fb = fx(b)
    fxi = fx(xi)
    if fa*fxi < 0:
        b=xi
    else:
        a=xi
        
    error= np.abs((xr-xi)/xr)*100

    print('============================================================================\n')
    print(f' i = {i}  |  a = {av}  |  b = {bv}  |    xi = {xi}   |  error = {error} %  ')
    
x = np.linspace(-5,5,100)
plt.plot(x, fx(x), color = 'green')
plt.plot(xi,fx(xi), color = 'red', marker = 'o')
plt.grid()
plt.show()