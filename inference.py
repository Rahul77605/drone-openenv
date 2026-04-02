import os
from env.drone_env import DroneEnv

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
MODEL_NAME = os.getenv("MODEL_NAME", "default-model")
HF_TOKEN = os.getenv("HF_TOKEN")

def simple_agent(state):
    dx = state["target"][0] - state["position"][0]
    dy = state["target"][1] - state["position"][1]

    if abs(dx) > abs(dy):
        return 3 if dx > 0 else 2
    else:
        return 0 if dy > 0 else 1

def run():
    env = DroneEnv(difficulty="medium")
    state = env.reset()

    done = False
    total_reward = 0

    while not done:
        action = simple_agent(state)
        state, reward, done, _ = env.step(action)
        total_reward += reward

    print("Total Reward:", total_reward)
    return total_reward

if __name__ == "__main__":
    run()