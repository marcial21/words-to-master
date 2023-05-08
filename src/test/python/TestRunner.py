import unittest
from src.test.python.exception.ErrorHandlerTest import ErrorHandlerTest
from src.test.python.ui.UserInterfaceTest import UserInterfaceTest

testSuite = unittest.TestSuite()
testSuite.addTest(unittest.makeSuite(ErrorHandlerTest))
testSuite.addTest(unittest.makeSuite(UserInterfaceTest))

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)