import time
import pybullet as p
import pybullet_data
import constants as c
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

#np.save("data/targetAngles_back_leg.npy", targetAngles_back_leg)
#np.save("data/targetAngles_front_leg.npy", targetAngles_front_leg)


# Step the simulation 100 times
for i in range(1000):
    p.stepSimulation()

    # Get the sensor value for backleg
    c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    # Get the sensor value for frontleg
    c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")


    # Create motors for the robot's joints
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=c.targetAngles_back_leg[i],
        maxForce=50)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=c.targetAngles_front_leg
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
