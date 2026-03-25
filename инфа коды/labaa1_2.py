import numpy as np
import matplotlib.pyplot as plt

X0 = np.array ([0, 1.3, 2.6, 4.0])
Y0 = np.array ([0, 1.14, 1.61, 2.0])
x = float(input())
for k in range(0,len(X0)):
    if X0[k] <= x and X0[k+1] >= x:
        y = (Y0[k+1]-Y0[k])/(X0[k+1]-X0[k])*(x-X0[k])+Y0[k]
        
print('Значение функции в точке', y)
plt.figure(1)
plt.plot(X0,Y0, 'ro', label = 'Заданные точки')
plt.plot(x,y, 'ro', color = 'g', label = 'Точка, введенная с клавиатуры')
plt.plot(X0,Y0, label = 'Интерполяционная функция')
plt.grid()
plt.legend()
plt.show(block = False)
