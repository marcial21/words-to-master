"""
Gabriel Marcial
https://github.com/marcial21
mgabrielofficial@outlook.com

DataImportService.py
"""

import os
from util.HashMap import HashMap

"""
Class used to handle the logic for importing word sets from text files and transcribing them to lists 
and hash map datastructures that the program can interact with.
"""
class DataImportService:
    """
    Constructor for service.

    Parameters:
        dataStorageService (DataStorageService):   Injected dependency.
        googleSearchService (GoogleSearchService): Injected dependency
    """
    def __init__(self, dataStorageService, googleSearchService) -> None:
        self.dataStorageService = dataStorageService
        self.googleSearchService = googleSearchService
        
    """
    Method that removes tabs and newlines from text file contents, calls google service
    class and stores definition into our hashmap datastructure and prints definitions to
    our file if neccessary. We can summarize our steps into the following 3:
        * Query google service for definitions
        * Populate our hash map with words and definitions as tuple pairs.
        * Write to the same file if needed with words and definitions. 

    Parameters:
        map (HashMap):     Our map that we will populate.
        txtLines (list):   Our file contents split by lines.
        filePath (string): The path of our file.
    """
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

    # Calls our dataStorageService class to write definitions to our specfied file
    def writeWordDefToFile(self, word, definitions, filePath):
        if os.path.exists(filePath):
            with open(filePath, "a") as f:
                self.dataStorageService.writeWordDefToTextFile(f, word, definitions)

    """
    Method that iterates through our /database/ directory for text files and imports each
    file as a new set of word-definitions in our program. For any file, it will gather the words
    and if the words have no definitions, than we will write them to that same file. 
    """
    def importAllFilesFromDatabase(self):
        # Read all the files in the database directory
        path = "src/database/"
        files = os.listdir(path)
    
        for file in files:
            filePath = os.path.join(path, file)
            baseName, extension = os.path.splitext(file)
            fileContents = []
            if os.path.isfile(filePath):
                with open(filePath, "r") as f:
                    fileContents = f.readlines()
            
            # Add name to available set keys
            self.dataStorageService.availableSetsKeys.append(baseName)
            newMap = HashMap(30)
            self.populateWordDefToHashMap(newMap, fileContents, filePath)
            # Add this hasmap to available sets using the basename as the key
            self.dataStorageService.availableSets.setValue(baseName, newMap)
            # Remove dangling words
            self.cleanupFile(filePath)
   
    # This method removes any dangling words in a file with no definitions.
    # How do we know a word is dangling? It has no ':' at the end of it.
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
