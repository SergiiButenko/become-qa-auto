# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser = webdriver.Chrome()
# browser.get('http://www.google.com')
#
# # try:
# #     element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "gbqfq")))
# # finally:
# #     browser.quit()
#
# element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "gbqfq")))
# search = browser.find_element_by_name('q')
# search.send_keys("cheese")


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://www.google.com')

search = browser.find_element_by_name('q')
search.send_keys("cheese")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results
browser.quit()