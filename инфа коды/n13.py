#13
import numpy as np
import matplotlib.pyplot as plt


# Генерируем массив m
m = np.random.randint(1, 100, size=20)  # Массив из 20 случайных чисел от 1 до 100
print("Массив m:", m)


# Находим элементы, кратные трём
elements = m[m % 3 == 0]


# Рассчитываем среднее арифметическое
if len(elements) > 0:
    average = np.mean(elements)
    print("Среднее арифметическое элементов, кратных трём:", average)
else:
    average = None
    print("Нет элементов, кратных трём.")


# Строим график
plt.figure(figsize=(10, 6))
plt.plot(m, marker='o', label='Элементы массива m')


# Выделяем элементы, кратные трём
for i, value in enumerate(m):
    if value % 3 == 0:
        plt.scatter(i, value, color='red', s=100, label='Кратные трём' if i == 0 else "")
       
plt.title('График элементов массива m')
plt.xlabel('Номер элемента массива (k)')
plt.ylabel('Значение элемента M(k)')
plt.legend()
plt.grid()
plt.show()
