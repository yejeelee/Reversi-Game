
# This is the computer ai class that handles the computer AI skills
class Computer_Ai:
    def __init__(self, SPOT):
        """ construct computer's ability in board """
        self.SPOT = SPOT
        self.corner = [(0, 0), (0, self.SPOT - 1),
                       (self.SPOT - 1, 0), (self.SPOT - 1, self.SPOT - 1)]

    def best_move(self, lst):
        """ Find the best legal move """
        for pos in lst:  # if legal move is found in the corner
            if pos in self.corner:
                return pos
        for pos in lst:  # if legal move is found in the edge
            if (pos[0] == 0 or pos[1] == 0 or
               pos[0] == self.SPOT - 1 or pos[1] == self.SPOT - 1):
                return pos
        for pos in lst:
            # if legal move is found in the middle
            if ((pos[0] > 1 and pos[0] < self.SPOT - 2) and
               (pos[1] > 1 and pos[1] < self.SPOT - 2)):
                return pos
        for pos in lst:
            # if legal move is found in row and col right before edge
            return pos
