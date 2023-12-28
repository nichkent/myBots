from solution import SOLUTION
import copy
import constants as c
import os
import glob


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        # Delete all brain and fitness files at the start of each hill_climber instance
        for brain_file in  glob.glob("brain*.nndf"):
            os.remove(brain_file)
        for fitness_file in glob.glob("fitness*.txt"):
            os.remove(fitness_file)

        # Create a dictionary of parents
        self.parents = {}

        # Assign an ID var
        self.nextAvailableID = 0

        # Find the entry key and assign an id
        for entry_key in range(c.populationSize):
            self.parents[entry_key] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            # Rest of the generations are w/o graphics
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.Evaluate(self.children)

        self.Print()
        #
        # self.Select()

    def Spawn(self):
        # Create an empty dictionary
        self.children = {}

        # Iterate over the key of each parent to deepcopy the children
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])

            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent.fitness = self.child.fitness

    def Print(self):
        print()
        for key in self.parents:
            parent_fitness = self.parents[key].fitness
            child_fitness = self.children[key].fitness
            print(f"Parent {key}: {parent_fitness} Child {key}: {child_fitness}")
        print()

    def Show_Best(self):
        pass
        # # Call the final parent with graphics to see imporvement
        # self.parent.Evaluate("GUI")

    def Evaluate(self, solutions):
        for parent in solutions:
            # Calls solutions to start the sim method with graphics
            solutions[parent].Start_Simulation("DIRECT")

        for parent in solutions:
            # Calls solutions to retrieve fitness values
            solutions[parent].Wait_For_Simulation_To_End()
