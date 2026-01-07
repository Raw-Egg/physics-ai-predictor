import numpy as np
import csv
import os

print("SCRIPT STARTED")

# Physical constants
g = 9.81
k = 0.1
m = 1.0
dt = 0.01

# Initial conditions
x, y = 0.0, 0.0
vx, vy = 20.0, 20.0

data = []

time = 0.0
while y >= 0:
    ax = -(k / m) * vx
    ay = -g - (k / m) * vy

    vx += ax * dt
    vy += ay * dt

    x += vx * dt
    y += vy * dt

    data.append([time, x, y, vx, vy])
    time += dt

print(f"Collected {len(data)} data points")

# Absolute path handling
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "simulated_data.csv")

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["time", "x", "y", "vx", "vy"])
    writer.writerows(data)

print(f"Data written to: {file_path}")
print("SCRIPT FINISHED")
