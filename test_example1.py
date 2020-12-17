from selenium import webdriver
import pytest

def test_1():
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

    driver.get("https://admin-demo.nopcommerce.com/Admin")
    driver.maximize_window()
    driver.find_element_by_id("Email").clear()
    driver.find_element_by_id("Email").send_keys("admin@yourStore.com")
    driver.find_element_by_id("Password").clear()
    driver.find_element_by_id("Password").send_keys("admin")
    driver.find_element_by_css_selector("input[type=submit]").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//a[@href='#']//span[contains(text(),'Customers')]").click()
    driver.find_element_by_xpath("//span[@class='menu-item-title'][contains(text(),'Customers')]").click()
    rows= len(driver.find_elements_by_xpath("//*[@id='customers-grid']/tbody/tr"))
    print(rows)
    email_test="admin@yourStore.com"
    name_test="John Smith"
    email=""

    for row in range(1,rows+1):
        email=driver.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(row)+"]/td[2]").text
        if email==email_test:
            assert True
            break

    if email != email_test:
        assert False










