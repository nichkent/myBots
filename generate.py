import pyrosim.pyrosim as pyrosim


# Define cube 1 dims
length = 1
width = 1
height = 1

# Define cube 1 pos
x = 0
y = 0.5
z = 0

def Create_World():
    # Start generation
    pyrosim.Start_SDF("world.sdf")

    # Create cube
    pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])

    # End cube generation
    pyrosim.End()

def Create_Robot():
    # Create the body of the robot
    pyrosim.Start_URDF("body.urdf")

    # Create body
    pyrosim.Send_Cube(name="Torso", pos=[x, z, y], size=[length, width, height])

    # End robot generation
    pyrosim.End()

Create_World()
Create_Robot()