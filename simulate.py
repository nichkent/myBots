from simulation import SIMULATION
import sys

# Create command line argument storage var
directOrGUI = sys.argv[1]

# Create simulation
simulation = SIMULATION(directOrGUI)

# Run simulation
simulation.Run()

simulation.Get_Fitness()




