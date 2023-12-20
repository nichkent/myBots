from solution import SOLUTION
import copy


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        # Define number of generations
        numberOfGenerations = 2

        # Calls solution's Evaluate method
        self.parent.Evaluate()

        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate()

        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        pass

    def Evaluate(self):
        pass

    def Select(self):
        pass
