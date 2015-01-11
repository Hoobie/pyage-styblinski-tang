from random import uniform

from pyage.core.emas import EmasAgent

from solution.genotype import VectorGenotype


def emas_initializer(energy=10, size=100, lowerbound=0.0, upperbound=1.0):
    agents = {}
    for i in range(size):
        agent = EmasAgent(VectorGenotype(uniform(lowerbound, upperbound), uniform(lowerbound, upperbound), uniform(lowerbound, upperbound), uniform(lowerbound, upperbound), uniform(lowerbound, upperbound)), energy)
        agents[agent.get_address()] = agent
    return agents