from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(6)

# get cookies
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# add cookie
cookie= {'name':'sooraj','value':'1234'}

driver.add_cookie(cookie)
cookies= driver.get_cookies()
print(len(cookies))
print(cookies)

# delete cookie
driver.delete_cookie('sooraj')
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))




driver.quit()