import numpy as np
M = np.zeros((10,10))
for i in range (10,0,-1):
    M[10-i,10-i :] = i
for i in range (5):
    M[5+i,5+i:]= 5-i
print(M)
