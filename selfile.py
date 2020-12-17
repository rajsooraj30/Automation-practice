from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Edge(executable_path="C:\Drivers\edgedriver_win64\msedgedriver.exe")

driver.get("https://www.splittywitty.com/")

print(driver.title)
driver.close()