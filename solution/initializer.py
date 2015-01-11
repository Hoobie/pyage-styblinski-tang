from random import uniform
from pyage.core.operator import Operator
from solution.genotype import VectorGenotype


class VectorInitializer(Operator):
    def __init__(self, size=100, lowerbound=0.0, upperbound=1.0):
        super(VectorInitializer, self).__init__(VectorGenotype)
        self.size = size
        self.lowerbound = lowerbound
        self.upperbound = upperbound

    def process(self, population):
        for i in range(self.size):
            population.append(VectorGenotype(self.__randomize(), self.__randomize(), self.__randomize(), self.__randomize(), self.__randomize()))

    def __randomize(self):
        return uniform(self.lowerbound, self.upperbound)