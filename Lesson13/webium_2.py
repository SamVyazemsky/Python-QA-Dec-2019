from selenium.webdriver.common.by import By
from webium import Find, BasePage


class Header(object):
    info = Find(by=By.CSS_SELECTOR, value='.about-info__text')
    students = Find(by=By.CSS_SELECTOR, value='.about-progress__title')


class StructuredPage(BasePage):
    # here we are just grouping Header elements together without any influence on actual search
    header = Find(Header)

    def __init__(self):
        super(StructuredPage, self).__init__(url='https://otus.ru/about/')


if __name__ == '__main__':
    page = StructuredPage()
    page.open()
    print(page.header.info.text)
    print(page.header.students.text)
    page._driver.quit()