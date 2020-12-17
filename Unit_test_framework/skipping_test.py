import unittest

class TestCase3(unittest.TestCase):

    @unittest.SkipTest       # this will skip test1
    def test1(self):
        print("test1")
    def test2(self):
        print("test2")

    @unittest.skip("i am skipping this test method because it is not ready")   # skipping with reason
    def test3(self):
        print("test3")
    @unittest.skipIf(1==1,"skipping test 4")             #skipping with condition and reason
    def test4(self):
        print("test4")
    def test5(self):
        print("test5")

if __name__ == "__main__":
    unittest.main()