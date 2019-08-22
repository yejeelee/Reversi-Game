class Tile:
    def __init__(self, x, y, c):
        """ Create tile with location and color """
        self.x = x
        self.y = y
        self.color = c
        self.DIAMETER = 90

    def display(self):
        """Draws the tile"""
        fill(self.color)
        ellipse(self.x, self.y, self.DIAMETER, self.DIAMETER)

    def get_color(self):
        """ Return the color of tile """
        return self.color

    def change_color(self, color):
        """ Change the color of tile """
        self.color = color
