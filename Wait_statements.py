# there are two types of wait in selenium "Implicit wait " and "Explicit wait"
# Implicit wait i applicable for all the elements in the web page. i.e by putting the implicit wait
# script will wait till all the elements in the page are displayed
# where are explicit wait can be focused to one particular element by putting the conditions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

#Implicit wait statement
driver.implicitly_wait(10)

driver.maximize_window()
driver.get("https://www.splittywitty.com/")

print(driver.title)
members= 6
names=['sooraj','parul','palak','sahil','pappu','tappu','jetha','taran','pk','john']
amount=[123,345,653,65,65,345,245,987,32,876]
for i in range(1,members-1):
    driver.find_element(By.ID,"PlusButton").click()

for i in range(1,members+1):
    mem = "memName"+str(i)
    amt = "memAmt"+str(i)
    driver.find_element(By.NAME, mem).send_keys(names[i-1])
    driver.find_element(By.NAME, amt).send_keys(amount[i-1])

driver.execute_script("window.scrollTo(0, 1000);")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"button[type=submit]").click()
time.sleep(5)
driver.execute_script("window.scrollTo(0, 1000);")
#Explicit wait statement
wait= WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/main/div[2]/div[3]/button")))
element.click()
