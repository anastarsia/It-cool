#11
import numpy as np
import matplotlib.pyplot as plt
import math
N = int(input())
s = 0
k = 1
s = np.array([k**2 for k in range(N)]) . cumsum()
k = range(N)
plt. plot(k,s)
print(s)
