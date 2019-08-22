import pytest
from tile import Tile


def test_constructor():
    """ Test tile constructor """
    t = Tile(100, 200, 0)
    assert t.x == 100
    assert t.y == 200
    assert t.color == 0
    assert t.DIAMETER == 90


def test_get_color():
    """ Test tile get_color() method """
    t = Tile(100, 200, 0)
    assert t.get_color() == 0
    t = Tile(100, 200, 255)
    assert t.get_color() == 255


def test_change_color():
    """ Test tile change_color() method """
    t = Tile(100, 200, 0)
    t.change_color(255)
    assert t.color == 255
    t = Tile(100, 200, 255)
    t.change_color(0)
    assert t.color == 0
