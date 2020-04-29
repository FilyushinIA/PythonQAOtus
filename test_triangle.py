import pytest
from figures import *


def test_add_square_t():
    s = Triangle(15, 20, 25)
    d = Square(20)
    assert s.add_square(d) == s.area + d.area, 'Сумма площадей не сходится'


def test_area_t():
    s = Triangle(10, 10, 10)
    assert s.area == math.sqrt(30 * 20 * 20 * 20)


def test_name_t():
    s = Triangle(15, 20, 25)
    assert s.name == "Треугольник"


def test_perimeter_t():
    s = Triangle(15, 20, 25)
    assert s.perimeter == 15 + 20 + 25


def test_angles_t():
    s = Triangle(15, 20, 25)
    assert s.angles == 3
