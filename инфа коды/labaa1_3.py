import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
# Табличные данные
x0 = np.array([0, 1, 2, 3])
y0 = np.array([1.00, 0.76, 0.22, -0.26])
# Построение кубического сплайна
cs = CubicSpline(x0, y0)
# Массив точек для гладкого графика
x = np.linspace(0, 3, 200)
y = cs(x)
# Построение графика
plt.figure()
plt.plot(x, y)
plt.scatter(x0, y0)
plt.grid()
plt.title('Интерполяция функции Бесселя')
plt.show()
