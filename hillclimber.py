from solution import SOLUTION


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        # Calls solution's Evaluate method
        self.parent.Evaluate()
