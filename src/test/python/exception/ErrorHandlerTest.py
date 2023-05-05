import unittest

from src.main.python.exception.ErrorHandler import ErrorHandler

ERROR_01 = "ERROR: NULL INPUT"
ERROR_02 = "ERROR: EMPTY STRING"

class ErrorHandlerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.errorHandler = ErrorHandler()
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()

    def testLigma(self):
        self.assertEqual(2, 2)

    def testBalls(self):
        self.assertEqual(2, 2)

    def testValidateNonEmptyString(self):
        emptyString = ""
        self.assertEqual(ERROR_02, self.errorHandler.validateNonEmptyString(emptyString))


if __name__ == '__main__':
    unittest.main()