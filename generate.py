import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    length = 1
    width = 1
    height = 1

    x = 2
    y = 0.5
    z = 2.5

    pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])

    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    length = 1
    width = 1
    height = 1

    x = 0
    y = 0.5
    z = 0.5

    pyrosim.Send_Cube(name="Torso", pos=[x + 1, z, y + 2], size=[length, width, height])

    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[x - 1, z, y], size=[length, width, height])

    pyrosim.Send_Cube(name="FrontLeg", pos=[x, z, y], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])

    pyrosim.End()

Create_World()
Create_Robot()
