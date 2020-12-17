import unittest
from selenium import webdriver

class SearchenginesTest(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title of the page : ",self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://bing.com")
        print("title of the page :",self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()