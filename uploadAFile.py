import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.switch_to.frame("frame-one1434677811")
element = driver.find_element_by_id("RESULT_FileUpload-10")
driver.execute_script("arguments[0].scrollIntoView();", element)
element.send_keys("C://Users//rajso//Downloads//dummy-pdf_2.pdf")
time.sleep(5)
driver.quit()