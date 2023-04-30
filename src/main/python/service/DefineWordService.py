from util.Logger import logger

class DefineWordService:
    def __init__(self, errorHandler, googleSearchService, userInterface, dataStorageService) -> None:
        self.errorHandler = errorHandler
        self.googleSearchService = googleSearchService
        self.userInterface = userInterface
        self.dataStorageService = dataStorageService
        self.errorCode = None
        
    def continousDictionary(self):
        logger.debug("HEHEHEH")
        while True:
            word = input("Please enter a word to define or enter 'return' to return to main menu.\n")
            self.errorCode = self.errorHandler.validateNonEmptyString(word)
            if (self.errorCode):
                print("Error, ", self.errorCode)
                continue
            
            if (self.errorHandler.isExitInvoked(word)): 
                break

            print("Looking up definition for ", word)
            definition = self.googleSearchService.getDefinition(word)
            self.userInterface.printDefinition(word, definition)


    # FOr option 3
    def newContinousStoredDictionary(self):
        self.dataStorageService.setNewActiveList()
        self.defineWordAndAddToList()

    def isValidDefinition(self, definition):
        if definition:
            return True
        else:
            return False
        
    # For option 4
    def loadContinousStoredDictionary(self):
        # Check for available lists on stack
        self.dataStorageService.loadActiveList()
        self.defineWordAndAddToList()

    def defineWordAndAddToList(self):
        while True:
            word = input("Please enter a word to define or enter 'return' to return to main menu\n")
            self.errorCode = self.errorHandler.validateNonEmptyString(word)
            if (self.errorCode):
                print("Error, ", self.errorCode)
                continue
                
            if (self.errorHandler.isExitInvoked(word)):
                break

            print("Looking up definition for ", word)
            definition = self.googleSearchService.getDefinition(word)
            self.userInterface.printDefinition(word, definition)

            if (self.isValidDefinition(definition)):
                self.dataStorageService.checkForNewWord(word, definition)


            

                