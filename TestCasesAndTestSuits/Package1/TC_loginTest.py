import unittest

class loginTest(unittest.TestCase):
    def test_loginByEmail(self):
        print("this is login by email test")
        self.assertTrue(True)

    def test_loginByFacebook(self):
        print("this is login by FB")
        self.assertTrue(True)

    def test_loginByTwitter(self):
        print("this is login by twitter")
        self.assertTrue(True)

if __name__ =="__main__":
    unittest.main()
