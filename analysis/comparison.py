import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, "data", "simulated_data.csv")

df = pd.read_csv(data_path)

# Plot trajectory
plt.figure()
plt.plot(df["x"], df["y"])
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.title("Projectile Motion with Air Resistance")
plt.grid(True)

# Save plot
output_path = os.path.join(base_dir, "analysis", "trajectory.png")
plt.savefig(output_path)
plt.show()

print(f"Plot saved to {output_path}")
