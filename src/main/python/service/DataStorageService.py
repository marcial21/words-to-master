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
    # Method should be called at the start of our program
    #TODO: fix for option 4
    def loadActiveList(self):
        userChosenKey = None
        if self.availableSets.length > 1:
            userChosenKey = self.userInterface.chooseWordSet(self.availableSetsKeys)
            self.activeSet = self.availableSets.getVal(userChosenKey)
            self.activeSetKey = userChosenKey
        elif self.availableSets.length == 1:
            self.activeSet = self.availableSets.getVal(self.activeSetKey)
        else:
            self.setNewActiveList()

    # For user option 3, create new list of words
    def setNewActiveList(self):
        self.activeSet = self.createNewSet()
        
        
    def createNewSet(self):
        name = input("Choose a name for your new word list: ")
        newMap = HashMap(30)
        self.availableSets.setValue(name, newMap)
        self.availableSetsKeys.append(name)
        self.activeSetKey = name
        print("Added new set for you named ", name)
        print("Setting ", name, " as the active list.")
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
                print("YOu have seen this word already!")
                return
            # Couldn't find it, now we add the word to the list
            else:
                self.activeSet.setValue(word, definition)
                print("New word added to your set!")

    # Will populate the availableLists array that can be used to switch in and out of the active list.
    # Most users would probably only have one list. 
    def importWordSets(self):
        #TODO
        pass
    