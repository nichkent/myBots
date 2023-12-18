from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim


class ROBOT:
    def __init__(self):
        self.motors = MOTOR()

        # Set the Body
        self.robotId = p.loadURDF("body.urdf")

        # Prepare pyrosim for the robot
        pyrosim.Prepare_To_Simulate(self.robotId)

        # Call Prepare To Sense function in Robot
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        sensors = SENSOR()
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName)

