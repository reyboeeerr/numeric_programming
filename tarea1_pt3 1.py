#rey antonio boer perez

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(5,1,15)
y1 = x**3-2
y2 = 5*x+3*x**2
y3 = 3*x+12*x

plt.plot(x, y1, '--' , color = 'blue', label='x**3-2', marker='o')
plt.plot(x, y2, ':', color='red', label='5x+3x**2', marker='*')
plt.plot(x, y3, '-.', color='green', label ='3*x+12*x', marker='+')
plt.legend(loc='best')

plt.xlabel('eje x')
plt.ylabel('eje y')

plt.title('funciones, usando ecuaciones')
plt.grid()
plt.show()
