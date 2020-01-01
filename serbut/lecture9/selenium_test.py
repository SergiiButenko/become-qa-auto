from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./linux_chromedriver')
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." in driver.page_source
# driver.close()