import unittest
from TestCasesAndTestSuits.Package1.TC_loginTest import loginTest
from TestCasesAndTestSuits.Package1.TC_SignUpTest import SignUpTest
from TestCasesAndTestSuits.Package2.TC_PaymentReturnTest import PaymentReturnTest
from TestCasesAndTestSuits.Package2.TC_PaymentTest import PaymentTest

#Get all the test from loginTest SignUpTest paymentReturnTest PaymentTest
tc1=unittest.TestLoader().loadTestsFromTestCase(loginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)

#creating TestSuits

sanityTestSuit= unittest.TestSuite([tc1,tc2])
functionalTestSuit = unittest.TestSuite([tc3,tc4])
masterTestSuit = unittest.TestSuite([tc1,tc2,tc3,tc4])

unittest.TextTestRunner(verbosity=2).run(masterTestSuit)
