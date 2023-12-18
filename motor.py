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


        # Call Prepare_To_Act in motor.py
        self.Prepare_To_Act()

        # Create a np vector filled with zeros based on a sin function defined in constants.py
        self.motorValues = self.targetAngles

    def Prepare_To_Act(self):
        if self.jointName == "Torso_FrontLeg":
            # Pull constants from constants.py
            self.amplitude = c.amplitude
            self.frequency = c.frequency
            self.offset = c.phaseOffset
        if self.jointName == "Torso_BackLeg":
            # Pull constants from constants.py
            self.amplitude = c.amplitude
            self.frequency = c.frequency / 2
            self.offset = c.phaseOffset

        # Create the vectors for movement based on a sin wave
        self.targetAngles = self.amplitude * numpy.sin(2 * numpy.pi * self.frequency * numpy.linspace(0, 1, 1000) + self.offset)

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
