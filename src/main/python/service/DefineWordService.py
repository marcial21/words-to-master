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

            print("Looking up definition for", word + "...")
            definitions = self.googleSearchService.getMultipleDefinitions(word)
            self.userInterface.printDefinitions(word, definitions)


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
            word = input("Please enter a word to define or choose from the following options:\n" +
            "\t* Enter 'return' to return to main menu\n" +
            "\t* Enter 'print' to print out your current active list.\n")
            self.errorCode = self.errorHandler.validateNonEmptyString(word)
            if (self.errorCode):
                print("Error, ", self.errorCode)
                continue
                
            if (self.errorHandler.isExitInvoked(word)):
                break
            if (self.userInterface.printSetInvoked(word)):
                self.userInterface.printSet(self.dataStorageService.activeSet, self.dataStorageService.activeSetKey)
                continue

            if not (self.dataStorageService.wordAlreadyInSet(word)):
                print("Looking up definition for", word + "...")
                definitions = self.googleSearchService.getMultipleDefinitions(word)
                if self.isValidDefinition(definitions):
                    self.dataStorageService.addWordDefsToActiveSet(word, definitions)
                    print("New word added to your set!")
            else:
                print("Word is already in your set, looking up definition(s) for you...")
                definitions = self.dataStorageService.activeSet.getVal(word)
            
            self.userInterface.printDefinitions(word, definitions)



            

                