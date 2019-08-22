from tile import Tile


class Tiles:
    def __init__(self, SPOT):
        """ Collection of tiles """
        self.spot = SPOT
        self.middle = self.spot // 2
        self.SPACING = 100
        self.black = 0
        self.white = 255
        self.t_total = [[0] * self.spot for i in range(self.spot)]
        self.m_top = (self.middle - 1) * self.SPACING + self.SPACING // 2
        self.m_bottom = self.middle * self.SPACING + self.SPACING // 2
        self.t_total[self.middle - 1][self.middle - 1] = Tile(self.m_top,
                                                              self.m_top,
                                                              self.white)
        self.t_total[self.middle - 1][self.middle] = Tile(self.m_top,
                                                          self.m_bottom,
                                                          self.black)
        self.t_total[self.middle][self.middle - 1] = Tile(self.m_bottom,
                                                          self.m_top,
                                                          self.black)
        self.t_total[self.middle][self.middle] = Tile(self.m_bottom,
                                                      self.m_bottom,
                                                      self.white)
        self.count = 4
        self.blacks = []
        self.whites = []

    def display(self):
        """ Display tile on the board """
        self.counting_tile()
        for x in range(len(self.t_total)):
            for y in range(len(self.t_total[x])):
                if(self.t_total[x][y] is not 0):
                    self.t_total[x][y].display()

    def add_tile(self, x, y, color):
        """ Create a tile and store into tile collection"""
        if(self.t_total[x][y] == 0):
            self.count += 1
            self.t_total[x][y] = Tile(x * self.SPACING + self.SPACING // 2,
                                      y * self.SPACING + self.SPACING // 2,
                                      color)

    def counting_tile(self):
        """ Counting tile """
        self.whites = []
        self.blacks = []
        for x in range(len(self.t_total)):
            for y in range(len(self.t_total[x])):
                if(self.t_total[x][y] != 0):
                    if(self.t_total[x][y].get_color() == self.white):
                        self.whites.append((x, y))
                    elif(self.t_total[x][y].get_color() == self.black):
                        self.blacks.append((x, y))
