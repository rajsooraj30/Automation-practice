# frames are the html pages in a web page
# to handel frames we need to use switch command in selenium that means
# we cannot directly use an element inside a frame without going into a frame
# the below are commands fr frames:-
# switch_to.frame(name)  --> this can be used if a frame has a name
# switch_to.frame(id)    --> this can be used if a fame has a id
# additionaly if we want to switch from one frame to another frame then we need to
# go back to the main page by using the below command
# switch_to.default_content()
# then we can switch to another frame

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(5)
#packageFrame
#classFrame
driver.switch_to.frame("packageListFrame")
driver.find_element(By.XPATH,"/html/body/main/ul/li[2]/a").click()

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH,"/html/body/main/div/section[1]/ul/li[1]/a").click()

driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[4]/a").click()







