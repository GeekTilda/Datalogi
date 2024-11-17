class Node():

    def __init__(self, value = None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return self.value

    ### GETTERS & SETTERS

    def setNext(self,new):
        self.next = new

    def getNext(self):
        return self.next

    def setValue(self,new):
        self.value = new

    def getValue(self):
        return self.value

class LinkedQ():
    def __init__(self):
        self.__first = None
        self.__last = None

    def enqueue(self, value):    
        newNode = Node(value)
        if not self.isEmpty():
            self.__last.setNext(newNode)
            self.__last = newNode
        else: 
            self.__first = newNode
            self.__last = newNode

    def dequeue(self):  
        if self.isEmpty():
            return None
        temp = self.__first
        self.__first = self.__first.getNext()
        if self.__first is None:
            self.__last = None
        return temp.getValue()

    def isEmpty(self):
        return self.__first is None

    def peek(self): # Peeks on the next value
        if self.isEmpty():
            return None
        return self.__first.getValue()