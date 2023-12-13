import pyrosim.pyrosim as pyrosim


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


def Create_Robot():
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
    pyrosim.Send_Cube(name="FrontLeg", pos=[x - .5, z, y - 1], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[x - .5, z, y + 1.5])
    pyrosim.Send_Cube(name="Torso", pos=[x, z, y + 2], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[x + .5, z, y + 1.5])
    pyrosim.Send_Cube(name="BackLeg", pos=[x + .5, z, y - 1], size=[length, width, height])


    # End robot generation
    pyrosim.End()


Create_World()
Create_Robot()
