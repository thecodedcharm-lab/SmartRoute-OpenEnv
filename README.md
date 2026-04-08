SmartRoute: Last-Mile Delivery Optimization OpenEnv

SmartRoute is a real-world OpenEnv environment designed to simulate last-mile delivery logistics.
An AI agent learns how to efficiently deliver packages while managing fuel, time, and traffic constraints.

This project was built for the Scaler OpenEnv Hackathon.

---

🚚 Problem

Last-mile delivery is one of the most expensive and complex parts of logistics systems used by companies like Amazon and Uber.

Drivers must constantly balance:

- Limited fuel
- Delivery deadlines
- Traffic congestion
- Priority packages

SmartRoute simulates this real-world decision problem so reinforcement learning agents can learn efficient delivery strategies.

---

🧠 Environment Overview

The agent controls a delivery vehicle navigating a city network to deliver packages.

The agent must optimize:

- number of deliveries
- fuel consumption
- time efficiency
- priority package handling

---

📊 State Space

Each environment state contains:

- packages_remaining
- fuel_level
- time_left
- traffic_level
- current_location
- priority_packages

Example state:

{
"packages_remaining": 5,
"fuel": 60,
"time_left": 120,
"traffic_level": 0.4,
"current_location": 2,
"priority_packages": 1
}

---

🎮 Action Space

The agent can take one of the following actions:

0 → Deliver nearest package
1 → Deliver priority package
2 → Refuel vehicle
3 → Change route to avoid traffic
4 → Wait

---

🏆 Reward Function

The reward function encourages efficient delivery behavior.

Event| Reward
Successful delivery| +1
Priority delivery| +1.5
Fuel wasted| -0.3
Traffic delay| -0.5
Running out of fuel| -1

---

🧪 Tasks

Three tasks of increasing difficulty are included.

Easy

Deliver 3 packages within the time limit.

Medium

Deliver 6 packages while managing limited fuel.

Hard

Deliver 10 packages with dynamic traffic and priority deliveries.

Graders return scores between 0.0 and 1.0.

---

🔧 API

The environment implements the standard OpenEnv API.

reset() → initializes the environment

step(action) → performs an action and updates the state

state() → returns the current environment state

---

📂 Project Structure

smartroute-openenv/
│
├── delivery_env.py
├── inference.py
├── openenv.yaml
├── grader.py
├── Dockerfile
├── requirements.txt
└── README.md

---

🚀 Running the Environment

Install dependencies

pip install -r requirements.txt

Run the inference script

python inference.py

---

🧪 Evaluation

The inference script runs the agent through all tasks and prints structured logs required by the OpenEnv evaluation pipeline.

---

🐳 Docker

The project includes a Dockerfile for reproducible environments and deployment.

---

🤖 Use Cases

This environment can be used to train AI agents for:

- logistics optimization
- delivery route planning
- fleet management research

---

📜 License

MIT License
