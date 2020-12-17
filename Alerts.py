# there are two types of alert commands
# switch_to_alert().accept()  --> it click on the accept or ok button of alert
# switch_to_alert().cancel()  --> it cancels the alert

from selenium import webdriver
import time

    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_xpath('''//*[@id="HTML9"]/div[1]/button''').click()
time.sleep(5)
#driver.switch_to_alert().accept()  # this will accept the alert
#driver.switch_to_alert().dismiss() # this will dissmiss the alert
driver.switch_to.alert.dismiss() # as per new python version the above statement is depriciated so the new method is this

driver.switch_to.alert.accept() # as per new python version the above statement is depriciated so the new method is this


