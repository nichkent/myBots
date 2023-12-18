import numpy


# Motor values
amplitude = numpy.pi/6
frequency = 20
phaseOffset = numpy.pi/4


# Create the vectors for movement based on a sin wave
targetAngles = amplitude * numpy.sin(2 * numpy.pi * frequency * numpy.linspace(0, 1, 1000) + phaseOffset)
