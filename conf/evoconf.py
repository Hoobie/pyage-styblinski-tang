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


size = 100

logger = logging.getLogger(__name__)

agents_count = 5
logger.debug("%s agents", agents_count)
agents = generate_agents(
    "agent", agents_count, Agent
)

stop_condition = lambda: StepLimitStopCondition(1000)

evaluation = lambda: StyblinskiTangEvaluation()
crossover = lambda: AverageVectorCrossover(size=size)
mutation = lambda: UniformVectorMutation(probability=0.1, radius=0.1)
selection = lambda: TournamentSelection(size=20, tournament_size=20)

operators = lambda: [evaluation(), selection(), crossover(), mutation()]
initializer = lambda: VectorInitializer(size=size, lowerbound=-5, upperbound=5)

address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics(
    'fitness_%s_pyage.txt' % __name__
)