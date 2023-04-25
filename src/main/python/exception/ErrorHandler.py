class ErrorHandler:
    def __init__(self) -> None:
        self.ERROR_01 = "ERROR: NULL INPUT"
        self.ERROR_02 = "ERROR: EMPTY STRING"

    def validateNonEmptyString(self, str):
        str = str.strip()
        if str is None:
            return self.ERROR_01
        elif str == "":
            return self.ERROR_02
        else:
            return None
        
    def isExitInvoked(self, input):
        return input == "return"