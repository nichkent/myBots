from simulation import SIMULATION
import sys

# Create command line argument for simulation var
directOrGUI = sys.argv[1]

# Command line argument storage for the solution ID
solutionID = sys.argv[2]

# Create simulation
simulation = SIMULATION(directOrGUI, solutionID)

# Run simulation
simulation.Run()

# Write the fitness of each generation to a file
simulation.Get_Fitness(solutionID)




