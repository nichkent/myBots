from solution import SOLUTION
import copy
import constants as c


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}

        for entry_key in range(c.populationSize - 1):
            self.parents[entry_key] = SOLUTION()

    def Evolve(self):
        for parent in self.parents:
            # Calls solutions Evaluate method with graphics
            self.parents[parent].Evaluate("GUI")


        # for currentGeneration in range(c.numberOfGenerations):
        #     # Rest of the generations are w/o graphics
        #     self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate("DIRECT")

        self.Print()

        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent.fitness = self.child.fitness

    def Print(self):
        print("\n", self.parent.fitness, self.child.fitness)

    def Show_Best(self):
        pass
        # # Call the final parent with graphics to see imporvement
        # self.parent.Evaluate("GUI")
