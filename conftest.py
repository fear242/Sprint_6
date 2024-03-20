import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--window-size=1024,768')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
