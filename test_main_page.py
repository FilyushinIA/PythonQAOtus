def test_open_main_page(driver,base_url):
	driver.get(base_url)
	title = driver.title
	assert title == 'Your Store'