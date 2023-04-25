from service.DefineWordService import DefineWordService
from ui.UserInterface import UserInterface
from exception.ErrorHandler import ErrorHandler
from service.GoogleSearchService import GoogleSearchService

class WordsToMaster:
    def __init__(self) -> None:
        # Initialize our dependencies
        self.userInterface = UserInterface()
        self.errorHandler = ErrorHandler()
        self.googleSearchService = GoogleSearchService()
        self.defineWordService = DefineWordService(self.errorHandler, self.googleSearchService, self.userInterface)

    def handleUserOptions(self, userInput):
        match userInput:
            case "1":
                print("Picked 1")
            case "2":
                print("Picked 2")
            case "3":
                print("Picked 3")
            case "4":
                print("Picked 4")
            case "5":
                print("Picked 5")
                self.defineWordService.continousDictionary()
            case "6":
                print("Picked 6")
            case _:
                print("Please select an option listed above.")




    def startApplication(self): 
        self.handleUserOptions(self.userInterface.welcomeScreen())
        # New user interface

        # New storage container tha will be empty or import 

        # New google search service
        
            
app = WordsToMaster().startApplication(); 

