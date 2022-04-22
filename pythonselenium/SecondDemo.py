from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\py\\100\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=us")

driver.find_element_by_id("username").send_keys("NAVEEN")
driver.find_element_by_xpath("//input[@id='password']").send_keys("hfsgfyig")
# driver.find_element_by_xpath("//input[@id='password']").clear()

driver.find_element_by_id("forgot_password_link").click()
driver.find_element_by_css_selector("input[name='cancel']").click()






time.sleep(10)

driver.close()
