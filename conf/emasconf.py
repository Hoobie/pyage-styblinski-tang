# coding=utf-8
import logging

from pyage.core import address

from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition

from pyage.elect.naming_service import NamingService
from pyage.solutions.evolution.crossover import AverageFloatCrossover
from pyage.solutions.evolution.mutation import UniformFloatMutation
from solution.evaluation import StyblinskiTangEvaluation

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
logger.debug("EMAS, %s agents", agents_count)
agents = root_agents_factory(agents_count, AggregateAgent)

stop_condition = lambda: StepLimitStopCondition(10000)

agg_size = 40
aggregated_agents = lambda: emas_initializer(
	votes = vectors, candidate = 1,size=agg_size, energy=40
	)

emas = EmasService

minimal_energy = lambda: 10
reproduction_minimum = lambda: 90
migration_minimum = lambda: 120
newborn_energy = lambda: 100
transferred_energy = lambda: 40

evaluation = StyblinskiTangEvaluation
crossover = AverageFloatCrossover
mutation = lambda: UniformFloatMutation(probability=1, radius=1)

address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics(
	'fitness_%s_pyage.txt' % __name__
    )

naming_service = lambda: NamingService(
	agents_count, agg_size
    )