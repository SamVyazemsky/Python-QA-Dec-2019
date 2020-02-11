import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(browser):
    """

    """
    browser.get("https://www.google.com//")
    element = browser.find_element_by_css_selector("*[name=q]")
    element.send_keys("Python Zen")
    element.send_keys(Keys.ENTER)
    assert browser.title == 'python zen - Поиск в Google'
