import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0.5
z = 0.5

k = 0

for i in range(5):
    for j in range(5):
        for k in range(5):
            pyrosim.Send_Cube(name="Box", pos=[x + i, z + j, y + k], size=[length, width, height])

            length *= .9
            width *= .9
            height *= .9
        length = 1
        width = 1
        height = 1
    length = 1
    width = 1
    height = 1


pyrosim.End()