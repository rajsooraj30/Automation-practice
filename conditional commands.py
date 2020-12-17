from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.webpagetest.org/")

print(driver.title)
time.sleep(5)

url_field= driver.find_element_by_name("url")
print(url_field.is_displayed())
print(url_field.is_enabled())

driver.get("https://www.ironspider.ca/forms/checkradio.htm")
time.sleep(5)

red_checkbox = driver.find_element_by_css_selector("input[value=red]")
print(red_checkbox.is_enabled())
print(red_checkbox.is_selected())  # for radio buttons , checkbox , sometimes dropdowns
time.sleep(20)
print(red_checkbox.is_selected())