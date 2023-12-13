import pyrosim.pyrosim as pyrosim

# Start generation
pyrosim.Start_SDF("boxes.sdf")

# Define cube 1 dims
length = 1
width = 1
height = 1

# Define cube 1 pos
x = 0
y = 0
z = 0.5



# Floor loop for cube tower
for i in range(10):
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
    z = z + 1


# End generation
pyrosim.End()
