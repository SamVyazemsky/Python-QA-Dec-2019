from selene import browser, config
from selene import by, be, have
import pytest


# def test_google():
#
#     config.timeout = 10
#     browser.open_url('https://google.com/ncr')
#     browser.\
#         element(by.name('q')).\
#         should(be.blank).\
#         type('selenium').\
#         press_enter()
#     results = browser.\
#         elements('div.g').\
#         should(have.size(16))
#     results.\
#         should(have.exact_text('Selenium automates browsers'))
#     browser.quit()


def test_otus():
    browser.open_url('https://otus.ru/')
    # print(browser.title())  # 'Онлайн курсы для профессионалов'
    browser.element(by.text('Отзывы')).click()
    el = browser.elements(by.css('.review-tile')).first().text
    print(el)
    browser.should(have.text('Selenium'))