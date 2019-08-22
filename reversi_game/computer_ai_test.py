import pytest
from computer_ai import Computer_Ai


def test_computer_ai_constructor():
    """ Test Computer_ai constructor """
    c = Computer_Ai(4)
    assert c.corner == [(0, 0), (0, 3), (3, 0), (3, 3)]


def test_best_move():
    """ Test best move the computer is going to make """
    c = Computer_Ai(4)
    example = [(1, 0), (2, 0), (2, 2), (3, 3), (2, 1)]
    assert c.best_move(example) == (3, 3)
    example = [(1, 0), (2, 0), (2, 2), (2, 1)]
    assert c.best_move(example) == (1, 0)
    example = [(2, 2), (2, 1)]
    assert c.best_move(example) == (2, 2)
