"""
Gabriel Marcial
https://github.com/marcial21
mgabrielofficial@outlook.com

DataStorageService.py
"""

import os
from util.HashMap import HashMap

"""
Class used to handle our data structures and data storage of word sets. Using
a complex set of lists and hash maps, we can accurately keep track of words, definitions and
word sets. Allows us to easily add new words and definitions while also switching out between
sets. 
"""
class DataStorageService:
    """
    Constructor for our service which holds the following variables and purposes:
        activeSet (HashMap):      The current hash table of word-definitions that user is interacting with.
        activeSetKey (string):    The name of the activeSet which is what we use to query that given set.
        availableSets (HashMap):  The hash table of name-word set that the user is interacting with.
        availableSetsKeys (list): A list of names that we use to query the 'availableSets' hash table.  
    """
    def __init__(self, userInterface) -> None:
        self.activeSet = None
        self.activeSetKey = None
        self.availableSets = HashMap(100)
        self.availableSetsKeys = []

        # Dependency injections
        self.userInterface = userInterface
        
    # For option 4, choose from an existing set, will default to 3 if no existing sets,
    """
    Function used for handling option 4 from our application. Will set our activeSet from any
    existing sets. If no existing sets, we will prompt user to create a new set. 
    """
    def loadActiveList(self):
        if (self.availableSets.length == 0):
            print("No available sets yet big g. Will create a new set for ya tho. \n")
            self.setNewActiveList()
            return
        
        if self.availableSets.length == 1:
            print("Set: '", self.activeSetKey, "' is now your active set!")
            return

        # Look for the existing set and choose it
        userChosenKey = self.userInterface.chooseWordSet(self.availableSetsKeys)
        self.activeSet = self.availableSets.getVal(userChosenKey)
        self.activeSetKey = userChosenKey

    # For user option 3, create new list of words
    def setNewActiveList(self):
        self.activeSet = self.createNewSet()     
        
    # Initialize a new map of word-definitions and set it as the activeSet.
    # Save its name and add this new map to our map of word sets.
    """
    Initialize a new map of word-definitions and set it as the activeSet. Save its 
    name and add this new map to our map of word sets.

    Returns:
        HashMap: The newly created word set.
    """
    def createNewSet(self):
        name = input("Choose a name for your new word list: ")
        name = name.strip()
        newMap = HashMap(10000)
        self.availableSets.setValue(name, newMap)
        self.availableSetsKeys.append(name)
        self.activeSetKey = name
        print("\nAdded new set for you named ", name)
        print("Setting", name, "as the active list.\n")
        self.activeSet = newMap
        return newMap

    # Add a new word-definitions pair to the activeSet
    def addWordDefsToActiveSet(self, word, definitions):
        self.activeSet.setValue(word, definitions)
        self.addToDatabase(word, definitions)

    # Check if our activeSet already contains an entry for the given word
    def wordAlreadyInSet(self, word):
        if self.activeSet.getVal(word):
            return True
        else:
            return False

    # TODO: User should bbe able to change a set's name
    def changeSetName(self):
        pass

    """
    Function to add our word and definitions to a text file in our database directory. Its programmed
    to write to a file named after the set's name followed by the textfile extension. So for example if
    our activeSet's name (also defined in our activeSetKey) is 'Kathy' than our method will write to 
    src/database/Kathy.txt

    Parameters:
        word (string):      The word we will write.
        definitions (list): The list of definitions for the given word.
    """
    def addToDatabase(self, word, definitions):
        file_path = "src/database/" + self.activeSetKey + ".txt"

        if os.path.exists(file_path):
            with open(file_path, "a") as f:
                self.writeWordDefToTextFile(f, word, definitions)
        else:
            with open(file_path, "w") as f:
                self.writeWordDefToTextFile(f, word, definitions)

    # Will write definitions to a file. Helper for addToDatabase
    def writeWordDefToTextFile(self, fileStream, word, definitions):
        fileStream.write(word + ":\n")
        for definition in definitions:
            fileStream.write("\t- "+ definition +"\n")
