#3
import matplotlib.pyplot as plt
import numpy as np
x = int(input('Enter x:'))
y = int(input('Enter y:'))
t = np.linspace(0, 2*np.pi)
i = x + np.cos(t)
h = y + np.sin(t)
plt.plot(i, h)
plt.plot(x, y, 'og')
plt.show()
