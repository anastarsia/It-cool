import numpy as np
import matplotlib.pyplot as plt
def integr(x, y):
    "Вычисляет интеграл дискретного сигнала методом левых прямоугольников"
    res = 0
    for i in range(len(x) - 1):
        res += y[i] * (x[i + 1] - x[i])
    return res

def differ(x, y):
    "Вычисляет численную производную дискретного сигнала"
    res = np.zeros(len(x))
    for i in range(len(x) - 1):
        res[i] = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
    res[-1] = res[-2]  # чтобы график не обрывался
    return res

#Основной сигнал            # частота дискретизации, Гц
t_test = np.linspace(0, 10, 1000)
y_lin = 5 * t_test - 2
int_lin = integr(t_test, y_lin)
dy_lin = differ(t_test, y_lin)


plt.figure(figsize=(10, 5))
plt.plot(t_test, y_lin, label='U(t)')
plt.title("Исходный сигнал ")
plt.xlabel("t, с")
plt.ylabel("U(t), В")
plt.grid(True)
plt.legend()

plt.figure(figsize=(10, 5))
plt.plot(t_test, dy_lin, color='orange', label="dU/dt")
plt.title("Производная сигнала ")
plt.xlabel("t, с")
plt.ylabel("dU/dt, В/с")
plt.grid(True)
plt.legend()

plt.show()

#Тест 1: Линейная функция y = 5t - 2
t_test = np.linspace(0, 10, 1000)
y_lin = 5 * t_test - 2
int_lin = integr(t_test, y_lin)
dy_lin = differ(t_test, y_lin)
print("\n--- Тестирование на линейной функции ---")
print("Аналитический интеграл =", (5 * 10**2 / 2 - 2 * 10) - (5 * 0**2 / 2 - 2 * 0))
print("Численный интеграл =", int_lin)
print("Среднее значение производной =", np.mean(dy_lin))

#Тест 2: Квадратичная функция y = 2t² - t + 0.5
y_quad = 2 * t_test**2 - t_test + 0.5
int_quad = integr(t_test, y_quad)
dy_quad = differ(t_test, y_quad)
print("\n--- Тестирование на квадратичной функции ---")
print("Аналитический интеграл =", (2/3 * 10**3 - 10**2 / 2 + 0.5 * 10) - (2/3 * 0**3 - 0**2 / 2 + 0.5 * 0))
print("Численный интеграл =", int_quad)
print("Производная в первой точке (аналит.) =", 4 * 0 - 1)
print("Производная в первой точке (числ.) =", dy_quad[0])

