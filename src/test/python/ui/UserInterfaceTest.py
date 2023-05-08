import unittest
from unittest.mock import patch
from src.main.python.ui.UserInterface import UserInterface

class UserInterfaceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.userInterface = UserInterface()
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()

    def testPrintDefinitions(self, mockLogger):
        with patch('UserInterface.logger.debug') as mockLogger:
            mockLogger.return_value = "pop"
            result = self.userInterface.printDefinitions("df", [])
        assert result == None

if __name__ == '__main__':
    unittest.main()