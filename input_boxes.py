from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.splittywitty.com/")
driver.implicitly_wait(5)
driver.maximize_window()
#find number of input boxes
input_box=driver.find_elements(By.CLASS_NAME,"form-control")
print(len(input_box))

#enter values in an input box
driver.find_element(By.NAME,"memName1").send_keys("Sooraj")

#find out the input box is displayed or not
status=driver.find_element(By.NAME,"memName1").is_displayed()
print("input box is displayed:",status)


