from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.expedia.com/")

driver.maximize_window()
time.sleep(5)
status= driver.find_element_by_id("add-flight-switch").is_selected()
print("checkbox 1 is selected : ",status)

driver.find_element_by_id("add-flight-switch").click()