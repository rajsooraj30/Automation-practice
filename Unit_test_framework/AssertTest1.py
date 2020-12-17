import unittest
from selenium import webdriver


class TestCase3(unittest.TestCase):

    def test1(self):
        #self.driver= webdriver.Chrome(executable_path="chromedriver.exe")
        #self.driver.get("http://www.google.com/")
        #titleOfWebPage= self.driver.title
        #self.assertEqual("Googlee",titleOfWebPage,"web page title are not same ")
        #self.assertNotEqual("Googlee",titleOfWebPage,"web page title are not same ")
        #self.assertTrue(titleOfWebPage=="Google")
        #self.assertFalse(titleOfWebPage=="Google")

        # test= None
        # self.assertIsNone(test)
        # self.assertIsNotNone(test)

        # list=["sooraj","surbhi","madhu"]
        # #self.assertIn("sooraj",list,"this field is not present in the container")
        # self.assertNotIn("Sooraj",list,"this field is present in the container ")

        # Relational comparison
        #self.assertGreater(100,230,"a is not greater than b")
        #self.assertGreaterEqual(100,100)
        #self.assertLess(10,100)
        self.assertLessEqual(100,100)










if __name__ == '__main__':
    unittest.main()