"""
Gabriel Marcial
https://github.com/marcial21
mgabrielofficial@outlook.com

HashMap.py
"""

"""
A utility class used to store data as a hash table. Has pretty much all the features 
of a traditional hash map. This is what we use to store word sets and word definition
sets.
"""
class HashMap:
    # Constructor
    def __init__(self, size):
        self.size = size
        self.length = 0
        self.hashTable = self.createBuckets()
    
    # List of lists as our data structure
    def createBuckets(self):
        return [[] for _ in range(self.size)]
 
    # Insert values into hash map
    def setValue(self, key, val):
        hashedKey = hash(key) % self.size
        bucket = self.hashTable[hashedKey]
        foundKey = False

        for index, record in enumerate(bucket):
            recordKey, recordVal = record
            if recordKey == key:
                foundKey = True
                break
 
        if foundKey:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
            self.length += 1
 
    # Return searched value with specific key
    def getVal(self, key):
        hashedKey = hash(key) % self.size
        bucket = self.hashTable[hashedKey]
        foundKey = False

        for index, record in enumerate(bucket):
            recordKey, recordVal = record             
            if recordKey == key:
                foundKey = True
                break
 
        if foundKey:
            return recordVal
        else:
            return None
 
    # Remove a value with specific key
    def deleteVal(self, key):
        hashedKey = hash(key) % self.size
        bucket = self.hashTable[hashedKey]
        foundKey = False

        for index, record in enumerate(bucket):
            recordKey, recordVal = record
            if recordKey == key:
                foundKey = True
                break
        if foundKey:
            bucket.pop(index)
            self.length -= 1
        return
 
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hashTable)
