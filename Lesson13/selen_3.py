from selene import by, be, have, driver
from selene import browser, config
import pytest


@pytest.fixture(scope='class')
def setup(request):

    yield browser
    browser.quit()


@pytest.mark.usefixtures('setup')
class BaseTest(object):
    pass


@pytest.mark.usefixtures('setup')
class OpenCart(BaseTest):
    config.timeout = 30
    config.start_maximized = True
    browser.open_url('https://demo.opencart.com/')

    def top_panel(self):
        browser.all(by.css('li.dropdown a'))


def test_top_panel():

    opencart = OpenCart()
    els = opencart.top_panel().first.click()

