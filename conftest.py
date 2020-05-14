import pytest
from selenium import webdriver


def pytest_addoption(parser):
	_browser_choices = ('firefox', 'chrome', 'ie')
	parser.addoption(
		"--browser",
		action="store",
		required=True,
		help="Choice the browser for running {0}".format(_browser_choices),
	)

	parser.addoption(
		"--baseurl",
		default="http://localhost",
		action="store",
		help="This is base url"
	)


@pytest.fixture
def browser(request):
	return request.config.getoption("--browser")


@pytest.fixture
def base_url(request):
	return request.config.getoption("--baseurl")


@pytest.yield_fixture()
def driver(browser):
	if browser == 'chrome':
		options = webdriver.ChromeOptions()
		options.add_argument('-headless')
		driver = webdriver.Chrome(executable_path='drivers/', options=options)
	elif browser == 'firefox':
		driver = webdriver.Firefox(executable_path='drivers/')
	elif browser == 'ie':
		driver = webdriver.Ie()
	else:
		raise Exception('Не знаю браузера {}'.format(browser))
	driver.maximize_window()
	driver.implicitly_wait(5)
	yield driver
	driver.quit()
