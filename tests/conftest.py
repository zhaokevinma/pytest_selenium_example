from pytest import fixture
from selenium import webdriver

@fixture(scope='session')
def chrome_driver():
    browser = webdriver.Chrome()
    yield browser