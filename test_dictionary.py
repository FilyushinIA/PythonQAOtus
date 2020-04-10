import pytest

dict_one = dict(a=1, b=2, c=3)


class TestDict:

    def test_key_is_exists(self):
        assert 'a' in dict_one

    def test_add_new_value_to_dict(self):
        dct = dict_one.copy()
        dct['d'] = 4
        assert dct == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    def test_remove(self):
        dct = dict_one.copy()
        dct.pop('a')
        assert dct == {'b': 2, 'c': 3}

    def test_clear(self):
        dct = dict_one.copy()
        dct.clear()
        assert dct == {}

    @pytest.mark.parametrize('numbers', [1,2,3])
    def test_value_is_exists(self, numbers):
        assert numbers in dict_one.values()
