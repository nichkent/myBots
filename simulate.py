import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorsValues = numpy.zeros(100)

for i in range(100):
    p.stepSimulation()

    backLegSensorsValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

    t.sleep(1/60)

numpy.save("data/backLegTouchVector.npy", backLegSensorsValues[i])
p.disconnect()