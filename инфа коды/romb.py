import matplotlib.pyplot as plt  
import numpy as np  
x = np.array([0, 1, 0.5])  
y = np.array([0, 0, np.sqrt(3)/2])  
x = np.append(x, x)  
y = np.append(y, y)  
plt.figure(figsize=(6, 6))  
plt.plot(x, y, 'b-', linewidth=2)               
plt.show()  
