import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Choose language')


@pytest.fixture
def language(request):
    return request.config.getoption('language')


@pytest.fixture
def chrome(language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    return webdriver.Chrome(options=options)


@pytest.fixture
def browser(request, chrome):
    yield chrome
    chrome.quit()
