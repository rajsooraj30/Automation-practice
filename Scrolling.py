from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")
driver.maximize_window()
driver.implicitly_wait(6)
time.sleep(5)
# 1. scroll down the page till 100th px
#driver.execute_script("window.scrollBy(0,1000)","")

# 2. scroll down the page till the element is visible
# element = driver.find_element_by_xpath("//*[@id='main']/div[7]/a")
# driver.execute_script("arguments[0].scrollIntoView();", element)

# 3. scroll down the page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
