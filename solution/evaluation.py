from pyage.core.operator import Operator

from solution.genotype import VectorGenotype


class StyblinskiTangEvaluation(Operator):
    def __init__(self, type=None):
        super(StyblinskiTangEvaluation, self).__init__(VectorGenotype)

    def process(self, population):
        for genotype in population:
            genotype.fitness = -self.__StyblinskiTang(genotype.x, genotype.y, genotype.z, genotype.s, genotype.t)

    def __StyblinskiTang(self, x, y, z, s, t):
        return (x ** 4 - (16 * x) ** 2 + 5 * x + y ** 4 - (16 * y) ** 2 + 5 * y + z ** 4 -
                (16 * z) ** 2 + 5 * z + s ** 4 - (16 * s) ** 2 + 5 * s + t ** 4 - (16 * t) ** 2 + 5 * t) / 2