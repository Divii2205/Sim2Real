# Sim2Real

This project focuses on **Sim2Real learning using the Go2 quadruped robot**, trained inside the **Genesis world simulation**. The objective is to design, train, and evaluate control and learning policies in a high-fidelity simulated environment and prepare them for reliable transfer to real-world robotic systems, reducing risk, cost, and iteration time.

## 📌 Overview

Sim2Real (Simulation-to-Reality) is a common robotics and reinforcement learning workflow where agents are trained in simulation and then deployed in the real world. This repository explores that pipeline using the **Go2 robot model** within the **Genesis simulation environment**, enabling rapid experimentation and controlled testing.

The project includes scripts for training, evaluation, and environment setup, with a focus on clean integration and extensibility.

## 🎯 Task Levels

The Go2 robot is trained and evaluated across the following task levels:

### 🟢 Level 1: The Toddler (Walking)

- **Goal:**  Stable walking with a natural gait, preferably in a straight line.
- **Metric:**  Maintain forward velocity between **0.5 – 1.0 m/s**, No falling, Cover the maximum possible distance within **60 seconds**

---

### 🔵 Level 2: The Sprinter (Running)

- **Goal:**  High-speed sprinting.
- **Metric:** Achieve forward velocity **≥ 2.0 m/s**

---

### 🟣 Level 3: The Geometrician (Circle)

- **Goal:**  Walk in a perfect circular trajectory.
- **Constraint:**  Circle radius = **2 meters**
- **Metric:**  Average **Root Mean Square Error (RMSE)** over **10 rounds**

---

### 🔴 Level 4: The Ballerina (Spin)

- **Goal:** Pure rotation in place.
- **Metric:**  High angular velocity (**ω**),  Zero forward velocity (**v = 0**)

---


## 📁 Repository Structure

| File | Description |
|-----|-------------|
| `go2_train.py` | Training script for the Go2 agent |
| `go2_eval.py` | Evaluation and testing script |
| `go2_env.py` | Custom environment wrapper for Genesis |
| `agent.py` | Core agent and policy logic |
| `requirements.txt` | Python dependencies |

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Divii2205/Sim2Real.git
cd Sim2Real
