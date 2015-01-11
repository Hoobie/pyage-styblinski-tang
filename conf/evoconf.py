# coding=utf-8
import logging

from pyage.core import address
from pyage.core.agent.agent import generate_agents, Agent
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition
from pyage.solutions.evolution.selection import TournamentSelection

from solution.initializer import VectorInitializer
from solution.evaluation import StyblinskiTangEvaluation
from solution.crossover import AverageVectorCrossover
from solution.mutation import UniformVectorMutation

vectors = [
	[-5, -5, -5, -5, -5],
    [-4, -4, -4, -4, -4],
    [-3, -3, -3, -3, -3],
    [-2, -2, -2, -2, -2],
    [-1, -1, -1, -1, -1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5],
]

vector_nr = len(vectors)

logger = logging.getLogger(__name__)

agents_count = 5
logger.debug("%s agents", agents_count)
agents = generate_agents(
    "agent" , agents_count , Agent
    )

stop_condition = lambda: StepLimitStopCondition(10000)

minimal_energy = lambda: 10
reproduction_minimum = lambda: 90
migration_minimum = lambda: 120
newborn_energy = lambda: 100
transferred_energy = lambda: 40

evaluation = lambda: StyblinskiTangEvaluation()
crossover = lambda: AverageVectorCrossover(size=vector_nr)
mutation = lambda: UniformVectorMutation(probability=0.1, radius=1)
selection = lambda: TournamentSelection(size=vector_nr, tournament_size=vector_nr) # magic numbers xD

operators = lambda: [evaluation(), selection(), crossover(), mutation()]
initializer = lambda: VectorInitializer(size=vector_nr, lowerbound=-5, upperbound=5)

address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics(
	'fitness_%s_pyage.txt' % __name__
    )