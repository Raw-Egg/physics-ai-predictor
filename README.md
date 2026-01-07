# physics-ai-predictor
This repository contains a physics-based simulation of projectile motion under air resistance combined with a simple AI model trained on simulated data. The project compares analytical equations, numerical simulation, and data-driven predictions to study the strengths and limitations of AI when applied to physical systems.

The simulated trajectory shows a smooth, asymmetric path due to linear air resistance, confirming correct numerical integration of Newton’s laws.

AI-Based Prediction
A linear regression model is trained to predict the horizontal range of a projectile using its initial velocity components. While the model successfully captures trends present in the simulated data, it does not encode any physical laws and fails to generalize beyond the conditions it was trained on. This comparison highlights the strengths of physics-based modeling over purely data-driven approaches for physical systems.



Status: Completed (v1.0)

This repository represents a finished exploratory project combining
physics-based simulation with a simple AI predictor.
