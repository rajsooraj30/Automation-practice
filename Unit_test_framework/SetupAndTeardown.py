#there are three types of setup and teardown which we can use
# 1st is setup and tear down method - these executes for each function i.e setup will execute before each
# function in a class and tear down method will execute after each function in a class
# 2nd is setup and tear down class - setup class will execute one time before executing the functions in the
#class and tear down class will execute one time after the execution of all the functions
# 3rd is setup module and tear down module - setup module will execute before executing a module and tearch down
#module will execute after executing a module

import unittest

def setUpModule():           #set up module will ececute first in the module
    print("setup module")

def tearDownModule():
    print("teardown module") # tear down module will execute at last of the module

class TestScript2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):         # set up class will execute before all the functions
        print("Set up class")

    @classmethod
    def tearDownClass(cls):       # teardown class will execute after all the functions
        print("tear down class")
    @classmethod
    def setUp(self):                  # set up method will execute before every function
        print("setup method")
    @classmethod
    def tearDown(self):               # teardown method will execute after every function
        print("teardown method")
    def test1(self):
        print("test1")
    def test2(self):
        print("test2")
    def test3(self):
        print("test3")
    def test4(self):
        print("test4")

if __name__ == "__main__":
    unittest.main()
