from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://aliexpress.ru/home.htm")
wait = WebDriverWait(driver, 10)
try:
    el = driver.find_element_by_css_selector(".close-layer")
    el.click()
    wait.until(EC.staleness_of(el))
finally:
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-role=join-link]")))
    search = driver.find_element_by_css_selector(".search-key")
    enter = driver.find_element_by_css_selector("span.join-btn > a")
    search.send_keys("Желтый человека нога")
    search.send_keys(Keys.ENTER)
    # wait.until(EC.staleness_of(enter))
    product_list = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li.list-item')))
    current = driver.current_window_handle
    product_list.pop(0).click()
    all_windows = driver.window_handles
    for each in all_windows:
        if each != current:
            driver.switch_to.window(each)
            break
    country_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.sku-property-list")))
    china = country_list.pop(0)
    china.find_element_by_css_selector('.sku-property-text').click()
    cost = driver.find_element_by_css_selector("div.product-shipping-price > span")
    text = cost.text
    more = driver.find_element_by_css_selector("span.next-input-group-addon.next-after > button")
    more.click()
