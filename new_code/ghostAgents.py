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
import tests
import util
import time

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

starttime = None
class DirectedGhost(GhostAgent, SearchAgent):
    global starttime
    starttime = time.time() 
    # queues = [util.PriorityQueue()]
    # queues = [util.PriorityQueue(), util.PriorityQueue()]
    # queues = [util.PriorityQueue(), util.PriorityQueue(), util.PriorityQueue()]
    queues = [util.PriorityQueue(), util.PriorityQueue(), util.PriorityQueue(), util.PriorityQueue()]
    # queues = [util.PriorityQueue(), util.PriorityQueue(), util.PriorityQueue(), util.PriorityQueue(), util.PriorityQueue()]
    tests.populateKA4(queues)
    # populatePackagesSmall1(queues[0])
    # populatePackagesMedium2(queues[1])
    # populatePackagesMedium3(queues[2])
    # populatePackagesMedium4(queues[1])
    # populatePackagesMedium5(queues[0])


    def __init__(self, index):
        self.index = index
        GhostAgent.__init__(self, self.index)
        SearchAgent.__init__(self, fn='uniformCostSearch') 
        self.package = None # tuple of priority and destination (from priority queue)
        self.origin = None

    def getDistribution(self, state):
        self.state = state
        dist = util.Counter()
        if self.package == None:
            self.acceptPackage(state)
        else:
            x, y = state.data.agentStates[self.index].configuration.pos
            state.data.food[int(x)][int(y)] = True
        self.checkDelivery(state)  
        if self.actions is None:
            self.actions = []
        next_action = SearchAgent.getAction(self, state)
        dist[next_action] = 1.0
        dist.normalize()
        return dist

    def setPackage(self, destination, pr, priority):
        global starttime
        if pr == True:
            print (time.time() - starttime)

        self.package = Package(destination, priority)

    def getDestination(self):
        return self.package.getDestination()

    def getPriority(self):
        return self.package.getPriority()

    def acceptPackage(self, state, queue=None): 
        ghostState = state.data.agentStates[self.index]
        x,y = ghostState.configuration.pos
        
        min_dist = 9999999
        min_source = None
        for source in state.data.sources:
            if util.manhattanDistance(source, ghostState.configuration.pos) < min_dist:
                min_dist = util.manhattanDistance(source, ghostState.configuration.pos)
                min_source = source

        source_idx = state.data.sources.index(min_source)
        
        queue = DirectedGhost.queues[source_idx] # 289TODO: multiple queue support
        if not queue.isEmpty():
            next_package = queue.pop()
            self.setPackage(next_package.getDestination(), False, next_package.getPriority())
            print "Package accepted by agent ", self.index, next_package.getDestination(), source_idx

    def checkDelivery(self, state):
        ghostState = state.data.agentStates[self.index]
        x,y = ghostState.configuration.pos
        x, y = int(x), int(y)

        # complete delivery
        if self.package != None and (x, y) == self.getDestination():
            if self.package.getPriority() != 0:
                state.data.food = state.data.food.copy()
                state.data.food[x][y] = False
                state.data._foodEaten = x, y
                # Go back to a source
                ghostState.scaredTimer = 40
                print "Package delivered ", x, y

                # go to closest source using manhattan distance 
                min_dist = 9999999
                min_source = None

                keep_source = state.data.sources[0]
                for source in state.data.sources:
                    source_idx = state.data.sources.index(source)
                    queue = DirectedGhost.queues[source_idx]
                    if queue.isEmpty():
                        try:
                            state.data.sources.remove(source_idx)
                        except ValueError:
                            pass
                    elif util.manhattanDistance(source, ghostState.configuration.pos) < min_dist:
                        min_dist = util.manhattanDistance(source, ghostState.configuration.pos)
                        min_source = source

                pr = False
                go_to = min_source
                if go_to == None:
                    go_to = keep_source
                    pr = True
                self.setPackage(go_to, pr, 0)
            else:
                self.acceptPackage(state)
    
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
