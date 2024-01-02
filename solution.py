import random
import os
import time
import numpy
import pyrosim.pyrosim as pyrosim
import constants as c


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1

        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGUI):
        # Call generate functions for sim
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain(self.myID)

        # Run the simulation with or without graphics
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        # Sleep the program if the fitness files have yet to be created
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)

        # Read the fitness values of the parent
        with open("fitness" + str(self.myID) + ".txt", "r") as fitnessFile:
            self.fitness = float(fitnessFile.read())
        #print(self.fitness)
        os.system("del fitness" + str(self.myID) + ".txt")

    def Create_World(self):
        # Define cube dims
        length = 1
        width = 1
        height = 1

        # Define cube pos
        x = -2
        y = 0.5
        z = 2

        # Start generation
        pyrosim.Start_SDF("world.sdf")

        # Create cube
        pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])

        # End cube generation
        pyrosim.End()

    def Generate_Body(self):
        # Define body dims
        length = 1
        width = 1
        height = 1

        # Define body pos
        x = 0
        y = 0
        z = 1

        # Create the body of the robot
        pyrosim.Start_URDF("body.urdf")

        # Create body

        # Torso
        pyrosim.Send_Cube(name="Torso", pos=[x, y, z+2], size=[length * .8, width, height * 2])

        # Torso
        pyrosim.Send_Cube(name="Head", pos=[x, y, z], size=[length * .4, width, height * .8])
        pyrosim.Send_Joint(name="Torso_Head", parent="Torso", child="Head", type="revolute",
                           position=[x, y, z + 2.25], jointAxis="1 0 0")

        # Left Leg
        pyrosim.Send_Cube(name="LeftLeg", pos=[x, y, z-1.5], size=[length * 0.4, width * 0.4, height])
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[x, y + .5, z+1.1], jointAxis="0 1 0")

        # Left Lower Leg
        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute",
                           position=[x, y, z-2], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[x, y, z-1.5], size=[length * 0.2, width * 0.2, height])

        # Right Leg
        pyrosim.Send_Cube(name="RightLeg", pos=[x, y, z-1.5], size=[length * 0.4, width * 0.4, height])
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[x, y-.5, z+1.1], jointAxis="0 1 0")
        # Right Lower Leg
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute",
                           position=[x, y, z-2], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[x, y, z - 1.5], size=[length * 0.2, width * 0.2, height])

        # Right Arm
        # pyrosim.Send_Cube(name="RightArm", pos=[x, y, z-1.5], size=[length * 0.4, width * 0.4, height])
        # pyrosim.Send_Joint(name="Torso_RightArm", parent="Torso", child="RightArm", type="revolute",
        #                    position=[x, y + .7, z + 3], jointAxis="0 1 0")
        # # Right Lower Arm
        # pyrosim.Send_Cube(name="RightLowerArm", pos=[x, y, z - 1.5], size=[length * 0.2, width * 0.2, height * 1.2])
        # pyrosim.Send_Joint(name="RightArm_RightLowerArm", parent="RightArm", child="RightLowerArm", type="revolute",
        #                    position=[x, y, z - 2], jointAxis="0 1 0")
        #
        # # Left Arm
        # pyrosim.Send_Cube(name="LeftArm", pos=[x, y, z - 1.5], size=[length * 0.4, width * 0.4, height])
        # pyrosim.Send_Joint(name="Torso_LeftArm", parent="Torso", child="LeftArm", type="revolute",
        #                    position=[x, y - .7, z + 3], jointAxis="0 1 0")
        #
        # # Left Lower Arm
        # pyrosim.Send_Cube(name="LeftLowerArm", pos=[x, y, z - 1.5], size=[length * 0.2, width * 0.2, height * 1.2])
        # pyrosim.Send_Joint(name="LeftArm_LeftLowerArm", parent="LeftArm", child="LeftLowerArm", type="revolute",
        #                    position=[x, y, z - 2], jointAxis="0 1 0")

        # End robot generation
        pyrosim.End()

    def Generate_Brain(self, ID):
        # Define body dims
        length = 1
        width = 1
        height = 1

        # Define body pos
        x = 0
        y = 0.5
        z = 0

        # Create the body of the robot
        pyrosim.Start_NeuralNetwork("brain" + str(ID) + ".nndf")

        # Create sensor neurons to receive information from sensors
        pyrosim.Send_Sensor_Neuron(name=0, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="RightLowerLeg")

        # Create motor neurons to move the link's joints
        pyrosim.Send_Motor_Neuron(name=2, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=5, jointName="RightLeg_RightLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_RightArm")
        # pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_LeftArm")
        # pyrosim.Send_Motor_Neuron(name=8, jointName="LeftArm_LeftLowerArm")
        # pyrosim.Send_Motor_Neuron(name=9, jointName="RightArm_RightLowerArm")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_Head")


        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])

        # End robot generation
        pyrosim.End()

    def Mutate(self):
        # Find random row and column
        row = random.randint(0, c.numSensorNeurons - 1)
        column = random.randint(0, c.numMotorNeurons - 1)

        # Calculate the amount the random element is changed by
        mutation_amount = random.random() * 2 - 1

        # Mutate that random element in weights for the child
        self.weights[row][column] = mutation_amount

    def Set_ID(self, newID):
        self.myID = newID