from sensor import SENSOR
from motor import MOTOR
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim


class ROBOT:
    def __init__(self):
        self.motors = MOTOR()

        # Set the Body
        self.robotId = p.loadURDF("body.urdf")

        # Prepare pyrosim for the robot
        pyrosim.Prepare_To_Simulate(self.robotId)

        # Define sensors dictionary as empty
        self.sensors = {}

        # Call Prepare To Sense function in Robot
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        # Define the robot's sensors based on how many are in body.urdf
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)