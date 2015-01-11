from pyage.solutions.evolution.crossover import AbstractCrossover
from solution.genotype import VectorGenotype


class AverageVectorCrossover(AbstractCrossover):
    def __init__(self, size=100):
        super(AverageVectorCrossover, self).__init__(VectorGenotype, size)

    def cross(self, p1, p2):
        genotype = VectorGenotype((p1.x + p2.x) / 2.0, (p1.y + p2.y) / 2.0, (p1.z + p2.z) / 2.0, (p1.s + p2.s) / 2.0, (p1.t + p2.t) / 2.0)
        return genotype