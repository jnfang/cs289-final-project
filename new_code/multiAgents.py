# HW 2
# Fatma Akcay and Luciano Arango


# multiAgents.py
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # print "reflex agent get action"

        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        currentPos = currentGameState.getPacmanPosition()
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()

        if len(newFood.asList()) == 0:
          return 9999999


        BadStates = {}
        for ghostState in newGhostStates:
          ghostPos = ghostState.getPosition()
          BadStates[ghostPos] = True
          BadStates[ (ghostPos[0] + 1, ghostPos[1]) ] = True
          BadStates[ (ghostPos[0] , ghostPos[1]+ 1) ] = True
          BadStates[ (ghostPos[0] - 1, ghostPos[1]) ] = True
          BadStates[ (ghostPos[0], ghostPos[1] -1 ) ] = True
        if newPos in BadStates:
          return -99999
        mini = 9999999
        mini_food = None

        for foodie in newFood.asList():
          distance = manhattanDistance(currentPos, foodie)
          if distance < mini:
            mini = distance
            mini_food = foodie

        current_dist = manhattanDistance(currentPos, mini_food)
        new_dist = manhattanDistance(newPos, mini_food)
        if new_dist < current_dist:
          return 99999


        # newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return 0

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """

        def find_max(gameState, d, agent):
          max_val = -9999999
          max_action = None
          for action in gameState.getLegalActions(0):
            new_game = gameState.generateSuccessor(0, action)
            new_val = minimax(new_game, d, agent + 1)
            if max_val <= new_val:
              max_val = new_val
              max_action = action
          return max_val, max_action

        def minimax(gameState, d, agent):

          if d == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
          if agent == gameState.getNumAgents() -1 :
            d -= 1
          agent = agent % gameState.getNumAgents()
          if agent == 0:
            max_val, max_action = find_max(gameState, d, agent)
            if d == self.depth:
              return max_action
            else:
              return max_val
          else:
              min_value = 9999999
              for action in gameState.getLegalActions(agent):
                new_game = gameState.generateSuccessor(agent, action)
                new_val = minimax(new_game, d, agent + 1)
                if min_value >= new_val:
                  min_value = new_val
              return min_value

        return minimax(gameState, self.depth , 0)



class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def find_max(gameState, d, agent, BestMax,BestMin):
          max_val = -9999999
          max_action = None
          for action in gameState.getLegalActions(0):
            new_game = gameState.generateSuccessor(0, action)
            new_val = alpha_beta(new_game, d, agent + 1, BestMax,BestMin)
            if max_val <= new_val:
              max_val = new_val
              max_action = action
            if max_val > BestMin:
              return max_val, max_action
            if max_val > BestMax:
              BestMax = max_val
          return max_val, max_action

        def alpha_beta(gameState, d, agent, BestMax, BestMin):

          if d == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
          if agent == gameState.getNumAgents() -1 :
            d -= 1
          agent = agent % gameState.getNumAgents()
          if agent == 0:
            max_val, max_action = find_max(gameState, d, agent, BestMax, BestMin)
            if d == self.depth:
              return max_action
            else:
              return max_val
          else:
              min_value = 9999999
              for action in gameState.getLegalActions(agent):
                new_game = gameState.generateSuccessor(agent, action)
                new_val = alpha_beta(new_game, d, agent + 1,  BestMax, BestMin)
                if min_value >= new_val:
                  min_value = new_val
                if min_value < BestMax:
                  return min_value
                if min_value < BestMin:
                  BestMin = min_value
              return min_value

        return alpha_beta(gameState, self.depth , 0, -999999999, 999999999)

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"

        def find_max(gameState, d, agent):
          max_val = -9999999
          max_action = None
          for action in gameState.getLegalActions(0):
            new_game = gameState.generateSuccessor(0, action)
            new_val = expectimax(new_game, d, agent + 1)
            if max_val <= new_val:
              max_val = new_val
              max_action = action
          return max_action, max_val

        def expectimax(gameState, d, agent):
          if d == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
          if agent == gameState.getNumAgents() -1 :
            d -= 1
          agent = agent % gameState.getNumAgents()
          if agent == 0:
            max_action, expected_value = find_max(gameState, d, agent)
            if d == self.depth:
              return max_action
            else:
              return expected_value
          else:
              expected_value = 0
              for action in gameState.getLegalActions(agent):
                new_game = gameState.generateSuccessor(agent, action)
                expected_value += expectimax(new_game, d, agent + 1)
              return expected_value/len(gameState.getLegalActions(agent))

        return expectimax(gameState, self.depth , 0)



def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    import random

    position = currentGameState.getPacmanPosition()
    foodList = currentGameState.getFood().asList()
    if currentGameState.isWin():
      return 999999999 + random.random()
    elif currentGameState.isLose():
      return -9999999999

    def manhattan_dist(xy1, xy2):
      return abs(xy2[0] - xy1[0]) + abs(xy2[1] - xy1[1])

    def shortestPath(Posi, remainingFood):
      total = 0
      minimum = -99999999
      for food in remainingFood:
          distance = manhattan_dist(Posi, food)
          total += distance
          if minimum > distance:
            minimum = distance
      return minimum, total

    closest, all_foods = shortestPath(position, foodList)

    if len(currentGameState.getCapsules()) == 0:
      return 1000000.0/(len(foodList))  +  1.0/closest + random.random()/100
    return 100000.0/(len(foodList))  +  1.0/closest + 1.0/all_foods + 1.0/len(currentGameState.getCapsules()) + random.random()/100





# Abbreviation
better = betterEvaluationFunction

