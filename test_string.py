import pytest


str_empty = ''
strg = 'abcdefg'


class TestString:

    def test_length(self):
        assert len(str_empty) == 0

    def test_index_in_string(self):
        assert strg.find('d') == 3

    def test_capitalize(self):
        assert strg.capitalize() == 'Abcdefg'

    def test_replace(self):
        assert strg.replace('e', 'ё') == 'abcdёfg'

    @pytest.mark.parametrize('letters', ['205', '0000000112'])
    def test_is_decimal(self, letters):
        assert letters.isdecimal()
