import pytest
from figures import *


def test_add_square_s():
    s = Square(15)
    d = Square(20)
    assert s.add_square(d) == s.area + d.area, 'Сумма не сходится'


def test_illegal_class():
    s = Square(15)
    d = 15
    assert s.add_square(d) == 'Передан неправильный класс', 'Нет сообщения о неправильном аргументе'


def test_area_s():
    s = Square(15)
    assert s.area == 15 * 15


def test_name_s():
    s = Square(10)
    assert s.name == "Квадрат"


def test_perimeter_s():
    s = Square(10)
    assert s.perimeter == 10 * 4


def test_angles_s():
    s = Square(10)
    assert s.angles == 4
