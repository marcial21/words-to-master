class DataStorageService:
    def __init__(self, userInterface) -> None:
        self.activeSet = None
        self.availableSets = []
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
        if len(self.availableSets) > 1:
            userChosenKey = self.userInterface.chooseWordSet(self.availableSetsKeys)
        elif len(self.availableSets) == 0:
            self.activeSet = self.availableSets[0]
        else:
            name = input("Choose a name for your new word list: ")
            self.activeSet = []
        

    #Use dictionary, will add word to active list and its definition
    def checkForNewWord(self, word):
        # Check if our active list is empty

        print("New word added to your set!")

        print("Duplicate word! You have seen this word previously.")
    
    # Add to binary search tree
    def addToActiveSet(self):
        pass

    # Will populate the availableLists array that can be used to switch in and out of the active list.
    # Most users would probably only have one list. 
    def loadExistingWordSets(self):
        #TODO
        print("No existing word sets, will initialize a new list for you!")
    