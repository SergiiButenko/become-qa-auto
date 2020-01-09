from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./win_chromedriver')
driver.get("http://www.python.org") #open the webpage
assert "Python" in driver.title #found python in title of html page
elem = driver.find_element_by_name("q") #placing cursor into the search line, q = is common html element for search 
elem.send_keys("pycon") #typing pycon into the search line
elem.send_keys(Keys.RETURN) #press ENTER
assert "No results found." in driver.page_source
# driver.close() 