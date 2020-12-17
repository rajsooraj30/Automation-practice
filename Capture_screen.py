from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(6)

# method 1
driver.save_screenshot("D:\Screenshots\screenshot3.png")

#method 2
driver.get_screenshot_as_file("D:\Screenshots\screenshot2.jpg")