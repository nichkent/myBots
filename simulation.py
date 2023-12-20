from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time
import constants as c


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
        # Define t to keep track of time
        for t in range(c.numTimeSteps):
            # Step the simulation
            p.stepSimulation()

            # Call the robot to sense on every step of the sim
            self.robot.Sense(t)

            # Call the robot to think between sensing and acting
            self.robot.Think()

            # Call the robot to move on every step of the sim
            self.robot.Act(t)

            # Sleep
            time.sleep(1/60)
            # print("Iteration:", i)

    def Get_Fitness(self):
        self.robot.Get_Fitness()
