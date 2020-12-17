from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
URL1  = "http://newtours.demout.com/"
URL2  = "https://www.splittywitty.com/"

driver.get(URL1)
print(driver.title)
time.sleep(5)

driver.get(URL2)
time.sleep(5)
print(driver.title)

driver.back()     # browser back
time.sleep(5)
print(driver.title)

driver.forward()   # browser forward
time.sleep(5)
print(driver.title)