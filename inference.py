from fastapi import FastAPI
from pydantic import BaseModel
from env.drone_env import DroneEnv

app = FastAPI()

env = DroneEnv()
state = env.reset()

class Action(BaseModel):
    action: int

@app.post("/reset")
def reset():
    global state
    state = env.reset()
    return state

@app.post("/step")
def step(action: Action):
    global state
    state, reward, done, _ = env.step(action.action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }

@app.get("/state")
def get_state():
    return state
