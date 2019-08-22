from tiles import Tiles


class Board:
    def __init__(self, WIDTH, HEIGHT, SPOT):
        """Create board for othello game"""
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SPACING = 100
        self.SPOT = SPOT
        self.tiles = Tiles(self.SPOT)
        self.STROKE = 3
        self.legal = []
        self.black = 0
        self.white = 255
        self.dir = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [1, 1],
                    [-1, 1], [1, -1]]

    def display(self):
        """Display the othello board"""
        strokeWeight(self.STROKE)
        for i in range(self.SPACING, self.WIDTH, self.SPACING):
            line(i, 0, i, self.WIDTH)
        for i in range(self.SPACING, self.HEIGHT, self.SPACING):
            line(0, i, self.HEIGHT, i)
        self.tiles.display()

    def flip(self, x, y, color):
        """ flip the tile of opponent color """
        black_white = []
        if(color == self.black):
            black_white = self.tiles.blacks
            other_color = self.white
        elif(color == self.white):
            black_white = self.tiles.whites
            other_color = self.black
        for direction in self.dir:
            ver, hor = x, y
            count = 0
            dir_x, dir_y = direction[0], direction[1]
            ver += dir_x
            hor += dir_y
            while(self.in_board(ver, hor) is True):
                if((count == 0 and (self.tiles.t_total[ver][hor] == 0 or
                                    (ver, hor) in black_white)) or
                   (count > 0 and self.tiles.t_total[ver][hor] == 0)):
                    break
                elif(self.tiles.t_total[ver][hor] != 0 and
                     self.tiles.t_total[ver][hor].get_color() == other_color):
                    count += 1
                    ver += dir_x
                    hor += dir_y
                elif(count > 0 and (ver, hor) in black_white):
                    for i in range(count):
                        ver -= dir_x
                        hor -= dir_y
                        self.tiles.t_total[ver][hor].change_color(color)
                    break

    def is_valid(self, x, y, color):
        """ Determine it is a valid move and add tile """
        if ((x, y) in self.legal):
            self.tiles.add_tile(x, y, color)
            return True
        return False

    def legal_move(self, color):
        """ Find all possible legal move of current player"""
        self.legal = []
        black_white = []
        if(color == self.black):
            black_white = self.tiles.blacks
            other_color = self.white
        if(color == self.white):
            black_white = self.tiles.whites
            other_color = self.black
        for pos in black_white:
            x = pos[0]
            y = pos[1]
            i = 0
            count = 0
            while(i < len(self.dir)):
                if(x == pos[0] and y == pos[1]):
                    x += self.dir[i][0]
                    y += self.dir[i][1]
                elif(self.tiles.t_total[x][y] == 0 or
                     self.tiles.t_total[x][y].get_color() == color):
                    if(count > 0 and self.tiles.t_total[x][y] == 0):
                        if((x, y) not in self.legal):
                            self.legal.append((x, y))
                    x = pos[0]
                    y = pos[1]
                    i += 1
                    count = 0
                elif(self.tiles.t_total[x][y].get_color() == other_color):
                    x += self.dir[i][0]
                    y += self.dir[i][1]
                    count += 1
                if(x < 0 or x > self.SPOT - 1 or y < 0 or y > self.SPOT - 1):
                    x = pos[0]
                    y = pos[1]
                    i += 1
                    count = 0
        return self.legal

    def in_board(self, x, y):
        return x >= 0 and x <= self.SPOT - 1 and y >= 0 and y <= self.SPOT - 1
