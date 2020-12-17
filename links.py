import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/s?k=mobiles&hvadid=82326127549554&hvbmt=be&hvdev=c&hvqmt=e&tag=msndeskstdin-21&ref=pd_sl_4oe1cksddi_e")

links = driver.find_elements(By.TAG_NAME,'a')  # finds all the links in page
print(links)       # print the list of links
print(len(links))  # print total links in the page

for link in links: # prints all the link texts in the page
    print(link.text)

# click on a particular link
driver.maximize_window()
time.sleep(4)
driver.find_element(By.LINK_TEXT,"Privacy Notice").click()


