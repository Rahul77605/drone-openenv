# 🚁 Drone Delivery OpenEnv

## 📌 Problem
Optimizing drone delivery in real-world conditions with obstacles, battery limits, and environmental disturbances.

## ⚙️ Environment Design

### State
- Drone position
- Target position
- Battery level
- Distance to target

### Actions
- Move up, down, left, right

### Reward
- Distance minimization
- Successful delivery (+100)
- Collision penalty (-50)

### Difficulty Levels
- Easy: minimal obstacles
- Medium: moderate obstacles
- Hard: wind disturbance + more obstacles

## ▶️ Run

```bash
python inference.py