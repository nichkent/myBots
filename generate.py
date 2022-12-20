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

    pyrosim.Send_Cube(name="Link0", pos=[x, z, y], size=[length, width, height])
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0, 0, 1])
    pyrosim.Send_Cube(name="Link1", pos=[x, z, y], size=[length, width, height])
    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[0, 0, 2])
    pyrosim.Send_Cube(name="Link2", pos=[x, z, y-1], size=[length, width, height])
    pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute", position=[1, 0, 2])
    pyrosim.Send_Cube(name="Link3", pos=[x, z, y-3], size=[length, width, height])
    pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4", type="revolute", position=[2, 0, 2])
    pyrosim.Send_Cube(name="Link4", pos=[x-1, z, y - 5], size=[length, width, height])

    pyrosim.End()

Create_World()
Create_Robot()
