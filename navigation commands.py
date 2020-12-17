from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")


driver.get("https://www.instagram.com/?hl=en")

print(driver.title)# print title
print(driver.current_url)
time.sleep(5)        # get sleep time
username=driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")  # getting the element and click over it
username.send_keys("foodocxotica")
password = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
password.send_keys("amsmpas@966")
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div").click()
time.sleep(10)
print(driver.title)

