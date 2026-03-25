import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

X0 = np.array ([0, 1.3, 2.6, 4.0])
Y0 = np.array ([0, 1.14, 1.61, 2.0])

f = interp1d(X0,Y0, kind = 'linear')
x = np.arange(0,4,0.01)
y = f(x)
n = float(input())

print('Значение функции в точке', f(n))

plt.figure(1)
plt.plot(X0,Y0, 'ro', label = 'Заданные точки')
plt.plot(x,y, label = 'Интерполяционная функция')
plt.grid()
plt.legend()
plt.show(block = False)
