class RouteProblem:
    def getStartState(self):
    def isGoalState(self, state):
    def getSuccessors(self, state):
    def getCostOfActions(self, state):

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()
    explored_set = ExploredSetWithCosts()

    # Passed into helper function so we can calculate the cost of each path as we are creating it
    priority_function = lambda p: problem.getCostOfActions([a for (s, a) in p][1:])
    return helper_graph_search(problem, frontier, explored_set, priority_function)
                       

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