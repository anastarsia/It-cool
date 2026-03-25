#1
import matplotlib.pyplot as plt
import numpy as np

# Ввод параметров
a = float(input("Введите длину катета a: "))
c = float(input("Введите длину гипотенузы c: "))

# Проверка корректности
if c <= a:
    print("Гипотенуза должна быть больше катета.")
else:
    # Вычисление второго катета b с помощью теоремы Пифагора
    b = (c**2 - a**2)**0.5


# Координаты вершин треугольника
triangle_points = np.array([[0, 0], [a, 0], [0, b], [0, 0]])


 # Построение треугольника
plt.fill(triangle_points[:, 0], triangle_points[:, 1])


# Настройки графика
plt.xlim(-1, a + 1)
plt.ylim(-1, b + 1)
plt.title('Прямоугольный треугольник')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

plt.show()
