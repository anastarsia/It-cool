6
import matplotlib.pyplot as plt
import numpy as np
#Ввод
a = float(input("Введите a: "))
b = float(input("Введите b: "))
#Создание массива значений t от 0 до 2pi
t = np.linspace(0, 2*np.pi, 100)
#вычисление x и y координату у эллипса
if a>b:
  x = a * np.cos(t)
  y = b * np.sin(t)
else:
  x = b * np.cos(t)
  y = a * np.sin(t)
#создание графика
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Эллипс с полуосями a и b')
plt.grid(True)
plt.axis('equal')
plt.show()
