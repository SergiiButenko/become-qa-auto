import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.expected_conditions import presence_of_element_located


#This example requires Selenium WebDriver 3.13 or newer
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com/")
driver.find_element_by_name("q").send_keys("cheese" + Keys.RETURN)
time.sleep(2) # <<<<<---- так делать только в редких случаях в виде исключения. Тут бы использовать явные ожидания
# first_result = driver.find_element_by_css_selector("h3")
# first_result.click()
second_result = driver.find_elements_by_css_selector("h3")[1]
# select second selector due to 1st is ukranian wiki
second_result.click()
casein_res = driver.find_element_by_partial_link_text('casein')
casein_res.click()
print(casein_res)
time.sleep(5)
driver.close()