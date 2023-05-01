import os

class DataImportService:
    def __init__(self, dataStorageService) -> None:
        self.dataStorageService = dataStorageService
        

    def importAllFilesFromDatabase(self):
        #Read all the files in the database directory,
        path = "src/database/"
        files = os.listdir(path)
        fileBaseNames = []
        for file in files:
            filePath = os.path.join(path, file)
            baseName, extension = os.path.splitext(file)
            fileContents = []
            if os.path.isfile(filePath):
                with open(filePath, "r") as f:
                    fileContents = f.readlines()
                    
            print(baseName)
            print(fileContents)
            
            fileBaseNames.append(baseName)

        
            
        #For each file, open as append and 
            #Create a new set with the key as the name of that set, and a new hashmap that will be populated with its words

