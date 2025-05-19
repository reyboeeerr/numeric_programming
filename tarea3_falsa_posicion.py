import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: 2*x*np.cos(2*x)-(x+1)**2

xr = -2.1913
a = -3
b = -2

n_i = 5

for i in range(1,n_i+1):
    av = a
    bv = b
    fa = fx(a)
    fb = fx(b)
    xi = b - ((fb*(a-b))/(fa-fb))
    fxi = fx(xi)
    if fa*fxi < 0:
        b=xi
    else:
        a=xi
        
    error= np.abs((xr-xi)/xr)*100

    print('=================================================================================================================\n')
    print(f' i = {i}  |  a = {av}  |  b = {bv}  |  f(a) = {fa}  |  f(b) = {fb}  |   f(xi) = {fxi}   |  error = {error} %  ')
    
x = np.linspace(-5,5,100)
plt.plot(x, fx(x), color = 'yellow')
plt.plot(xi,fx(xi), color = 'red', marker = '*')
plt.grid()
plt.show()