class HashNode:
   def __init__(self, key = "", data = None):
      self.key = key
      self.data = data

#Fyll i kod här nedan för att initiera hashtabellen

class Hashtable:
    def __init__(self, size):
       self.size = size
       self.hashlist = [None]*size

    def store(self, key, data):
        c = 0   #COUNTER
        hashKey = self.hashfunction(key)
        objectToStore = HashNode(key,data)
        if self.hashlist[hashKey] != None:
            if type(self.hashlist[hashKey]) == list:
                self.hashlist[hashKey].insert(0,objectToStore)
                c = 1   #COUNTER
            else:
                alreadyStored = self.hashlist[hashKey]
                storedObjects = [alreadyStored,objectToStore]
                self.hashlist[hashKey] = storedObjects
                c = 1   #COUNTER
        else:
            self.hashlist[hashKey] = objectToStore
        return c   #COUNTER

    def search(self, key):
        hashKey = self.hashfunction(key)
        if self.hashlist[hashKey] == None:
            raise KeyError
        if type(self.hashlist[hashKey]) == list:
            for i in self.hashlist[hashKey]:
                if i.key == key:
                    return i.data
            raise KeyError
        if self.hashlist[hashKey].key == key:
            return self.hashlist[hashKey].data
        raise KeyError

    def hashfunction(self, key):
        hashKey = ""
        for c in str(key):
            num = int(((ord(c)+14)*35 + (ord(c))*self.size)/3.1415926)
            hashKey += str(num)
        return int(hashKey) % self.size
    
    def __getitem__(self,key):
        return self.search(key)
    
    def __contains__(self,key):
        try:
            self.search(key)
        except KeyError:
            return False
        return True
    
table = Hashtable(10000)
print(table.hashfunction("a"))
print(table.hashfunction("b"))
print(table.hashfunction("c"))
print(table.hashfunction("d"))
print(table.hashfunction("AB"))
print(table.hashfunction("BA"))
print(table.hashfunction("hej"))
print(table.hashfunction("Hejsan"))
print(table.hashfunction("TJA"))
print(table.hashfunction("Tjenix"))