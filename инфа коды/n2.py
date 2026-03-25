import matplotlib.pyplot as plt
a = float(input("Введите длину a: "))
x = float(input("Введите координату x центра: "))
y = float(input("Введите координату y центра: "))
h = (3**0.5 / 2) * a
x1 = x - a / 2
y1 = y - h / 3
x2 = x + a / 2
y2 = y - h / 3
x3 = x
y3 = y + (2 * h) / 3

plt.figure()
plt.grid()
plt.title("Равносторонний треугольник")
plt.xlabel("x")
plt.ylabel("y")
plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1])
plt.scatter(x, y, color='red')
plt.show()
