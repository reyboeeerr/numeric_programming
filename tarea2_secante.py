import numpy as np
import matplotlib.pyplot as plt

xn = -0.3
xs1 = 0.5
ni = 5

fx = lambda x: 8*x*np.sin(x)*np.exp(-x)-1

for i in range(ni):
    vf = xn
    x_new = xn-(fx(xn)*(xs1-xn)/(fx(xs1)-fx(xn)))
    xs1 = xn
    xn = x_new
    error = np.abs((x_new-vf )/x_new)*100
    print('-------------------------------------------------------------------\n')
    print(f' i = {i+1}  |  x_i = {vf}  |  x_i+1 = {x_new}  |  error = {error} %')
    
x = np.linspace(-5,5,100)
plt.plot(x, fx(x), color = 'yellow')
plt.plot(x_new,fx(x_new), color = 'red', marker = 'o')
plt.grid()
plt.show()