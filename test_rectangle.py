import pytest
from figures import *


def test_add_square_r():
    s = Square(15)
    d = Rectangle(20, 15)
    assert s.add_square(d) == s.area + d.area, 'Сумма не сходится'


def test_area_r():
    s = Rectangle(15, 20)
    assert s.area == 15 * 20


def test_name_r():
    s = Rectangle(10, 20)
    assert s.name == "Прямоугольник"


def test_perimeter_r():
    s = Rectangle(10, 20)
    assert s.perimeter == 2 * (10 + 20)


def test_angles_r():
    s = Rectangle(10, 20)
    assert s.angles == 4
