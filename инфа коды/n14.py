#14
import numpy as np
import matplotlib.pyplot as plt
m=[14, 28, 19, 42, 22, 11, 10] #Тут любые числа какие хочешь крч
m1 = m[::-1]
k=[] #Список номеров элементов массива
print(m1)
for l in range(1,len(m)+1):
  k+=[l]
print(k)
plt.plot(k,m)
plt.grid()
plt.show()
plt.plot(k,m1)
plt.grid()
plt.show()
