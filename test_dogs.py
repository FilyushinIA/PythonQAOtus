import requests
import pytest

API = 'https://dog.ceo/api/'
BREED = API + 'breed/'
BREEDS = API + 'breeds/'
BREEDS_LIST_ALL = BREEDS + 'list/all'
BREEDS_RANDOM = BREEDS + 'image/random/'


def test_breeds_all():
    """TEST: LIST ALL BREEDS"""
    r = requests.get(url=BREEDS_LIST_ALL)
    assert r.status_code == 200
    assert len(r.json()['message']) == 94


def test_display_single_random():
    """ TEST: DISPLAY SINGLE RANDOM IMAGE FROM ALL DOGS COLLECTION """
    r1 = requests.get(url=BREEDS_RANDOM)
    r2 = requests.get(url=BREEDS_RANDOM)
    assert r1.json()['message'] != r2.json()['message']


@pytest.mark.parametrize('dogs', [5, 12])
def test_display_multiple_random(dogs):
    """ TEST: DISPLAY MULTIPLE RANDOM IMAGES FROM ALL DOGS COLLECTION"""
    url = BREEDS_RANDOM + str(dogs)
    r = requests.get(url=url)
    assert len(r.json()['message']) == dogs


@pytest.mark.parametrize('breed', ['bulldog', 'boxer'])
def test_images_are_jpg(breed):
    """ TEST: IMAGES FOR BREED ARE JPG"""
    url = BREED + breed + '/images'
    r = requests.get(url=url)
    assert r.status_code == 200
    for m in r.json()['message']:
        assert m[-4:] == '.jpg'


def test_all_sub_breeds():
    """ TEST: LIST ALL SUB-BREEDS FOR ONE BREED"""
    hound_sub_breeds = ["afghan", "basset", "blood", "english", "ibizan", "plott", "walker"]
    url = BREED + 'hound/list'
    r = requests.get(url=url)
    assert r.status_code == 200
    assert r.json()['message'] == hound_sub_breeds
