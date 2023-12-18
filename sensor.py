import pyrosim.pyrosim as pyrosim
import numpy


class SENSOR:
    def __init__(self, linkName):
        # Set the link name of the sensor
        self.linkName = linkName
        # Create a np vector filled with zeros
        self.values = numpy.zeros(1000)

    def Get_Value(self, t):
        # Get the touch sensor value
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        # Print the values of the sensors at the end
        if t == 999:
            print(self.values)
