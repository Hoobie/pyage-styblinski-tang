import random
from pyage.solutions.evolution.mutation import AbstractMutation
from solution.genotype import VectorGenotype


class UniformVectorMutation(AbstractMutation):
    def __init__(self, probability=0.1, radius=100.5):
        super(UniformVectorMutation, self).__init__(VectorGenotype, probability)
        self.radius = radius

    def mutate(self, genotype):
        genotype.x = genotype.x + random.uniform(-self.radius, self.radius)
        genotype.y = genotype.y + random.uniform(-self.radius, self.radius)
        genotype.z = genotype.z + random.uniform(-self.radius, self.radius)
        genotype.s = genotype.s + random.uniform(-self.radius, self.radius)
        genotype.t = genotype.t + random.uniform(-self.radius, self.radius)
