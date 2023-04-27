from util.HashMap import HashMap

class DataStorageService:
    def __init__(self, userInterface) -> None:
        self.activeSet = None
        self.activeSetKey = None
        self.availableSets = HashMap(100)
        self.availableSetsKeys = []
        self.userInterface = userInterface

        #Hash map to store names of keysets and index
        #Hash map for a list of words and definitions

        ####
        ## SO this will be a hashtable of hashtables. The big one is going to be key=any given name the user chooses, and the value
        ## is there word-definition hashmap. Than query it so lets say getValue("Kathy'sList") will query this particular 
        # word-definition hashMap
        
    # Method should be called at the start of our program
    def initializeActiveList(self):
        userChosenKey = None
        if self.availableSets.size > 1:
            userChosenKey = self.userInterface.chooseWordSet(self.availableSetsKeys)
            self.activeSet = self.availableSets.getVal(userChosenKey)
            self.activeSetKey = userChosenKey
        elif self.availableSets.size == 1:
            self.activeSet = self.availableSets[0]
            self.activeSetKey = self.availableSetsKeys[0]
        else:
            self.activeSet = self.createNewSet()

        
    def createNewSet(self):
        name = input("Choose a name for your new word list: ")
        newMap = HashMap(10000)
        self.availableSets.setValue(name, newMap)
        self.availableSetsKeys.append(name)
        self.activeSetKey = name
        print("Added new set for you named ", name)
        print("Setting ", name, " as the active list.")
        self.activeSet = newMap
        return newMap
        

    #Use dictionary, will add word to active list and its definition
    def checkForNewWord(self, word, definition):
        # Check if our active list is empty
        if (len(self.activeSet) == 0):
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
    def loadExistingWordSets(self):
        #TODO
        print("No existing word sets, will initialize a new list for you!")
    