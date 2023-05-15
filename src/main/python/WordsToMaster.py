"""
Gabriel Marcial
https://github.com/marcial21
mgabrielofficial@outlook.com

WordsToMaster.py
"""

from util.Logger import logger
from service.DefineWordService import DefineWordService
from ui.UserInterface import UserInterface
from exception.ErrorHandler import ErrorHandler
from service.GoogleSearchService import GoogleSearchService
from service.DataStorageService import DataStorageService
from service.DataImportService import DataImportService

class WordsToMaster:
    """
    Constructor which initializes all services needed by the entire program.
    """
    def __init__(self) -> None:
        # Initialize our dependencies
        self.errorHandler = ErrorHandler()
        self.googleSearchService = GoogleSearchService()
        self.userInterface = UserInterface(self.errorHandler)
        self.dataStorageService = DataStorageService(self.userInterface, self.errorHandler)
        self.defineWordService = DefineWordService(self.errorHandler, self.googleSearchService, self.userInterface, self.dataStorageService)
        self.dataImportService = DataImportService(self.dataStorageService, self.googleSearchService)

    """
    Guides the path of the program based on user's option. 

    Parameters:
        userInput - the specified option from the user
    """
    def handleUserOptions(self, userInput):
        match userInput:
            case "1":
                print("Picked 1")
            case "2":
                print("Picked 2")
                self.dataImportService.importAllFilesFromDatabase()
            case "3":
                print("Picked 3")
                self.defineWordService.newContinousStoredDictionary()
            case "4":
                print("Picked 4")
                self.defineWordService.loadContinousStoredDictionary()
            case "5":
                print("Picked 5")
                self.defineWordService.continousDictionary()
                logger.debug("Test logging")
            case "6":
                print("Picked 6")
                quit()
            case _:
                print("Please select an option listed above.")
    
    """
    Main application
    """
    def startApplication(self): 
        while True:
            self.handleUserOptions(self.userInterface.welcomeScreen())
            
app = WordsToMaster().startApplication(); 
