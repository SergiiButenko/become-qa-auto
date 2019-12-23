
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#This example requires Selenium WebDriver 3.13 or newer
driver = webdriver.Chrome('./win_chromedriver.exe')
driver.get("https://google.com/ncr")
driver.find_element_by_name("q").send_keys("cheese" + Keys.RETURN)
first_result = driver.find_element_by_css_selector("h3")
print(first_result.get_attribute("textContent"))
viki = driver.find_element_by_tag_name('wikipedia')
viki.click()
