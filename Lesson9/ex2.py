from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# driver.implicitly_wait(10)
driver.get("https://pagination.js.org/")
wait = WebDriverWait(driver, 10)  # seconds
demo1 = driver.find_element_by_id("demo1")
items = demo1.find_elements_by_css_selector(".data-container ul li")
print(items.pop(0).text)
pagination = demo1.find_elements_by_css_selector(".paginationjs-pages ul li")
pagination.pop(2).click()
# wait.until(EC.staleness_of(items.pop(0)))
items = demo1.find_elements_by_css_selector(".data-container ul li")
print(items.pop(0).text)
driver.quit()
