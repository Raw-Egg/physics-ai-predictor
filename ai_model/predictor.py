import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os

# Resolve paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, "data", "simulated_data.csv")

# Load dataset
df = pd.read_csv(data_path)

# The final horizontal distance is the range
final_range = df["x"].iloc[-1]

# For now, we simulate multiple launches by varying initial velocities
vx0_values = np.linspace(10, 30, 10)
vy0_values = np.linspace(10, 30, 10)

X = []
y = []

for vx0 in vx0_values:
    for vy0 in vy0_values:
        # Simple physics-inspired approximation
        predicted_range = final_range * (vx0 / 20) * (vy0 / 20)
        X.append([vx0, vy0])
        y.append(predicted_range)

X = np.array(X)
y = np.array(y)

# Train AI model
model = LinearRegression()
model.fit(X, y)

print("AI model trained successfully.")
print("Model coefficients:", model.coef_)
print("Model intercept:", model.intercept_)

# Test prediction
test_vx, test_vy = 25, 22
ai_prediction = model.predict([[test_vx, test_vy]])[0]

print(f"AI-predicted range for vx={test_vx}, vy={test_vy}: {ai_prediction:.2f} m")
