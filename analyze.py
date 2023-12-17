import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
targetAngles = np.load("data/targetAngles.npy")

#print(backLegSensorValues)
#print(frontLegSensorValues)

plt.plot(targetAngles)
#plt.plot(backLegSensorValues, linewidth=3, label='Back Leg')
#plt.legend()
#plt.plot(frontLegSensorValues, label='Front Leg')
#plt.legend()

plt.show()
