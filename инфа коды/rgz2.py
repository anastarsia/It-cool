
import matplotlib.pyplot as plt
with open('load_chart_for_eco.txt', 'r', encoding='utf-8') as f:
    P = [float(line.strip().replace(',', '.')) for line in f if line.strip()]

def cost1(hour):
    return 3.08
def cost2(hour):
    if 7 <= hour < 23:
        return 3.54
    else:
        return 2.40
def cost3(hour):
    if (7 <= hour < 10) or (17 <= hour < 21):
        return 3.80       
    elif (10 <= hour < 17) or (21 <= hour < 23):
        return 3.08       
    else:
        return 2.40       

def calc_total_and_avg(P, cost_func):
    total = 0
    energy = sum(P)
    for h in range(24):
        total += P[h] * cost_func(h)
    avg = total / energy
    return total, avg

C1, avg1 = calc_total_and_avg(P, cost1)
C2, avg2 = calc_total_and_avg(P, cost2)
C3, avg3 = calc_total_and_avg(P, cost3)

costs = {"Одноставочный": C1, "Двухставочный": C2, "Трёхставочный": C3}
best_tariff = min(costs, key=costs.get)

print("\nСамый выгодный тариф:", best_tariff)

plt.figure(figsize=(8,5))
plt.bar(["Одноставочный", "Двухставочный", "Трёхставочный"], [C1, C2, C3], color=['blue', 'orange', 'green'])
plt.ylabel("Стоимость, руб")
plt.title("Стоимость электроэнергии за сутки по тарифам")

plt.figure(figsize=(8,5))
plt.bar(["Одноставочный", "Двухставочный", "Трёхставочный"], [avg1, avg2, avg3], color=['blue', 'orange', 'green'])
plt.ylabel("Средняя стоимость, руб/кВт⋅ч")
plt.title("Средняя стоимость 1 кВт⋅ч по тарифам")

plt.show()
