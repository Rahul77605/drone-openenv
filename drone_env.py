import numpy as np

class DroneEnv:
    def __init__(self, grid_size=10):
        self.grid_size = grid_size
        self.max_steps = 200

    def reset(self):
        self.drone_pos = [0, 0]
        self.target = [9, 9]
        self.battery = 100
        self.steps = 0
        self.obstacles = [(3,3), (5,5), (7,2)]
        return self._get_state()

    def _get_state(self):
        dist = np.linalg.norm(np.array(self.drone_pos) - np.array(self.target))
        return {
            "position": self.drone_pos,
            "target": self.target,
            "battery": self.battery,
            "distance": dist
        }

    def step(self, action):
        self.steps += 1

        if action == 0: self.drone_pos[1] += 1
        elif action == 1: self.drone_pos[1] -= 1
        elif action == 2: self.drone_pos[0] -= 1
        elif action == 3: self.drone_pos[0] += 1

        self.drone_pos[0] = np.clip(self.drone_pos[0], 0, self.grid_size-1)
        self.drone_pos[1] = np.clip(self.drone_pos[1], 0, self.grid_size-1)

        self.battery -= 1
        reward = -0.1

        dist = np.linalg.norm(np.array(self.drone_pos) - np.array(self.target))
        reward += -dist * 0.05

        if tuple(self.drone_pos) in self.obstacles:
            reward -= 50

        done = False
        if self.drone_pos == self.target:
            reward += 100
            done = True

        if self.battery <= 0 or self.steps > self.max_steps:
            done = True

        return self._get_state(), reward, done, {}