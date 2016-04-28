 def minimax(gameState, d, maxiPlayer):

          if d == -1 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
          # if d == 3:
          #   print "FUCK ME IM FAMOUS"
          if maxiPlayer:
            #print "its a maxi turn"
            max_val = -9999999
            max_action = None
            count = 0
            for action in gameState.getLegalActions(0):
              new_game = gameState.generateSuccessor(0, action)
              new_val = minimax(new_game, d-1, False)
              #if d == self.depth:
                #print new_val
              if max_val <= new_val:
                max_val = new_val
                if d == self.depth:
                  max_action = action
                count +=1
            if d == self.depth:
              # print "count",count
              return max_action
            else:
              #print max_val
              return max_val
          else:
            #print "its a mini turn"
            actual_min = 9999999
            pac_val = 9999999
            # print "fatma likes poop"
            for x in xrange(1,gameState.getNumAgents()):
              #print "ghots", x
              # print gameState.getLegalActions(x), d
              new_action = None
              for action in gameState.getLegalActions(x):
                # print "action", action
                new_game = gameState.generateSuccessor(x, action)
                new_val = minimax(new_game, d-1, False)
                # print "new_val", new_val
                if actual_min >= new_val:
                  actual_min = new_val
                  new_action = action

              if new_action:
                new_pac = minimax(gameState.generateSuccessor(x, new_action), d-1, True)
                if pac_val >= new_pac :
                  pac_val = new_pac


            # print "actual_min", actual_min

            return pac_val

        return minimax(gameState, self.depth , True)
