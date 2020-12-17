from  selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
toggle = driver.find_element_by_xpath("//*[@id='HTML8']/div[1]/p[1]/a")
print(toggle.get_attribute('title'))
driver.execute_script("arguments[0].scrollIntoView();", toggle)
actions= ActionChains(driver)
actions.move_to_element(toggle).perform() #this is the commnd to perform hover action on an element

print(toggle.get_attribute('title'))
driver.quit()