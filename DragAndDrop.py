from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

source_element = driver.find_element_by_id("draggable")
target_element = driver.find_element_by_id("droppable")

actions= ActionChains(driver)
actions.double_click(source_element).perform()
actions.drag_and_drop(source_element,target_element).perform() #draging the source element to the target element
