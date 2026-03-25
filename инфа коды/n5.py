#5
import matplotlib.pyplot as plt
import numpy as np
import math as m
t=np.linspace(-3*m.pi, (-1)*m.pi)
f1=np.sin(t)
plt.plot(t, f1, label='y = sin(t)', lw=2)
t=np.linspace((-1)*m.pi, 0)
f2=t*0
plt.plot(t, f2, label='y = 0', lw=2)
t=np.linspace(0, 1)
f3=t
plt.plot(t, f3, label='y = t', lw=2)
t=np.linspace(1, 2)
f4=2-t
plt.plot(t, f4, label='y = 2t', lw=2)
t=np.linspace(2, 10)
f5=-np.sin(t-2)
plt.plot(t, f5, label='y = sin(t-2)', lw=2)
plt.axhline(0, color='black', linewidth=2, zorder = 0)
plt.axvline(0, color='black', linewidth=2, zorder = 0)
plt.title('График функции y = sin(t), y = 0, y = t, y = 2 t и y = sin(t-2)')
plt.xlabel('t')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
