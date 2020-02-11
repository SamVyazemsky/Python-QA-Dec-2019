from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10) # seconds
driver.get("https://www.google.com/")
e = driver.find_element_by_name('q')
e.send_keys(("Otus"))
e.send_keys(Keys.ENTER)
el = driver.find_element_by_id("center_col")
element = wait.until(lambda x: len(driver.find_elements_by_css_selector("center_col")) > 0)
# element = wait.until(EC.presence_of_element_located((By.ID, "center_col")))


"""
# обратите внимание, что локатор передается как tuple!
# element = wait.until(EC.presence_of_element_located((By.NAME, "q")))
# element2 = wait.until(lambda d: d.find_element_by_name("q"))
"""