import numpy

# Back leg motor values
amplitude_back_leg = numpy.pi/6
frequency_back_leg = 20
phaseOffset_back_leg = 0

# Front leg motor values
amplitude_front_leg = numpy.pi/6
frequency_front_leg = 20
phaseOffset_front_leg = numpy.pi/4

# Create a np vector filled with zeros
backLegSensorValues = numpy.zeros(1000)
# Create a np vector filled with zeros
frontLegSensorValues = numpy.zeros(1000)

# Create the vectors for movement
targetAngles_back_leg = amplitude_back_leg * numpy.sin(2 * numpy.pi * frequency_back_leg * numpy.linspace(0, 1, 1000) + phaseOffset_back_leg)
targetAngles_front_leg = amplitude_front_leg * numpy.sin(2 * numpy.pi * frequency_front_leg * numpy.linspace(0, 1, 1000) + phaseOffset_front_leg)
