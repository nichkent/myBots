import pyrosim.pyrosim as pyrosim

# Start generation
pyrosim.Start_SDF("boxes.sdf")

# Define cube 1 dims
length = 1
width = 1
height = 1

# Define cube 1 pos
x = 0
y = 0.5
z = 0

# Create cube
pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])



# End generation
pyrosim.End()
