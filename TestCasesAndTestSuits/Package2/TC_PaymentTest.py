import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentinDollar(self):
        print("payment in dollar test")
        self.assertTrue(True)
    def test_paymentinRupees(self):
        print("payment in rupees test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()