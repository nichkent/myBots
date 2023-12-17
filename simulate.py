import time
import pybullet as p
import pybullet_data
import numpy as np

import pyrosim.pyrosim as pyrosim

amplitude_back_leg = np.pi/6
frequency_back_leg = 20
phaseOffset_back_leg = 0

amplitude_front_leg = np.pi/6
frequency_front_leg = 20
phaseOffset_front_leg = np.pi/4

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
backLegSensorValues = np.zeros(1000)
# Create a np vector filled with zeros
frontLegSensorValues = np.zeros(1000)


# Create the vectors for movement
targetAngles_back_leg = amplitude_back_leg * np.sin(2 * np.pi * frequency_back_leg * np.linspace(0, 1, 1000) + phaseOffset_back_leg)
targetAngles_front_leg = amplitude_front_leg * np.sin(2 * np.pi * frequency_front_leg * np.linspace(0, 1, 1000) + phaseOffset_front_leg)

#np.save("data/targetAngles_back_leg.npy", targetAngles_back_leg)
#np.save("data/targetAngles_front_leg.npy", targetAngles_front_leg)


# Step the simulation 100 times
for i in range(1000):
    p.stepSimulation()

    # Get the sensor value for backleg
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    # Get the sensor value for frontleg
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")


    # Create motors for the robot's joints
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles_back_leg[i],
        maxForce=50)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles_front_leg
        [i],
        maxForce=50)

    time.sleep(1/60)
    #print("Iteration:", i)

# Save to a file in data
#np.save("data/backLegSensorValues.npy", backLegSensorValues)
# Save to a file in data
#np.save("data/frontLegSensorValues.npy", frontLegSensorValues)

# Stop sim
p.disconnect()
