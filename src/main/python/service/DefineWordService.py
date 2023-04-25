class DefineWordService:
    def __init__(self, errorHandler, googleSearchService, userInterface) -> None:
        self.errorHandler = errorHandler
        self.googleSearchService = googleSearchService
        self.userInterface = userInterface
        self.errorCode = None
        
    def continousDictionary(self):
        while True:
            word = input("Please enter a word to define:")
            self.errorCode = self.errorHandler.validateNonEmptyString(word)
            if (self.errorCode):
                print("Error, ", self.errorCode)
                continue
            print("Looking up definition for ", word)
            definition = self.googleSearchService.getDefinition(word)
            self.userInterface.printDefinition(word, definition)

                