import pytest


@pytest.fixture
def first_fixture():
    print('\nThis is first fixture')
    yield
    print('\nGoodby first fixture ')


