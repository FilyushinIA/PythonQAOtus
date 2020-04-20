import requests
import pytest

API = 'https://api.openbrewerydb.org/'
LIST = API + 'breweries/'
SEARCH = LIST + 'search'
AUTOCOMPLETE = LIST + 'autocomplete'


@pytest.mark.parametrize('numbers', [-10, 20, 51, 100])
def test_breweries_per_page(numbers):
    """TEST: Numbers of Breweries in list"""
    r = requests.get(url=LIST + '?per_page={}'.format(numbers))
    expected = numbers
    if numbers > 50:
        expected = 50
    elif numbers <= 0:
        expected = 20
    assert len(r.json()) == expected


@pytest.mark.parametrize('filters', [['by_city', 'san_diego'], ['by_name', 'cooper'], ['by_state', 'ohio']])
def test_list_breweries_with_filter(filters):
    """TEST: Filters of Breweries"""
    r = requests.get(url=LIST, params={filters[0]: filters[1]})
    assert r.status_code == 200
    assert len(r.json()) > 0

@pytest.mark.parametrize('search_str', ['dog', 'man'])
def test_search_brewerie(search_str):
    r = requests.get(url=SEARCH, params={'query': search_str})
    r_json = r.json()[:5]  # output result is limited, else the test falls (it's a site's bug)
    assert r.status_code == 200
    assert len(r_json) > 0
    for brwr in r_json:
        assert brwr['name'].lower().count(search_str) > 0


@pytest.mark.parametrize('auto_str', ['dark', 'sun'])
def test_autocomplete(auto_str):
    """ TEST: output results for autocomplete is correct"""
    r = requests.get(url=AUTOCOMPLETE, params={'query': auto_str})
    assert r.status_code == 200
    for n in r.json():
        assert n['name'].lower().count(auto_str) > 0

def test_get_a_single_brewery():
    """ TEST: all fields are filled"""
    r = requests.get(LIST + '5404')
    r_json = r.json()
    for key in r_json:
        assert r.json()[key] != ''




