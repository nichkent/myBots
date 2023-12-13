import pyrosim.pyrosim as pyrosim

# Start generation
pyrosim.Start_SDF("boxes.sdf")

# Define cube 1 dims
length_1 = 1
width_1 = 1
height_1 = 1

# Define cube 1 pos
x_1 = 0
y_1 = 0
z_1 = 0.5

# Define cube 2 dims
length_2 = 1
width_2 = 1
height_2 = 1

# Define cube 2 pos
x_2 = 1
y_2 = 0
z_2 = 1.5

# Add cube 2
pyrosim.Send_Cube(name="Box1", pos=[x_1, y_1, z_1], size=[length_1, width_1, height_1])

# Add cube 2
pyrosim.Send_Cube(name="Box2", pos=[x_2, y_2, z_2], size=[length_2, width_2, height_2])

# End generation
pyrosim.End()
