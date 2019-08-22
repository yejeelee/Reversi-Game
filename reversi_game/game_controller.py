from board import Board
from computer_ai import Computer_Ai


class GameController:
    """Maintains the state of the game."""
    def __init__(self, WIDTH, HEIGHT, SPOT):
        self.game_on = True
        self.SPOT = SPOT
        self.SPACING = 100
        self.comp = Computer_Ai(self.SPOT)
        self.board = Board(WIDTH, HEIGHT, self.SPOT)
        self.black_wins = False
        self.white_wins = False
        self.tie = False
        self.computer_turn = False
        self.player_turn = True
        self.p_no_move = 0
        self.c_no_move = 0
        self.black = 0  # color of black
        self.white = 255  # color of white

    def no_more_move(self):
        """ Returns True if there is no move for both Computer and Player """
        if (self.p_no_move + self.c_no_move == 2):
            return True
        return False

    def player(self):
        """ To see if player's legal move exist """
        legal = self.board.legal_move(self.black)
        if(len(legal) == 0):
            self.p_no_move = 1
            print("No legal move for player!")
            self.computer_turn = True
            self.player_turn = False

    def player_make_move(self, x, y):
        """ Player's move """
        self.p_no_move = 0
        x = x // self.SPACING
        y = y // self.SPACING
        if(self.board.is_valid(x, y, self.black) is True):
            self.board.flip(x, y, self.black)
            self.player_turn = False
            self.computer_turn = True

    def computer_make_move(self):
        """ Computer's move """
        print("Computer turn")
        legal = self.board.legal_move(self.white)
        if(len(legal) == 0):
            self.c_no_move = 1
            print("No legal move for computer!")
        else:
            self.c_no_move = 0
            best = self.comp.best_move(legal)
            if(self.board.is_valid(best[0], best[1], self.white) is True):
                self.board.flip(best[0], best[1], self.white)
        self.player_turn = True
        print("Player turn")
        self.computer_turn = False

    def winner(self, black, white):
        """announce the winner when black or white wins or tie"""
        fill(255)
        rect(150, 150, 150, 80, 7)
        fill(0)
        textSize(20)
        if self.tie:
            text("It's Tie", 160, 180)
        elif self.black_wins:
            text("Black WINS", 160, 180)
        elif self.white_wins:
            text("White WINS", 160, 180)
        result = "black: " + str(black)
        text(result, 160, 200)
        result = "white: " + str(white)
        text(result, 160, 220)

    def update(self):
        """Action playing while game is playing """
        if(self.game_on is True and
           (self.player_turn is True or self.computer_turn is True)):
            self.board.display()
            if(self.board.tiles.count == self.SPOT * self.SPOT or
               self.no_more_move()):
                self.player_turn = False
                self.computer_turn = False
                if(self.no_more_move()):
                    print("No legal move for both!")
                print("Game Over!")
                if(len(self.board.tiles.blacks) ==
                   len(self.board.tiles.whites)):
                    self.tie = True
                elif(len(self.board.tiles.blacks) >
                     len(self.board.tiles.whites)):
                    self.black_wins = True
                elif(len(self.board.tiles.whites) >
                     len(self.board.tiles.blacks)):
                    self.white_wins = True
                self.winner(len(self.board.tiles.blacks),
                            len(self.board.tiles.whites))
        elif(self.game_on is False):
            return
        elif(self.player_turn is False and self.computer_turn is False):
            self.make_record()

    def make_record(self):
        """ Take the users name to make record """
        answer = self.input('enter your name: ')
        if answer:
            print('hi ' + answer + '! Your answer has been recorded.')
            self.record_score(answer, len(self.board.tiles.blacks))
            self.game_on = False
        else:
            self.game_on = False  # Canceled dialog will turn off

    def record_score(self, answer, score):
        """ Record the score, if its highest place it on the top"""
        f = open('scores.txt', 'r+')
        new_first_line = str(answer) + ' ' + str(score) + '\n'
        if not f.read(1):
            f.write(new_first_line)
        else:
            first_line = f.readline().split()
            if int(first_line[-1]) < score:
                f.seek(0)
                whole = f.readlines()
                f.seek(0, 0)
                f.write(new_first_line)
                for line in whole:
                    f.writelines(line)
            else:
                f.write(new_first_line)
        f.close()

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)
