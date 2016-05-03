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

def populatePackagesSmall1(queue):
    queue.push(Package((1,1),1),1)
    queue.push(Package((5,5),1),1)
    queue.push(Package((6,5),1),1)
    queue.push(Package((4,2),1),1)
    queue.push(Package((5,2),1),1)
    queue.push(Package((6,2),1),1)
    queue.push(Package((8,2),1),1)
    queue.push(Package((3,1),1),1)

def populatePackagesSmall2(queue):
    queue.push(Package((4,1),1),1)
    queue.push(Package((5,2),1),1)
    queue.push(Package((7,3),1),1)
    queue.push(Package((8,3),1),1)
    queue.push(Package((1,4),1),1)
    queue.push(Package((2,4),1),1)
    queue.push(Package((7,5),1),1)
    queue.push(Package((8,5),1),1)

def populatePackagesSmall3(queue):
    queue.push(Package((2,2),1),1)
    queue.push(Package((3,2),1),1)
    queue.push(Package((6,2),1),1)
    queue.push(Package((8,2),1),1)
    queue.push(Package((1,3),1),1)
    queue.push(Package((2,3),1),1)
    queue.push(Package((3,3),1),1)
    queue.push(Package((5,3),1),1)

def populatePackagesSmall4(queue):
    queue.push(Package((6,3),1),1)
    queue.push(Package((6,4),1),1)
    queue.push(Package((8,4),1),1)
    queue.push(Package((1,5),1),1)
    queue.push(Package((5,1),1),1)
    queue.push(Package((6,1),1),1)
    queue.push(Package((7,1),1),1)
    queue.push(Package((8,1),1),1)

def populatePackagesSmall5(queue):
    queue.push(Package((1,2),1),1)
    queue.push(Package((2,2),1),1)
    queue.push(Package((3,2),1),1)
    queue.push(Package((4,2),1),1)
    queue.push(Package((2,5),1),1)
    queue.push(Package((3,5),1),1)
    queue.push(Package((4,5),1),1)
    queue.push(Package((1,3),1),1)

def populatePackagesMedium1(queue):
    queue.push(Package((17,17),1),1)
    queue.push(Package((17,17),1),1)
    queue.push(Package((1,1),1),1)
    queue.push(Package((1,8),1),1)
    queue.push(Package((4,9),1),1)
    queue.push(Package((17,13),1),1)
    queue.push(Package((17,14),1),1)
    queue.push(Package((17,15),1),1)

def populatePackagesMedium2(queue):
    queue.push(Package((17,16),1),1)
    queue.push(Package((1,13),1),1)
    queue.push(Package((1,12),1),1)
    queue.push(Package((8,4),1),1)
    queue.push(Package((8,15),1),1)
    queue.push(Package((4,5),1),1)
    queue.push(Package((1,11),1),1)
    queue.push(Package((1,10),1),1)

def populatePackagesMedium3(queue):
    queue.push(Package((1,9),1),1)
    queue.push(Package((7,2),1),1)
    queue.push(Package((7,12),1),1)
    queue.push(Package((4,8),1),1)
    queue.push(Package((4,9),1),1)
    queue.push(Package((13,15),1),1)
    queue.push(Package((1,7),1),1)
    queue.push(Package((13,11),1),1)

def populatePackagesMedium4(queue):
    queue.push(Package((17,12),1),1)
    queue.push(Package((8,11),1),1)
    queue.push(Package((17,7),1),1)
    queue.push(Package((7,3),1),1)
    queue.push(Package((7,10),1),1)
    queue.push(Package((8,2),1),1)
    queue.push(Package((17,2),1),1)
    queue.push(Package((13,9),1),1)

def populatePackagesMedium5(queue):
    queue.push(Package((13,16),1),1)
    queue.push(Package((7,11),1),1)
    queue.push(Package((7,13),1),1)
    queue.push(Package((7,15),1),1)
    queue.push(Package((8,1),1),1)
    queue.push(Package((8,3),1),1)
    queue.push(Package((4,6),1),1)
    queue.push(Package((4,7),1),1)

def populatePackagesLarge1(queue):
    queue.push(Package((18,37), 1), 1)
    queue.push(Package((16,14), 1), 1)
    queue.push(Package((32,29), 1), 1)
    queue.push(Package((33,33), 1), 1)
    queue.push(Package((26,25), 1), 1)
    queue.push(Package((37,30), 1), 1)

def populatePackagesLarge2(queue):
    queue.push(Package((33,24), 1), 1)
    queue.push(Package((12,19), 1), 1)
    queue.push(Package((21,26), 1), 1)
    queue.push(Package((4,10), 1), 1)
    queue.push(Package((34,26), 1), 1)
    queue.push(Package((3,11), 1), 1)
    queue.push(Package((29,13), 1), 1)
    queue.push(Package((14,31), 1), 1)

def populatePackagesLarge3(queue):
    queue.push(Package((21,16), 1), 1)
    queue.push(Package((14,26), 1), 1)
    queue.push(Package((7,25), 1), 1)
    queue.push(Package((2,13), 1), 1)
    queue.push(Package((19,8), 1), 1)
    queue.push(Package((3,27), 1), 1)
    queue.push(Package((35,26), 1), 1)
    queue.push(Package((8,25), 1), 1)

def populatePackagesLarge4(queue):
    queue.push(Package((21,36), 1), 1)
    queue.push(Package((31,29), 1), 1)
    queue.push(Package((15,19), 1), 1)
    queue.push(Package((36,15), 1), 1)
    queue.push(Package((14,27), 1), 1)
    queue.push(Package((35,25), 1), 1)
    queue.push(Package((7,7), 1), 1)
    queue.push(Package((17,35), 1), 1)


starttime = None
class DirectedGhost(GhostAgent, SearchAgent):
    global starttime
    starttime = time.time() 
    queues = [util.PriorityQueue()] #, util.PriorityQueue(), util.PriorityQueue(), util.PriorityQueue()]
    populatePackagesMedium5(queues[0])
    # populatePackagesSmall2(queues[1])
    # populatePackagesSmall3(queues[2])
    # populatePackagesSmall4(queues[3])


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

    def setPackage(self, destination, priority):
        global starttime
        if destination == None:
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
            self.setPackage(next_package.getDestination(), next_package.getPriority())
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

                # print len(state.data.sources)
                    # print "HELLOOOO"
                    # print (time.time() - starttime)
                    # return
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

                go_to = min_source
                if go_to == None:
                    go_to = keep_source
                self.setPackage(go_to, 0)
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
