from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time


class SIMULATION:
    def __init__(self):

        # Start the sim
        physicsClient = p.connect(p.GUI)

        # Connect pybullect data
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # Set the gravity
        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT()

    def __del__(self):
        # Stop sim
        p.disconnect()

    def Run(self):
        for t in range(1000):
            p.stepSimulation()
            self.robot.Sense(t)
            #
            # # Create motors for the robot's joints
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=self.robotId,
            #     jointName="Torso_BackLeg",
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=c.targetAngles_back_leg[i],
            #     maxForce=50)
            #
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=self.robotId,
            #     jointName="Torso_FrontLeg",
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=c.targetAngles_front_leg
            #     [i],
            #     maxForce=50)
            #
            time.sleep(1/60)
            # print("Iteration:", i)


