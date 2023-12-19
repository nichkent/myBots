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

    def Set_Value(self, desiredAngle, robotId):
        # Create motor for the robot's joints
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,  # Using the name of each joint
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,  # Using the motor's values to set the position
            maxForce=50)

