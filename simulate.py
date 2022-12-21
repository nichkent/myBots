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
backLegSensorsValues = numpy.zeros(500)
frontLegSensorsValues = numpy.zeros(500)

for i in range(500):
    p.stepSimulation()

    backLegSensorsValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorsValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    t.sleep(1/60)

numpy.save("data/backLegTouchVector.npy", backLegSensorsValues)
numpy.save("data/frontLegTouchVector.npy", frontLegSensorsValues)
p.disconnect()