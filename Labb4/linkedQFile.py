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
        self.__first = None
        self.__last = None

    def enqueue(self, value):    # Adds a new node to the end and makes sure that the list isnt empty
        newNode = Node(value)
        if not self.isEmpty():
            self.__last.setNext(newNode)
            self.__last = newNode
        else: 
            self.__first = newNode
            self.__last = newNode

    def dequeue(self):  # Makes the new first node the next node, and returns the value (aka removes the first node)
        if self.isEmpty():
            return None
        temp = self.__first
        self.__first = self.__first.getNext()
        if self.__first is None:
            self.__last = None
        return temp.getValue()
    
    def isEmpty(self):  # Checks if the list is empty
        if self.__first == None:
            return True
        else:
            return False
        
    def size(self):
        if self.isEmpty():
            return 0
        
        counter = 1
        currentNode = self.__first
        while currentNode.next != None:
            currentNode = currentNode.next
            counter += 1
        return counter
        
    def __str__(self):
        return str(self.__first.getValue())
