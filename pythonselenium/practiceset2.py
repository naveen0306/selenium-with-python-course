from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\py\\100\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        # assert is always give true value
        assert checkbox.is_selected()   

radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()



time.sleep(2)
driver.close()

