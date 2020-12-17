import unittest


class SignUpTest(unittest.TestCase):
    def test_SignupByEmail(self):
        print("this is signup by email test")
        self.assertTrue(True)

    def test_SignupByFacebook(self):
        print("this is signup by FB")
        self.assertTrue(True)

    def test_SignupByTwitter(self):
        print("this is signup by twitter")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
