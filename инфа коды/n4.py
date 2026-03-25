#4
import matplotlib.pyplot as plt
from math import cos, sin, pi
 
a = float(input("Введите a: "))
b = float(input("Введите b: "))
alpha = float(input("Введите alpha (в градусах): ")) * (pi / 180)
 
x = [0, b * cos(alpha), a + b * cos(alpha), a, 0]
y = [0, b * sin(alpha), b * sin(alpha), 0, 0]
 
plt.plot(x, y)
plt.fill(x, y, alpha=0.5)
plt.axis('equal')
plt.title("Параллелограмм")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()
