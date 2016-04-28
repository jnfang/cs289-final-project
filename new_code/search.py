# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


# Used for DFS and BFS (no priority function) to test if already explored
class ExploredSet(object):
    def __init__(self):
        self.explored_set = set()

    def exploring(self, state, cost):
        self.explored_set.add(state)

    def is_member(self, state, cost):
        return state in self.explored_set

# Used for UCS, A* to test if already explored, accounting for minimizing the value 
# from the priority queue
class ExploredSetWithCosts(object):
    def __init__(self):
        self.explored_set = {}

    def exploring(self, state, cost):
        self.explored_set[state] = cost

    def is_member(self, state, cost):
        if not state in self.explored_set:
            return False
        return self.explored_set[state] <= cost

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    frontier = util.Stack()
    explored_set = ExploredSet()
    return helper_graph_search(problem, frontier, explored_set)
    

def helper_graph_search(problem, frontier, explored_set, priority_function=lambda x:None):
    start = problem.getStartState()
    
    # BFS and DFS will use the except, everything else will be in try because they use a
    # priority queue
    try:
        frontier.push([(start, None)], 0)
    except TypeError:
        frontier.push([(start, None)]) 
    
    while not frontier.isEmpty():
        path = frontier.pop()
        recent, action = path[-1]
        if problem.isGoalState(recent):
            # Parse the actions from the path, ignore the first action because it's None
            result =[a for (s, a) in path]
            return result[1:]
        q_value = priority_function(path)
        if not explored_set.is_member(recent, q_value):
            explored_set.exploring(recent, q_value)
            successors = problem.getSuccessors(recent)

            # Expand all children 
            for successor in successors:
                state, direction, _ = successor
                new_path = list(path) + [(state, direction)]
                new_path_q_value = priority_function(new_path)

                # Only count as visited if new calculatd value is lower in the queue
                if not explored_set.is_member(state, new_path_q_value):
                    if new_path_q_value is not None:
                        frontier.push(new_path, new_path_q_value)
                    else:
                        frontier.push(new_path)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    frontier = util.Queue()
    explored_set = ExploredSet()
    return helper_graph_search(problem, frontier, explored_set)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()
    explored_set = ExploredSetWithCosts()

    # Passed into helper function so we can calculate the cost of each path as we are creating it
    priority_function = lambda p: problem.getCostOfActions([a for (s, a) in p][1:])
    return helper_graph_search(problem, frontier, explored_set, priority_function)
                       

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    frontier = util.PriorityQueue()
    explored_set = ExploredSetWithCosts()

    # Passed into helper function so we can calculate the cost and the heuristic value when creating the path
    priority_function = lambda p: heuristic(p[-1][0], problem)+ problem.getCostOfActions([a for (s, a) in p][1:])
    return helper_graph_search(problem, frontier, explored_set, priority_function)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
