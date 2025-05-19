import numpy as np
import matplotlib.pyplot as plt

def fx(x):
    return np.cos(x/2)-np.sin(2*x)

def fprix(x):
    return -np.sin(x/2)*(1/2)-2*np.cos(2*x)

ni = 5
xcero = 3.3

for i in range(ni):
    vf = xcero
    x_new = xcero-((fx(xcero))/(fprix(xcero)))
    xcero = x_new
    error = np.abs((x_new-vf )/x_new)*100
    print('-------------------------------------------------\n')
    print(f' i = {i+1}  |  x_i = {x_new}  |  error = {error} %')
    
x = np.linspace(-5,5,100)
plt.plot(x, fx(x), color = 'black')
plt.plot(x_new,fx(x_new), color = 'red', marker = 'o')
plt.grid()
plt.show()