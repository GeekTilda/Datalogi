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
        hashKey = self.hashfunction(key)
        objectToStore = HashNode(key,data)
        i = 1
        while self.hashlist[hashKey] != None:
            hashKey = ((hashKey+i**2)) % self.size
            i = i + 1
        self.hashlist[hashKey] = objectToStore

    def search(self, key):
        hashKey = self.hashfunction(key)
        try:
            i = 1
            while self.hashlist[hashKey].key != key:
                hashKey = (hashKey + i**2) % self.size
                i = i + 1
            return self.hashlist[hashKey].data
        except:
            pass
        raise KeyError

    def hashfunction(self, key):
        hashKey = ""
        for c in str(key):
            num = ord(c)
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