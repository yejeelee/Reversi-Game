# This is the Reversi starter application
from game_controller import GameController

SPOT = 8
WIDTH = SPOT * 100
HEIGHT = SPOT * 100
DELAY = 50

gc = GameController(WIDTH, HEIGHT, SPOT)

def setup():
    print("Welcome to Othello Game!")
    print("Player turn")
    size(WIDTH, HEIGHT)
    background(0, 100, 0)
    
def draw():
    global DELAY
    gc.update()
    if(gc.player_turn is True):
        gc.player()
        if(mousePressed):
            gc.player_make_move(mouseX, mouseY)
    elif(gc.computer_turn is True):
        DELAY -= 1
        if DELAY == 0:
            gc.computer_make_move()
            DELAY = 50
