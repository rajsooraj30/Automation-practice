# winow handels are used to navigate throw the different windows
# two types of window handels are used
# driver.current_window_handle ==> get the current window handel
# driver.window_handels ==> get all the open window handels

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.selenium.dev/")
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.current_window_handle)  # get the current window handels
driver.find_element(By.XPATH,"//*[@id='banner-blm']/h3/a[1]").click()

print(driver.window_handles) # get all the window handels

for handel in driver.window_handles:
    driver.switch_to.window(handel)    #switch to the particular handel
    print(driver.title)
    if driver.title == "the Equal Justice Initiative":
        driver.close()


