import matplotlib.pyplot as plt

# Quarterly Equipment Efficiency Rate data
quarters = ["Q1", "Q2", "Q3", "Q4"]
efficiency = [75.49, 72.86, 76.99, 75.64]
industry_target = 90
average = sum(efficiency) / len(efficiency)

print(f"Quarterly Data: {list(zip(quarters, efficiency))}")
print(f"Average Efficiency: {average:.2f}")

# Plotting
plt.figure(figsize=(8,5))
plt.plot(quarters, efficiency, marker='o', linestyle='-', color='b', label='Equipment Efficiency')
plt.hlines(industry_target, xmin=0, xmax=3, colors='r', linestyles='dashed', label='Industry Target (90)')
plt.title('Quarterly Equipment Efficiency Rate (2024)')
plt.xlabel('Quarter')
plt.ylabel('Efficiency Rate')
plt.ylim([70, 100])
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('efficiency_trend.png')
plt.show()
