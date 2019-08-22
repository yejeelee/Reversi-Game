import pytest
from game_controller import GameController
from board import Board
from computer_ai import Computer_Ai


def test_gc_constructor():
    """ Test gc constructor """
    gc = GameController(400, 400, 4)
    assert gc.game_on is True
    assert gc.SPOT == 4
    assert gc.black_wins is False
    assert gc.white_wins is False
    assert gc.tie is False
    assert gc.computer_turn is False
    assert gc.player_turn is True
    assert gc.p_no_move == 0
    assert gc.c_no_move == 0
    assert gc.black == 0
    assert gc.white == 255


def test_no_more_move():
    """ Test if there is no more move available for both """
    gc = GameController(400, 400, 4)
    gc.p_no_move = 1
    gc.c_no_move = 0
    assert gc.no_more_move() is False
    gc.c_no_move = 1
    assert gc.no_more_move() is True


def test_player():
    """ test player's legal move """
    gc = GameController(400, 400, 4)
    gc.board.tiles.counting_tile()
    lst = gc.board.legal_move(0)
    assert len(lst) == 4
    assert (2, 3) in lst


def test_player_move():
    """ Test player's move """
    gc = GameController(400, 400, 4)
    gc.board.tiles.counting_tile()
    lst = gc.board.legal_move(0)
    gc.player_make_move(200, 300)
    assert gc.board.tiles.t_total[2][3].get_color() == 0
    assert gc.board.tiles.t_total[2][2].get_color() == 0
    assert gc.board.tiles.t_total[2][3].get_color() == 0


def test_computer_move():
    """ Test computer's move """
    gc = GameController(400, 400, 4)
    gc.board.tiles.counting_tile()
    lst = gc.board.legal_move(0)
    gc.player_make_move(200, 300)
    gc.board.tiles.counting_tile()
    lst = gc.board.legal_move(255)
    assert len(lst) == 3
    assert gc.comp.best_move(lst) == (3, 3)
    gc.computer_make_move()
    assert gc.board.tiles.t_total[3][3].get_color() == 255
    assert gc.board.tiles.t_total[2][2].get_color() == 255
    assert gc.board.tiles.t_total[1][1].get_color() == 255


def test_record_score():
    """ Test the score.txt assuming it is an empty file """
    gc = GameController(400, 400, 4)
    gc.record_score("Jenny", 100)
    f = open('scores.txt', 'r')
    assert f.readline() == 'Jenny 100\n'
    gc.record_score("Jenny", 10)
    f = open('scores.txt', 'r')
    assert f.readline() == 'Jenny 100\n'
