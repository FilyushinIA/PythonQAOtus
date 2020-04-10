import pytest


@pytest.fixture(params=[['run', 'dum'], ['clon', 'kiwi', 'win']])
def fixt_list(request):
    return request.param


class Test_List:

    def test_len(self):
        list_one = ['a', 'b', 'c']
        assert len(list_one) == 3

    def test_add(self):
        list_two = ['d', 'e', 'f', 'g']
        assert ['a', 'b', 'c'] + list_two == ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    def test_append(self):
        list_three = ['a', 'b']
        list_three.append('f')
        assert list_three == ['a', 'b', 'f']

    def test_remove(self):
        list_four = ['a', 'b', 'c', 'f']
        list_four.remove('b')
        assert list_four == ['a', 'c', 'f']

# параметризированный с помощью фикстуры
    def test_pop(self, fixt_list):
        assert fixt_list.count('virus') == 0
