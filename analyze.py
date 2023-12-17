import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
targetAngles_back_leg = np.load("data/targetAngles_back_leg.npy")
targetAngles_front_leg = np.load("data/targetAngles_front_leg.npy")


plt.plot(targetAngles_back_leg, linewidth=3, label='Back Leg')
plt.legend()
plt.plot(targetAngles_front_leg, label='Front Leg')
plt.legend()
#plt.plot(backLegSensorValues, linewidth=3, label='Back Leg')
#plt.legend()
#plt.plot(frontLegSensorValues, label='Front Leg')
#plt.legend()

plt.show()
