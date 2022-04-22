from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\py\\100\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
time.sleep(4)

count = len(driver.find_elements_by_xpath("//div[@class='products']"))
# assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()
driver.close()
