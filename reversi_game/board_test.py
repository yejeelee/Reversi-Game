import pytest
from board import Board
from tiles import Tiles


def test_constructor():
    """ Test board constructor """
    b = Board(400, 400, 4)
    assert b.WIDTH == 400
    assert b.HEIGHT == 400
    assert b.SPOT == 4
    assert len(b.legal) == 0
    assert len(b.dir) == 8
    assert len(b.tiles.t_total) == 4
    assert b.tiles.t_total[1][1].get_color() == 255
    b = Board(800, 800, 8)
    assert len(b.tiles.t_total) == 8
    assert len(b.tiles.t_total[0]) == 8
    assert b.tiles.t_total[3][3].get_color() == 255
    assert b.tiles.t_total[4][4].get_color() == 255
    assert b.tiles.t_total[3][4].get_color() == 0
    assert b.tiles.t_total[4][3].get_color() == 0


def test_legal_move():
    """ Test board legal move """
    b = Board(400, 400, 4)
    b.tiles.counting_tile()
    lst = b.legal_move(0)
    assert (0, 1) in lst
    assert len(lst) == 4
    lst = b.legal_move(255)
    assert (2, 0) in lst
    assert len(lst) == 4


def test_flip():
    """ Test if tile flips """
    b = Board(400, 400, 4)
    b.tiles.counting_tile()
    b.legal_move(0)
    b.tiles.add_tile(0, 1, 0)
    b.flip(0, 1, 0)
    b.tiles.counting_tile()
    assert b.tiles.t_total[0][1].get_color() == 0
    assert b.tiles.t_total[1][1].get_color() == 0
    assert b.tiles.t_total[2][2].get_color() == 255
    b = Board(400, 400, 4)
    b.tiles.counting_tile()
    b.legal_move(0)
    b.tiles.add_tile(2, 0, 255)
    b.flip(2, 0, 255)
    b.tiles.counting_tile()
    assert b.tiles.t_total[2][0].get_color() == 255
    assert b.tiles.t_total[2][1].get_color() == 255
    assert b.tiles.t_total[1][2].get_color() == 0


def test_is_valid():
    """ Test if position is valid """
    b = Board(400, 400, 4)
    b.tiles.counting_tile()
    assert len(b.tiles.blacks) == 2
    lst = b.legal_move(0)
    assert (0, 1) in lst
    b.is_valid(0, 1, 0)
    b.tiles.add_tile(0, 1, 0)
    b.tiles.counting_tile()
    assert b.tiles.t_total[0][1].get_color() == 0
    assert b.tiles.t_total[1][1].get_color() == 255


def test_in_board():
    """ Test if position is in board """
    b = Board(400, 400, 4)
    assert b.in_board(1, 3) is True
    assert b.in_board(7, 6) is False
