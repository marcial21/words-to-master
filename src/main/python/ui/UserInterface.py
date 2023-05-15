"""
Gabriel Marcial
https://github.com/marcial21
mgabrielofficial@outlook.com

UserInterface.py
"""

from util.Logger import logger

"""
A class used to handle features specific to the user interface.
"""
class UserInterface:
    """
    Constructor with no initialization of variables.
    """
    def __init__(self, errorHandler) -> None:
        self.errorHandler = errorHandler
    
    """
    Will print the word followed by its definition if exists, will specify and print that 
    no definition was found otherwise.

    Parameters:
        word (str):       The word.
        definition (str): The definition of the word we are defining.
    """
    def printDefinition(self, word, definition):
        if definition:
            print(f"\n\nThe definition of '{word}' is: \n\t'{definition}'\n\n")
        else:
            print(f"\n\tNo definition found for '{word}'\n")

    """
    Will print the word followed by its definitions if exists, will specify and print that 
    no definition was found otherwise.

    Parameters:
        word (str):         The word.
        definitions (list): A list of definitions for a given word.
    """
    def printDefinitions(self, word, definitions):
        if definitions:
            print(f"\n\nThe definition(s) of '{word}' are:")
            for definition in definitions:
                print(f"\t- {definition}")
            print("\n")
        else:
            print(f"\n\tNo definition found for '{word}'\n")

    """
    Will print a set of words and definitions to the console.

    Parameters:
        set (hashmap): The word set.
        setName (str): The name of the set.
    """
    def printSet(self, set, setName):
        logger.debug("Set name:" + setName + "\n\t"+ str(set))
        print("\n==============================YOUR WORD SET FOR '"+ setName +"'==============================================")
        for item in set.hashTable:
            if len(item) == 1:
                print("\n'"+ item[0][0] +"' has the following definition(s):")
                for definition in item[0][1]:
                    print("\t->", definition)
        print("\n==============================END OF SET================================================================")
        
    """
    Checks if given input matches a specifed string.

    Parameters:
        str: The string to check.
    """
    def printSetInvoked(self, str):
        if (str == "print"):
            return True

    """
    Returns input from the user specifying a word set key. The keys symbolizes the 
    name of a given set. Typically in sync with the name of the text file being 
    written to.

    Parameters:
        setKeys (list): A list of keys to iterate.

    Returns:
        String: The string entered by the user.
    """
    def chooseWordSet(self, setKeys):
        print("\nChoose from one of the following word set options: ")
        while True:
            for key in setKeys:
                print(key)

            chosenKey = input("Enter name of chosen set: \n")
            chosenKey = chosenKey.strip()

            if not self.errorHandler.isValidKey(chosenKey, setKeys):
                print("\nInvalid name!!! Please choose from one of the options, no mispelling :p")
                continue

            return chosenKey

    """
    A method used to print out the main options of the program so the user can choose among them.

    Returns:
        String: The option entered by the user.
    """
    def welcomeScreen(self):
        print("Welcome to WordsToMaster, your very own english literacy tool! Brought to you by Gabe.\n")
        print("Please refer to the README file to get a detailed desciption of how to use the tool and it's features.")

        print("Now please pick from some of the menu options.")

        print("1. To be implemented...")
        print("2. Import from database.")
        print("3. Create a new list of words.")
        print("4. Choose from an existing list of words. ")
        print("5. Define single word.")
        print("6. Exit program.")

        return input("Enter your choice (1-6): ")
    