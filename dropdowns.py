import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/s?k=mobiles&hvadid=82326127549554&hvbmt=be&hvdev=c&hvqmt=e&tag=msndeskstdin-21&ref=pd_sl_4oe1cksddi_e")

drop_down= Select(driver.find_element_by_xpath("//*[@id='searchDropdownBox']"))

# select by visible text
drop_down.select_by_visible_text("Baby")

#select by value
time.sleep(5)
drop_down.select_by_value("Furniture")

#select by index
time.sleep(3)
drop_down.select_by_index(2)

# get the count of values in a dropdown
print(len(drop_down.options))

# get the values of the dropdown
for x in drop_down.options:
    print(x.text)