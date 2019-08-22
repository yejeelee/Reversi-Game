import pytest
from tiles import Tiles
from tile import Tile


def test_constructor():
    """ Test tiles constructor """
    t = Tiles(4)
    assert t.spot == 4
    assert t.middle == 2
    assert t.m_top == 150
    assert t.m_bottom == 250
    assert len(t.blacks) == 0
    assert len(t.whites) == 0
    assert len(t.t_total) == t.spot
    assert t.t_total[0] == [0] * t.spot
    assert t.t_total[t.spot - 1] == [0, 0, 0, 0]
    assert t.t_total[1][1].get_color() == 255
    assert t.t_total[1][2].get_color() == 0
    assert t.t_total[2][1].get_color() == 0
    assert t.t_total[2][2].get_color() == 255


def test_add_tile():
    """ Test if add tile properly"""
    t = Tiles(4)
    t.add_tile(1, 0, 0)
    assert t.t_total[1][0].get_color() == 0
    assert t.t_total[1][1].get_color() == 255
    assert t.t_total[1][2].get_color() == 0
    # trying to put it at a spot that is already filled a tile
    t.add_tile(1, 0, 255)
    assert t.t_total[1][0].get_color() == 0


def test_counting_tile():
    """ Test counting tiles method """
    t = Tiles(4)
    t.counting_tile()
    assert len(t.blacks) == 2
    assert len(t.whites) == 2
    t.add_tile(1, 0, 0)
    t.counting_tile()
    assert len(t.blacks) == 3
    assert len(t.whites) == 2
