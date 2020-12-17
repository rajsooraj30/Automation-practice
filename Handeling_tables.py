from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")
driver.maximize_window()
driver.implicitly_wait(5)

rows=len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
cols=len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))
print("no of rows",rows)
print("no of cols",cols)


for r in range(1,rows+1):
    for c in range(1,cols+1):
        if r==1:
            print(driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(r)+"]/th["+str(c)+"]").text,end="  ")
        else:
            print(driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text,end="  ")
    print()
driver.quit()