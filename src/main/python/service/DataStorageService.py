from util.HashMap import HashMap

#Hash map to store names of keysets and index
#Hash map for a list of words and definitions
class DataStorageService:
    def __init__(self, userInterface) -> None:
        # The current hash table of word-definition that user is using
        self.activeSet = None
        # The key for this hashmap
        self.activeSetKey = None
        # Hash map of word sets to easily lookup different sets the user may want to use
        self.availableSets = HashMap(100)
        # Keep track of our sets through the keys so we can query them easily
        self.availableSetsKeys = []

        # Dependency injections
        self.userInterface = userInterface
        
    # For option 4, choose from an existing set, will default to 3 if no existing sets,
    def loadActiveList(self):
        if (self.activeSetKey is None):
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
        
        
    def createNewSet(self):
        name = input("Choose a name for your new word list: ")
        newMap = HashMap(30)
        self.availableSets.setValue(name, newMap)
        self.availableSetsKeys.append(name)
        self.activeSetKey = name
        print("\nAdded new set for you named ", name)
        print("Setting", name, "as the active list.\n")
        self.activeSet = newMap
        return newMap
        

    def checkForNewWord(self, word, definition):
        # Check if our active list is empty
        if self.activeSet.length == 0:
            self.activeSet.setValue(word, definition)
            print("First word added to your set! '", word, "'")
        else:
            # Check if word already exists
            if self.activeSet.getVal(word):
                print("You have seen this word already!")
                return
            # Couldn't find it, now we add the word to the list
            else:
                self.activeSet.setValue(word, definition)
                print("New word added to your set!")

    def checkForNewWordMultipleDefinitions(self, word, definitions):
        # Check if our active list is empty
        if self.activeSet.length == 0:
            self.activeSet.setValue(word, definitions)
            print("First word added to your set! '", word, "'")
        else:
            # Check if word already exists
            if self.activeSet.getVal(word):
                print("You have seen this word already!")
                return
            # Couldn't find it, now we add the word to the list
            else:
                self.activeSet.setValue(word, definitions)
                print("New word added to your set!")


    # Will populate the availableLists array that can be used to switch in and out of the active list.
    # Most users would probably only have one list. 
    def importWordSets(self):
        #TODO
        pass

    #TODO: user should bbe able to change a set's name
    def changeSetName(self):
        pass