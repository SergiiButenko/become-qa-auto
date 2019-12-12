from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('./chromedriver')
wait = WebDriverWait(driver, 10)
driver.get("https://google.com/ncr")
driver.find_element_by_name("q").send_keys("cheese" + Keys.RETURN)
first_result = driver.find_element_by_css_selector("h3")
print(first_result.get_attribute("textContent"))
first_result.click()
word = driver.find_element_by_partial_link_text("casein")
print(word.get_attribute('textContent'))
driver.close()
