import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0.5
z = 0.5

pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])
pyrosim.Send_Cube(name="Box2", pos=[x + 1, z, y+1], size=[length, width, height])


pyrosim.End()