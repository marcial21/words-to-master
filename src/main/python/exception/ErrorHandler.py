"""
Gabriel Marcial
https://github.com/marcial21
mgabrielofficial@outlook.com

ErrorHandler.py
"""

"""
A class used to handle errors across the program.
"""
class ErrorHandler:
    """
    Constructor which initializes error codes.
    """
    def __init__(self) -> None:
        self.ERROR_01 = "ERROR: NULL INPUT"
        self.ERROR_02 = "ERROR: EMPTY STRING"

    """
    Checks if a given string is empty.

    Parameters:
        str:    The sring to check

    Returns:
        String: The specified error code.
        Null:   None if string was not empty.
    """
    def validateNonEmptyString(self, str):
        str = str.strip()
        if str is None:
            return self.ERROR_01
        elif str == "":
            return self.ERROR_02
        else:
            return None
        
    """
    Checks if a string is passed that signifies return.

    Parameters:
        String: The input from user.

    Returns:
        Bool: True if input is equal to 'return', false otherwise.
    """
    def isExitInvoked(self, input):
        return input == "return"
    