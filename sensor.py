import pyrosim.pyrosim as pyrosim
import numpy


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        # Create a np vector filled with zeros
        self.values = numpy.zeros(1000)

    def Get_Value(self, t):
        # Get the touch sensor value
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        if t == 999:
            print(self.values)
