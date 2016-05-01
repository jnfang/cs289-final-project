# ghostAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

from searchAgents import SearchAgent
from searchAgents import PositionSearchProblem
from game import Agent
from game import Actions
from game import Directions
from game import Package
import random
from util import manhattanDistance
import util

class GhostAgent( Agent ):
    def __init__( self, index ):
        self.index = index

    def getAction( self, state ):
        dist = self.getDistribution(state)
        if len(dist) == 0:
            return Directions.STOP
        else:
            return util.chooseFromDistribution( dist )

    def getDistribution(self, state):
        "Returns a Counter encoding a distribution over actions from the provided state."
        util.raiseNotDefined()

class DirectedGhost(GhostAgent, SearchAgent):
    queues = [util.PriorityQueue()]
    
    def __init__(self, index):
        self.index = index
        GhostAgent.__init__(self, self.index)
        SearchAgent.__init__(self, fn='uniformCostSearch') 
        self.package = None # tuple of priority and destination (from priority queue)
        self.origin = None
        self.populateQueue(DirectedGhost.queues[0])
        self.acceptPackage(DirectedGhost.queues[0])

    def populateQueue(self, global_queue):
        global_queue.push(Package((11, 5), 1), 1)
        global_queue.push(Package((3, 5), 1), 1)
        global_queue.push(Package((8, 5), 1), 1)
        # global_queue.push(Package((1, 1), 1), 1)

    def getDistribution(self, state):
        dist = util.Counter()
        if self.package == None:
            self.acceptPackage()
            print self.package.getDestination()
        next_action = SearchAgent.getAction(self, state)
        dist[next_action] = 1.0
        dist.normalize()
        return dist

    def setPackage(self, destination, priority):
        self.package = Package(destination, priority)

    def acceptPackage(self, queue=None): # should this be here
        if queue == None:
            queue = DirectedGhost.queues[0] # 289TODO: multiple queue support
        print queue
        next_package = queue.pop()
        print "accepting ", next_package.getDestination()
        self.setPackage(next_package.getDestination(), next_package.getPriority())
    
class RandomGhost( GhostAgent ):
    "A ghost that chooses a legal action uniformly at random."
    def getDistribution( self, state ):
        dist = util.Counter()
        for a in state.getLegalActions( self.index ): dist[a] = 1.0
        dist.normalize()
        return dist

class DirectionalGhost( GhostAgent ):
    "A ghost that prefers to rush Pacman, or flee when scared."
    def __init__( self, index, prob_attack=0.8, prob_scaredFlee=0.8 ):
        self.index = index
        self.prob_attack = prob_attack
        self.prob_scaredFlee = prob_scaredFlee

    def getDistribution( self, state ):
        # Read variables from state
        ghostState = state.getGhostState( self.index )
        legalActions = state.getLegalActions( self.index )
        pos = state.getGhostPosition( self.index )
        isScared = ghostState.scaredTimer > 0

        speed = 1
        if isScared: speed = 0.5

        actionVectors = [Actions.directionToVector( a, speed ) for a in legalActions]
        newPositions = [( pos[0]+a[0], pos[1]+a[1] ) for a in actionVectors]
        pacmanPosition = state.getPacmanPosition()

        # Select best actions given the state
        distancesToPacman = [manhattanDistance( pos, pacmanPosition ) for pos in newPositions]
        if isScared:
            bestScore = max( distancesToPacman )
            bestProb = self.prob_scaredFlee
        else:
            bestScore = min( distancesToPacman )
            bestProb = self.prob_attack
        bestActions = [action for action, distance in zip( legalActions, distancesToPacman ) if distance == bestScore]

        # Construct distribution
        dist = util.Counter()
        for a in bestActions: dist[a] = bestProb / len(bestActions)
        for a in legalActions: dist[a] += ( 1-bestProb ) / len(legalActions)
        dist.normalize()
        return dist
