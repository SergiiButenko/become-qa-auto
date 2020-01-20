from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="WebDrivers\chromedriver.exe")
driver.get("https://www.facebook.com/")

email_ele=driver.find_element_by_name("email")

print(email_ele.is_displayed())
print(email_ele.is_enabled())

pass_ele=driver.find_element_by_name("pass")

print(pass_ele.is_displayed())
print(pass_ele.is_enabled())

email_ele.send_keys("user")
pass_ele.send_keys("pass")

driver.find_element_by_id("u_0_b").click()

