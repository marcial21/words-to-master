from util.Logger import logger

class UserInterface:
    def __init__(self) -> None:
        pass
    
    def printDefinition(self, word, definition):
        if definition:
            print(f"\n\nThe definition of '{word}' is: \n\t'{definition}'\n\n")
        else:
            print(f"\n\tNo definition found for '{word}'\n")

    def printDefinitions(self, word, definitions):
        if definitions:
            print(f"\n\nThe definition(s) of '{word}' are:")
            for definition in definitions:
                print(f"\t- {definition}")
            print("\n")
        else:
            print(f"\n\tNo definition found for '{word}'\n")

    def printSet(self, set, setName):
        logger.debug("Set name:" + setName + "\n\t"+ str(set))
        print("\n==============================YOUR WORD SET FOR '"+ setName +"'==============================================")
        for item in set.hashTable:
            if len(item) == 1:
                print("\n'"+ item[0][0] +"' has the following definition(s):")
                for definition in item[0][1]:
                    print("\t->", definition)
        print("\n==============================END OF SET================================================================")
        
    def printSetInvoked(self, word):
        if (word == "print"):
            return True

    def chooseWordSet(self, setKeys):
        print("Print from one of the following word set options: ")
        for key in setKeys:
            print(key)

        return input("Enter name of chosen set: \n")

    def welcomeScreen(self):
        print("Welcome to WordsToMaster, your very own english literacy tool! Brought to you by big daddy Gabe.\n")
        print("Please refer to the README file to get a detailed desciption of how to use the tool and it's features.")

        print("Now please pick from some of the menu options.")

        print("1. Import word list from excel.")
        print("2. Import from textfile.")
        print("3. Create a new list of words.")
        print("4. Choose from an existing list of words. ")
        print("5. Define single word.")
        print("6. Exit program.")

        return input("Enter your choice (1-6): ")