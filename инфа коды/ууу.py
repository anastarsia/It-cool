import matplotlib.pyplot as plt
import numpy as np
T1 = np.arange(-4,-2,0.01)
F1 = 1 + (1+T1)**2/5
T2 = np.array ([-2,0])
F2 = 1 + (2+T2)**2/5
T3 = np.array([0,1])
F3 = np.array([1.8,1.8])
T4 = np.array([1,3])
F4 = 1 + (T4-3)**2/5
T5 = np.arange(3,5,0.01)
F5 = 1 - (T5-3)**2/5
plt.figure(1)
plt.plot(T1,F1,'r',lw = 2, label = 'f(t)')
plt.plot(T2,F2,'r',lw = 2)
plt.plot(T3,F3,'r',lw = 2)
plt.plot(T4,F4,'r',lw = 2)
plt.plot(T5,F5,'r',lw = 2)
plt.grid()
plt.legend()
plt.xlabel('t')
plt.ylabel('f')
plt.title('График')
plt.show(block = False)
