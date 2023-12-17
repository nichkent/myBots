import time
import pybullet as p
import pybullet_data
import numpy as np
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

# Create a np vector filled with zeros
backLegSensorValues = np.zeros(100)
# Create a np vector filled with zeros
frontLegSensorValues = np.zeros(100)

# Step the simulation 100 times
for i in range(100):
    p.stepSimulation()

    # Get the sensor value for backleg
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    # Get the sensor value for backleg
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    time.sleep(1/60)
    #print("Iteration:", i)

# Save to a file in data
np.save("data/backLegSensorValues.npy", backLegSensorValues)
# Save to a file in data
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)

# Stop sim
p.disconnect()
