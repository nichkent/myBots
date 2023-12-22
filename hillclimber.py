from solution import SOLUTION
import copy
import constants as c


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        # Calls solutions Evaluate method with graphics
        self.parent.Evaluate("GUI")

        for currentGeneration in range(c.numberOfGenerations):
            # Rest of the generations are w/o graphics
            self.Evolve_For_One_Generation()

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
        # Call the final parent with graphics to see imporvement
        self.parent.Evaluate("GUI")
