import pytest

def test_first(first_fixture):
    a = 3
    b = 5
    assert a + b == 8
