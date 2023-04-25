class DefineWordService:
    def __init__(self, errorHandler, googleSearchService, userInterface, dataStorageService) -> None:
        self.errorHandler = errorHandler
        self.googleSearchService = googleSearchService
        self.userInterface = userInterface
        self.dataStorageService = dataStorageService
        self.errorCode = None
        
    def continousDictionary(self):
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

            self.dataStorageService.checkForNewWord(word)
            

                