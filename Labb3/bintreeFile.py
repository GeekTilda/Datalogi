class Node():

    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return self.value

    ### GETTERS & SETTERS

    def setLeft(self,new):
        self.left = new

    def getLeft(self):
        return self.left

    def setRight(self,new):
        self.right = new

    def getRight(self):
        return self.right

    def setValue(self,new):
        self.value = new

    def getValue(self):
        return self.value

class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newValue): # Sorts in newvalue into the tree
        push(self.root,newValue)

    def __contains__(self,value):   # True if value exists in the tree, False otherwise
        return binarySearch(self.root,value)

    def write(self):    # Writes out the tree in inorder
        #writeInorder(self.root)
        print("\n")    
    
def push(root, newValue):
    if not binarySearch(root, newValue):
        while (root != None):
            if (root > newValue):
                if root.getLeft() != None:
                    root = root.getLeft()
                else:
                    return root.setLeft(Node(newValue))
            if (root < newValue):
                if root.getRight() != None:
                    root = root.getRight()
                else:
                    return root.setRight(Node(newValue))
        root = Node(newValue)

def binarySearch(root,value):    
    while(root != None):
        if (root > value):
            if (root.getLeft() == None):
                return False
            else:
                root = root.getLeft()
        if (root < value):
            if (root.getRight() == None):
                return False
            else:
                root = root.getRight()
        if (root == value):
            return True
    return False

#def writeInorder():
