from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.google.com/search?q=online+calculator")
browser.find_element_by_xpath("//*[contains(text(), '2')]").click()

browser.quit()