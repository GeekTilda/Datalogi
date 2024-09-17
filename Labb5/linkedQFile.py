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
    

class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word  # Word stored in this node
        self.parent = parent  # Reference to the parent node


class LinkedQ():
    def __init__(self):
        self.__first = None
        self.__last = None

    # Adds a new node to the end of the queue
    def enqueue(self, value):    
        newNode = Node(value)
        if not self.isEmpty():
            self.__last.setNext(newNode)
            self.__last = newNode
        else: 
            self.__first = newNode
            self.__last = newNode

    # Removes and returns the first node in the queue
    def dequeue(self):
        if self.isEmpty():
            return None
        temp = self.__first
        self.__first = self.__first.getNext()
        if self.__first is None:
            self.__last = None
        return temp.getValue()
    
    # Checks if the queue is empty
    def isEmpty(self):
        return self.__first is None
        
    def size(self):
        if self.isEmpty():
            return 0
        
        counter = 1
        currentNode = self.__first
        while currentNode.getNext() != None:
            currentNode = currentNode.getNext()
            counter += 1
        return counter
        
    def __str__(self):
        return str(self.__first.getValue())
