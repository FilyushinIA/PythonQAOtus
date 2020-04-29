import pytest
from figures import *


def test_add_square_c():
    s = Circle(15)
    d = Square(20)
    assert s.add_square(d) == s.area + d.area, 'Сумма не сходится'


def test_area_c():
    s = Circle(15)
    assert s.area == math.pi*15*15


def test_name_s():
    s = Circle(10)
    assert s.name == "Круг"


def test_perimeter_s():
    s = Circle(10)
    assert s.perimeter == 2 * math.pi * 10


def test_angles_s():
    s = Circle(10)
    assert s.angles == 0
