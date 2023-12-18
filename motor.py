import numpy

import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim


class MOTOR:
    def __init__(self, jointName, robotId):
        # Using the current joint name
        self.jointName = jointName

        # Using the current robot id
        self.robotId = robotId

        # Create a np vector filled with zeros based on a sin function defined in constants.py
        self.motorValues = c.targetAngles

        # Call Prepare_To_Act in motor.py
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        # Pull constants from constants.py
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset

    def Set_Value(self, t, robotId):
        # Create motor for the robot's joints
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,  # Using the name of each joint
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],  # Using the motor's values to set the position
            maxForce=50)

    def Save_Values(self):
        numpy.save("data/motorValues.npy", self.motorValues)
