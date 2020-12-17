from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Edge(executable_path="C:\Drivers\edgedriver_win64\msedgedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)# print title
print(driver.current_url)
time.sleep(5)        # get sleep time
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()  # getting the element and click over it
print(driver.title)
print(driver.current_url)
time.sleep(5)

#driver.close() # it will close currently focused browser tab
driver.quit() # it will close all the open windows (tabs) opened

