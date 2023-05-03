import os
from util.HashMap import HashMap

class DataImportService:
    def __init__(self, dataStorageService, googleSearchService) -> None:
        self.dataStorageService = dataStorageService
        self.googleSearchService = googleSearchService
        
    # Query google service for definitions
    # populate this hash map with word definitions
    # write to that same file the word definitions via appendage
    def populateWordDefToHashMap(self, map, txtLines, filePath):
        textLines = [line.replace('\n', '').replace('\t','') for line in txtLines]
        for line in textLines:
            # if line ends with ':' we don't need to write defintions to the file
            if line.endswith(':'):
                word = line[:-1]
                definitions = self.googleSearchService.getMultipleDefinitions(word)
                map.setValue(word, definitions)
            elif not line.startswith('-'):
                definitions = self.googleSearchService.getMultipleDefinitions(line)
                map.setValue(line, definitions)
                self.writeWordDefToFile(line, definitions, filePath)

    # Its like data storage's addToDatabase but in this one we don't have the 
    # activeSetKey
    def writeWordDefToFile(self, word, definitions, filePath):
        if os.path.exists(filePath):
            with open(filePath, "a") as f:
                self.dataStorageService.writeWordDefToTextFile(f, word, definitions)

    def importAllFilesFromDatabase(self):
        #Read all the files in the database directory,
        path = "src/database/"
        files = os.listdir(path)
    
        for file in files:
            filePath = os.path.join(path, file)
            baseName, extension = os.path.splitext(file)
            fileContents = []
            if os.path.isfile(filePath):
                with open(filePath, "r") as f:
                    fileContents = f.readlines()
            
            #Add name to available set keys
            self.dataStorageService.availableSetsKeys.append(baseName)
            # Create a new hashmap with the word def
            newMap = HashMap(30)
            self.populateWordDefToHashMap(newMap, fileContents, filePath)
            # add this hasmap to available sets using the basename as the key
            self.dataStorageService.availableSets.setValue(baseName, newMap)
            # Remove dangling words
            self.cleanupFile(filePath)
   
   
    # This method removes any dangling words in a file with no definitions
    #How do we know a word is dangling? It has no ':' at the end of it hehe.
    # HAS NO COLON (ew)
    def cleanupFile(self, filePath):
        contentsToCopy = []
        with open(filePath, "r") as file:
            for line in file:
                if ':' in line or '-' in line:
                    contentsToCopy.append(line)
        with open(filePath, "w") as file:
            file.truncate()
            for item in contentsToCopy:
                file.write(item)

