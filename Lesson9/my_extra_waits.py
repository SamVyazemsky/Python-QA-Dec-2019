from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class waittest:
    def __init__(self, locator, attr, value):
        self._locator = locator
        self._attribute = attr
        self._attribute_value = value

    def __call__(self, driver):
        try:
            element = driver.find_element_by_css_selector(self._locator)
        except:
            Exception
        finally:
            if element.get_attribute(self._attribute) == self._attribute_value:
                return element
            else:
                return False


driver = webdriver.Chrome()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)  # seconds
driver.get("https://www.google.com/")
e = driver.find_element_by_name('q')
e.send_keys(("Otus"))
e.send_keys(Keys.ENTER)
element = WebDriverWait(driver, 10).until(waittest('.g', 'lang', 'ru-RU'))
print(element.text)
