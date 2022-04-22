from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\py\\100\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_xpath("//input[@name='name']").send_keys("NAVEEN")

driver.find_element_by_name("email").send_keys("nkv@gmail.com")

driver.find_element_by_css_selector("input[id='exampleInputPassword1']").send_keys("abcdefgh")

driver.find_element_by_id("exampleCheck1").click()

# driver.find_element_by_xpath("//input[@type='submit']").click()

driver.find_element_by_xpath("//input[@type='submit']").click()

# print(driver.find_element_by_class_name("alert-success").text)
message = driver.find_element_by_class_name("alert-success").text


assert "success" in message



time.sleep(10)

driver.close()


