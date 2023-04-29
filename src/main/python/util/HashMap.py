class HashMap:
 
    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.length = 0
        self.hashTable = self.createBuckets()
 
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
