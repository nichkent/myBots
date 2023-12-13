import time
import pybullet as p
import pybullet_data

# Start the sim
physicsClient = p.connect(p.GUI)

# Connect pybullect data
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Set the gravity
p.setGravity(0, 0, -9.8)

# Set the floor
planeId = p.loadURDF("plane.urdf")

# Load box object
p.loadSDF("boxes.sdf")

# Step the simulation 1000 times
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print("Iteration:", i)

# Stop sim
p.disconnect()
