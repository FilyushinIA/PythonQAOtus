import pytest

a = set('abracadabra')
b = set('alacazam')


class TestSet:

    def test_letters_in_a_but_not_in_b(self):
        assert a - b == {'d', 'b', 'r'}

    def test_letters_in_a_or_b_or_both(self):
        assert a | b == {'a', 'b', 'm', 'c', 'r', 'z', 'l', 'd'}

    def test_letters_in_both_a_and_b(self):
        assert a & b == {'a', 'c'}

    def test_letters_in_a_or_b_but_not_both(self):
        assert a ^ b == {'r', 'd', 'b', 'm', 'z', 'l'}

    @pytest.mark.parametrize('letters', 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    def test_letters_in_a(self, letters):
        assert letters not in a
