from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# browse exposes an executable file
# Through Selenium test we need to invoke the executable file which will then invoke actual browser
driver = webdriver.Chrome(executable_path="C:\\py\\100\\chromedriver.exe")

driver.get("https://www.google.co.in/")

print(driver.title)
print(driver.current_url)

driver.close()
# exit multiple window
driver.quit()