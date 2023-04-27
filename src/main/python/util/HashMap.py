class HashMap:
 
    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hashTable = self.createBuckets()
 
    def createBuckets(self):
        return [[] for _ in range(self.size)]
 
    # Insert values into hash map
    def setValue(self, key, val):
       
        # Get the index from the key
        # using hash function
        hashedKey = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hashTable[hashedKey]
 
        foundKey = False
        for index, record in enumerate(bucket):
            recordKey, recordVal = record
             
            # check if the bucket has same key as
            # the key to be inserted
            if recordKey == key:
                foundKey = True
                break
 
        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if foundKey:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
 
    # Return searched value with specific key
    def getVal(self, key):
       
        # Get the index from the key using
        # hash function
        hashedKey = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hashTable[hashedKey]
 
        foundKey = False
        for index, record in enumerate(bucket):
            recordKey, recordVal = record
             
            # check if the bucket has same key as
            # the key being searched
            if recordKey == key:
                foundKey = True
                break
 
        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if foundKey:
            return recordVal
        else:
            return None
 
    # Remove a value with specific key
    def deleteVal(self, key):
       
        # Get the index from the key using
        # hash function
        hashedKey = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hashTable[hashedKey]
 
        foundKey = False
        for index, record in enumerate(bucket):
            recordKey, recordVal = record
             
            # check if the bucket has same key as
            # the key to be deleted
            if recordKey == key:
                foundKey = True
                break
        if foundKey:
            bucket.pop(index)
        return
 
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hashTable)
    


# hash_table = HashMap(50)
 
# # insert some values
# hash_table.setValue('gfg@example.com', 'some value')
# print(hash_table)
# print()
 
# hash_table.setValue('portal@example.com', 'some other value')
# print(hash_table)
# print()
 
# # search/access a record with key
# print(hash_table.getVal('portal@example.com'))
# print()
 
# # delete or remove a value
# hash_table.deleteVal('portal@example.com')
# print(hash_table)