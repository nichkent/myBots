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



# Floor loop for cube tower
# Creates the rows length-wise
for i in range(5):
    # Reset positions
    y = 0.5
    z = 0

    # Increment row length-wise on each iteration
    x = x + 1

    # Reset the dimensions of each tower's bottom cube
    length = 1
    width = 1
    height = 1
    # Creates the rows width-wise
    for j in range(5):
        # Reset position
        y = 0.5

        # Increment row width-wise on each iteration
        z = z + 1

        # Reset the dimensions of each tower's bottom cube
        length = 1
        width = 1
        height = 1
        # Creates the height
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])

            # Increment height pos of cube
            y = y + 1

            # Make each cube on top 90% of the dims of the cube below it
            length = length * .9
            width = width * .9
            height = height * .9



# End generation
pyrosim.End()
