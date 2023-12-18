import pybullet as p


class WORLD:
    def __init__(self):
        # Set the floor
        self.planeId = p.loadURDF("plane.urdf")

        # Load world object
        p.loadSDF("world.sdf")
