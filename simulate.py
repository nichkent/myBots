import time
import pybullet as p
import pybullet_data

import pyrosim.pyrosim as pyrosim

# Start the sim
physicsClient = p.connect(p.GUI)

# Connect pybullect data
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Set the gravity
p.setGravity(0, 0, -9.8)

# Set the floor
planeId = p.loadURDF("plane.urdf")

# Set the Body
robotId = p.loadURDF("body.urdf")

# Load box object
p.loadSDF("world.sdf")

# Prepare pyrosim for the robot
pyrosim.Prepare_To_Simulate(robotId)

# Step the simulation 1000 times
for i in range(1000):
    p.stepSimulation()

    # Get the sensor value for backleg
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    print(backLegTouch)

    time.sleep(1/60)
    #print("Iteration:", i)

# Stop sim
p.disconnect()
