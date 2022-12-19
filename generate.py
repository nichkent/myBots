import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

length = 1
width = 2
height = 3

x = 0
y = 1.5
z = 0.5

pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])

pyrosim.End()