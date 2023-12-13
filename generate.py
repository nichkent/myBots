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
    pyrosim.Send_Cube(name="Link0", pos=[x, z, y], size=[length, width, height])
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[x, z, y + .5])
    pyrosim.Send_Cube(name="Link1", pos=[x, z, y], size=[length, width, height])
    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[x, z, y + .5])
    pyrosim.Send_Cube(name="Link2", pos=[x, z, y], size=[length, width, height])
    pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute", position=[x, z + 1, y - .5])
    pyrosim.Send_Cube(name="Link3", pos=[x, z, y], size=[length, width, height])
    pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4", type="revolute", position=[x, z + 1, y - .5])
    pyrosim.Send_Cube(name="Link4", pos=[x, z, y], size=[length, width, height])
    pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5", type="revolute", position=[x, z, y - 1.5])
    pyrosim.Send_Cube(name="Link5", pos=[x, z, y], size=[length, width, height])
    pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6", type="revolute", position=[x, z, y - 1.5])
    pyrosim.Send_Cube(name="Link6", pos=[x, z, y], size=[length, width, height])

    # End robot generation
    pyrosim.End()


Create_World()
Create_Robot()
