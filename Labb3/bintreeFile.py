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
            if (root.getRight().getValue() > newValue):
                if root.getLeft() != None:
                    root = root.getLeft()
                else:
                    return root.setLeft(Node(newValue))
            if (root.getLeft().getValue() < newValue):
                if root.getRight() != None:
                    root = root.getRight()
                else:
                    return root.setRight(Node(newValue))
        root = Node(newValue)

def binarySearch(root,value):
    currentNode = root
    while currentNode != None:
        print(str(currentNode.getValue()))
        if currentNode.getValue() == value:
            return True
        elif (currentNode.getRight() != None) and (currentNode.getRight().getValue() > value):
            if currentNode.getLeft() == None:
                return False
            else:
                currentNode = currentNode.getLeft()
        elif (currentNode.getLeft() != None) and (currentNode.getLeft().getValue() < value): 
            if currentNode.getRight() == None:
                return False
            else:
                currentNode = currentNode.getRight()
    return False

#def writeInorder():

tree = Bintree()

rootNode = Node(5)
leftNode = Node(3)
rightNode = Node(7)
rrnode = Node(8)

rootNode.setLeft(leftNode)
rootNode.setRight(rightNode)
rightNode.setRight(rrnode)

tree.root = rootNode

print(binarySearch(rootNode,4))