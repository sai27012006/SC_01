import matplotlib.pyplot as plt
import numpy as np

# Simulated age vs population data (more granular)
ages = np.arange(0, 101, 1)  # Age from 0 to 100
population = np.piecewise(
    ages,
    [ages <= 20, (ages > 20) & (ages <= 64), ages > 64],
    [lambda x: -0.05 * (x - 20)**2 + 25,  # Peak at 20
     lambda x: -0.01 * (x - 28)**2 + 25,  # Plateau
     lambda x: -0.02 * (x - 64)**2 + 10]  # Decline after 64
)
population = np.maximum(population, 0)  # No negative values

# Define age bands (more detailed)
age_bands = [
    (0, 10, 'gold', '0-10 Years\n312 Mn (22.0%)'),
    (10, 20, 'orange', '11-20 Years\n200 Mn (14.1%)'),
    (20, 40, 'skyblue', '21-40 Years\n450 Mn (31.7%)'),
    (40, 64, 'royalblue', '41-64 Years\n357 Mn (25.3%)'),
    (64, 80, 'violet', '65-80 Years\n75 Mn (5.3%)'),
    (80, 100, 'purple', '80+ Years\n23 Mn (1.6%)')
]

# Plot
fig, ax = plt.subplots(figsize=(14, 7))
y_base = np.zeros_like(ages)

for (start, end, color, label) in age_bands:
    mask = (ages >= start) & (ages <= end)
    ax.fill_between(ages, y_base, population, 
                    where=mask, 
                    color=color, 
                    alpha=0.7, 
                    label=label)

# Add median line and annotations
ax.axvline(28, color='black', linestyle='--', linewidth=1.5, label='Median Age: 28')
ax.set_title("India’s Population Distribution by Age (2022)\nTotal Population: 1.42 Billion", fontsize=16, pad=20)
ax.set_xlabel("Age", fontsize=12)
ax.set_ylabel("Population (Millions)", fontsize=12)
ax.set_xlim(0, 100)
ax.set_ylim(0, 30)
ax.grid(True, linestyle='--', alpha=0.3)

# Custom legend
ax.legend(loc='upper right', fontsize=10, framealpha=1)

plt.tight_layout()
plt.show()