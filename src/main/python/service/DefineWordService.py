"""
Gabriel Marcial
https://github.com/marcial21
mgabrielofficial@outlook.com

DefineWordService.py
"""

from util.Logger import logger

"""
Our service class for defining a word. Combines all other services to work congruently in a harmonious series of
storing, importing, and querying data. All for the sole purpose of defining english words. 
"""
class DefineWordService:
    # Constructor with dependencies injected
    def __init__(self, errorHandler, googleSearchService, userInterface, dataStorageService) -> None:
        self.errorCode = None

        # Dependency injections
        self.errorHandler = errorHandler
        self.googleSearchService = googleSearchService
        self.userInterface = userInterface
        self.dataStorageService = dataStorageService
        
    # Method for simply quering google api and printing definitions to console. No storage or imports.
    def continousDictionary(self):
        logger.debug("continousDictionary")
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


    # Handler for option 3 of our program, will call our services to create a new active list
    # and call our helper function.
    def newContinousStoredDictionary(self):
        self.dataStorageService.setNewActiveList()
        self.defineWordAndAddToList()

    # Method used to check if a definition is valid simply by seeing if it exists. 
    def isValidDefinition(self, definition):
        if definition:
            return True
        else:
            return False
        
    # Handler for option 4 of our program. Will call our services to load a new activeSet and 
    # call our helper function.
    def loadContinousStoredDictionary(self):
        # Check for available lists on stack
        self.dataStorageService.loadActiveList()
        self.defineWordAndAddToList()

    """
    Function used to bring Google Search service and Data Storage services together. Will qeury word and 
    store their definitions to our datastructures and external files. As well as utlize our User Interface 
    service to let the user drive the program. 
    """
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
