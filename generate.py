import pyrosim.pyrosim as pyrosim
import random

def Create_World():
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


def Generate_Body():
    # Define body dims
    length = 1
    width = 1
    height = 1

    # Define body pos
    x = 0
    y = 0.5
    z = 0

    # Create the body of the robot
    pyrosim.Start_URDF("body.urdf")

    # Create body
    pyrosim.Send_Cube(name="FrontLeg", pos=[x + .5, z, y-1], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[x + .5, z, y + .5])
    pyrosim.Send_Cube(name="Torso", pos=[x, z, y + 1], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[x - .5, z, y + .5])
    pyrosim.Send_Cube(name="BackLeg", pos=[x - .5, z, y-1], size=[length, width, height])

    # End robot generation
    pyrosim.End()

def Generate_Brain():
    # Define body dims
    length = 1
    width = 1
    height = 1

    # Define body pos
    x = 0
    y = 0.5
    z = 0

    # Create the body of the robot
    pyrosim.Start_NeuralNetwork("brain.nndf")

    # Create sensor neurons to receive information from sensors
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

    sensor_neurons = [0, 1, 2] # Names of sensor neurons

    # Create motor neurons to move the link's joints
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

    motor_neurons = [3, 4] # Names of motor neurons

    # Generate synapses
    # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=1.0)
    # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=1.0)
    # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=4, weight=-1.0)
    # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=-1.0)

    for name in sensor_neurons:
        for motor in motor_neurons:
            pyrosim.Send_Synapse(sourceNeuronName=name, targetNeuronName=motor, weight=random.randint(-1, 1))

    # End robot generation
    pyrosim.End()


Create_World()
Generate_Body()
Generate_Brain()
