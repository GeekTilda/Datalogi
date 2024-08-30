class Node():

    def __init__(self, value = None):
        self.value = value
        self.next = None

    def setNext(self,new):
        self.next = new

    def getNext(self):
        return self.next

    def setValue(self,new):
        self.value = new

    def getValue(self):
        return self.value
    
    def __str__(self):
        return self.value

class LinkedQ():

    def __init__(self):
        self._first = None
        self._last = None

    def enqueue(self, value):    # Adds a new node to the end and makes sure that the list isnt empty
        newNode = Node(value)
        if not self.isEmpty():
            self._last.setNext(newNode)
            self._last = newNode
        else: 
            self._first = newNode
            self._last = newNode

    def dequeue(self):  # Makes the new first node the next node, and returns the value (aka removes the first node)
        if self.isEmpty():
            return None
        temp = self._first
        self._first = self._first.getNext()
        if self._first is None:
            self._last = None
        return temp.getValue()
    
    def isEmpty(self):  # Checks if the list is empty
        if self._first == None:
            return True
        else:
            return False
        
    def __str__(self):
        return str(self._first.getValue())
    
