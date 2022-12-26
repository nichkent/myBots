import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorsValues = numpy.zeros(500)
frontLegSensorsValues = numpy.zeros(500)

for i in range(500):
    # Makes the simulation step one time (tic)
    p.stepSimulation()

    # Stores sensor values
    backLegSensorsValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorsValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # Supplies force to the backleg joint
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_BackLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=((math.pi * random.random()) - math.pi/2),
        maxForce=500)

    # Supplies force to the front joint
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_FrontLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=((math.pi * random.random()) - math.pi/2),
        maxForce=500)

    # Makes the programs in simulation time run at 1/60 of a sec
    t.sleep(1/60)

numpy.save("data/backLegTouchVector.npy", backLegSensorsValues)
numpy.save("data/frontLegTouchVector.npy", frontLegSensorsValues)
p.disconnect()