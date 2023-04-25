class UserInterface:
    def __init__(self) -> None:
        pass
    
    def printDefinition(self, word, definition):
        if definition:
            print(f"The definition of '{word}' is '{definition}'")
        else:
            print(f"No definition found for '{word}'")

    def welcomeScreen(self):
        print("Welcome to WordsToMaster, your very own english literacy tool! Brought to you by big daddy Gabe.\n")
        print("Please refer to the README file to get a detailed desciption of how to use the tool and it's features.")

        print("Now please pick from some of the menu options.")

        print("1. Import word list from excel.")
        print("2. Import from textfile.")
        print("3. Create a new list of words.")
        print("4. Choose from an existing list of words. ")
        print("5. Define single word.\n")
        print("6. Exit program.")

        return input("Enter your choice (1-6): ")