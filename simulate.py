import time
import pybullet as p

# Start the sim
physicsClient = p.connect(p.GUI)

# Step the simulation 1000 times
for i in range(1000):
    p.stepSimulation()
    time.sleep(1)
    print("Iteration:", i)

# Stop sim
p.disconnect()