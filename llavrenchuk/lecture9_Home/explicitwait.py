from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="WebDrivers\chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.com/")

#driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")

time.sleep(2) #from python

driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")

driver.find_element(By.ID,"package-departing-hp-package").clear()
driver.find_element(By.ID,"package-departing-hp-package").send_keys("01/14/2020")

driver.find_element(By.ID,"package-returning-hp-package").clear()
driver.find_element(By.ID,"package-returning-hp-package").send_keys("01/19/2020")

driver.find_element(By.ID,"search-button-hp-package").click()

wait=WebDriverWait(driver,10)

element=wait.until(EC.element_to_be_clickable((By.ID, "star5")))

element.click()

time.sleep(3)

driver.quit()