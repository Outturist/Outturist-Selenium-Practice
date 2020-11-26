import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name",  action='store', default='chrome')


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    if browser_name == 'firefox':
        browser = webdriver.Firefox()
    yield browser
    browser.quit()