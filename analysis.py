# analysis.py
import matplotlib.pyplot as plt

# Quarterly equipment efficiency rate data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
efficiency_rate = [75.49, 72.86, 76.99, 75.64]
industry_target = 90
average_efficiency = sum(efficiency_rate) / len(efficiency_rate)

# Print average
print(f"Average Equipment Efficiency Rate: {average_efficiency:.2f}")

# Plotting the trend vs industry benchmark
plt.figure(figsize=(8,5))
plt.plot(quarters, efficiency_rate, marker='o', label='Company Efficiency')
plt.axhline(y=industry_target, color='r', linestyle='--', label='Industry Target (90)')
plt.title('Quarterly Equipment Efficiency Rate - 2024')
plt.xlabel('Quarter')
plt.ylabel('Efficiency Rate')
plt.ylim(70, 95)
plt.grid(True)
plt.legend()
plt.savefig('efficiency_trend.png', dpi=300)
plt.show()
