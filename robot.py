from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c


class ROBOT:
    def __init__(self, ID):
        # Set the Body
        self.robotId = p.loadURDF("body.urdf")

        # Prepare pyrosim for the robot
        pyrosim.Prepare_To_Simulate(self.robotId)

        # Define sensors dictionary as empty
        self.sensors = {}

        # Define neural network
        self.nn = NEURAL_NETWORK("brain" + str(ID) + ".nndf")

        # Delete nndf file after it has been read
        os.system("del brain" + str(ID) + ".nndf")

        # Define motors dictionary as empty
        self.motors = {}

        # Call Prepare_To_Sense function in Robot
        self.Prepare_To_Sense()

        # Call Prepare_To_Act function in Robot
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        # Define the robot's sensors based on how many links are in body.urdf
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        # For each sensor get the value of that sensor
        for sensor in self.sensors.values():
            sensor.Get_Value(t)

    def Prepare_To_Act(self):
        # Define the robot's motors based on how many joints are in body.urdf
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName, self.robotId)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange

                # For each motor set the value of that motor
                if jointName in self.motors:
                    self.motors[jointName].Set_Value(desiredAngle, self.robotId)



    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self, solutionID):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        linkPosition = basePositionAndOrientation[0]
        xPosition = linkPosition[0]

        with open("tmp" + str(solutionID) + ".txt", "w") as f:
            f.write(str(xPosition))
        os.system("rename tmp" + str(solutionID) + ".txt " "fitness" + str(solutionID) + ".txt")

