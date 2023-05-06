import unittest

class UserInterfaceTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def testMyBalls(self):
        self.assertEqual(2, 2)

    def testYourBalls(self):
        self.assertEqual(3,3)

    # @patch('UserInterface.Logger')
    # def testPrintDefinitions(self, mockLogger):
    #     mockLogger.debug.return_value = None
    #     UserInterface.printDefinitions("hello", ["df", "df"])
    #     self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()