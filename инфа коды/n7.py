#7
import numpy as np
import matplotlib.pyplot as plt
a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
d = (b ** 2) - (4*a* c)
x1 = 0
if d > 0:
  x1 = (b * (-1) + (d**(1/2))) / 2 * a
  x2 = (b * (-1) - (d**(1/2))) / 2 * a
  print('x1 = {0:.2f}'.format(x1))
  print('x2 = {0:.2f}'.format(x2))
  x = np.arange(-3, 3, 0.0025)
  y = ((a* x **2) + (b *x) + c)
  plt.title("График квадратичной функции")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.plot(x, y)
  plt.grid()
  plt.show()
elif d == 0:
  x0 = (b* (-1)) / (4* a *c)
  print('x0 = {0:.2f}'.format(x0))
  x = np.arange(-3, 3, 0.0025)
  y = ((a* x **2) + (b * x) + c)
  plt.title("график квадратичной функции")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.plot(x, y)
  plt.grid()
  plt.show()
else:
  print("нет корней")
