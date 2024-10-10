class DictHash:
    def __init__(self):
        self.hashlist = {}

    def store(self,key,data):
        self.hashlist[key] = data

    def search(self,key):
        value = self.hashlist.get(key)
        return value
    
    def __getitem__(self,key):
        return self.search(key)
    
    def __contains__(self,key):
        return key in self.hashlist


