import matplotlib.pyplot as plt

with open ('load_chart_for_eco.txt', 'r', encoding='utf-8') as f:
    power_load = [float(line.strip().replace(',', '.')) for line in f if line.strip()]
# Тарифы (цена руб./кВт∙ч по часам):
# Одноставочный: 3.08 для всех часов
one_rate = [3.08]*24

# Двухставочный:
# 07:00-23:00 - 3.54, 23:00-07:00 - 2.40
two_rate = []
for h in range(24):
    if 7 <= h < 23:
        two_rate.append(3.54)
    else:
        two_rate.append(2.40)

# Трехставочный:
# 07:00-10:00, 17:00-21:00 - 3.80
# 10:00-17:00, 21:00-23:00 - 3.08
# 23:00-07:00 - 2.40
three_rate = []
for h in range(24):
    if (7 <= h < 10) or (17 <= h < 21):
        three_rate.append(3.80)
    elif (10 <= h < 17) or (21 <= h < 23):
        three_rate.append(3.08)
    else:
        three_rate.append(2.40)

def calculate_cost(power, rate):
    total_cost = 0
    total_energy = 0
    for p, c in zip(power, rate):
        total_cost += p * c * 1  # интервал 1 час
        total_energy += p * 1
    avg_cost = total_cost / total_energy if total_energy != 0 else 0
    return total_cost, avg_cost

# Расчеты
cost_one, avg_one = calculate_cost(power_load, one_rate)
cost_two, avg_two = calculate_cost(power_load, two_rate)
cost_three, avg_three = calculate_cost(power_load, three_rate)

# Вывод: гистограммы и самый выгодный тариф
import numpy as np

labels = ['Одноставочный', 'Двухставочный', 'Трехставочный']
total_costs = [cost_one, cost_two, cost_three]
avg_costs = [avg_one, avg_two, avg_three]

# Определяем самый выгодный тариф (минимальная стоимость)
min_cost = min(total_costs)
best_tariff = labels[total_costs.index(min_cost)]

# Гистограмма суммарных затрат
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.bar(labels, total_costs, color=['blue', 'green', 'orange'])
plt.title('Суммарные затраты за сутки (руб.)')
plt.ylabel('Затраты, руб.')

# Гистограмма средней стоимости 1 кВт∙ч
plt.subplot(1, 2, 2)
plt.bar(labels, avg_costs, color=['blue', 'green', 'orange'])
plt.title('Средняя стоимость 1 кВт∙ч (руб.)')
plt.ylabel('Средняя цена, руб.')

plt.tight_layout()
plt.show()

print(f"Самый выгодный тариф: {best_tariff} с затратами {min_cost:.2f} руб. и средней стоимостью {avg_costs[total_costs.index(min_cost)]:.2f} руб./кВт∙ч")
