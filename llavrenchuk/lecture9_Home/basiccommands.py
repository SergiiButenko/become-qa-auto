from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="WebDrivers\chromedriver.exe")

driver.get("https://sushiwok.ua/")

print(driver.title)  #returns the title of the page
print(driver.current_url)  # returns URL of the page

driver.find_element_by_link_text("Доставка").click()

time.sleep(5)

driver.close()  #currently focussed browser

driver.quit() # closes all browsers