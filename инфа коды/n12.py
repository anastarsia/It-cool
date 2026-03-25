#12
import matplotlib.pyplot as plt
def calculate_sum(N):
  S_values = []
  sum = 0
  for k in range(1, N + 1):
    sum += k** 2
    S_values.append(sum) # Добавляем текущее значение суммы в список
  return S_values
def main():
  N = int(input("Введите N: "))
  S_values = calculate_sum(N)
  plt.plot(range (1, N + 1), S_values, marker='o')
  plt.xlabel('k')
  plt.ylabel('s')
  plt.title('График зависимости S(k)')
  plt.show()
if __name__ == "__main__":
  main()
