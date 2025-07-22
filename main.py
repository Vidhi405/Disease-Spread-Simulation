from simulation import run_simulation
from visualize import plot_counts, animate_grid
import os

os.makedirs("results/plots", exist_ok=True)
os.makedirs("results/animations", exist_ok=True)

# Run simulation
history = run_simulation()

# Visualize results
plot_counts(history)
animate_grid(history)
