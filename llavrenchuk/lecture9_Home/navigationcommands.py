from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="WebDrivers\chromedriver.exe")
driver.get("https://www.facebook.com/")
print(driver.title) #
driver.get("https://dou.ua/forums/topic/13389/")
time.sleep(5)
print(driver.title)
driver.back()
time.sleep(5)
print(driver.title)
driver.forward()
time.sleep(5)
print(driver.title)