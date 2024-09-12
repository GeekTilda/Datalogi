class Bintree():
    def __init__(self):
        self.root = None

    def put(self, newValue):
        if self.root == None:
            self.root = Node(newValue)
        else:
            push(self.root, newValue)

    def __contains__(self, value):
        return binarySearch(self.root, value)

    def write(self):
        printTree(self.root)
        print("\n")
    

class Node():

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

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
    
    def __str__(self):
        return str(self.value)
    

def nodeToLeft(node1, node2):
    if node2.getValue() < node1.getValue():
        return True
    return False

def push(root, newValue):
    if not binarySearch(root, newValue):
        currentNode = root
        newNode = Node(newValue)

        run = True
        while run:      # Runs until newNode is placed.
            while nodeToLeft(currentNode, newNode):
                if currentNode.getLeft() == None:
                    currentNode.setLeft(newNode)    # Node is placed to the left.
                    run = False
                    break
                currentNode = currentNode.getLeft()

            while not nodeToLeft(currentNode, newNode):
                if currentNode.getRight() == None:
                    currentNode.setRight(newNode)   # Node is placed to the right.
                    run = False
                    break
                currentNode = currentNode.getRight()
            
    
def binarySearch(root, value):
    currentNode = root
    if currentNode != None:
        while currentNode.getValue() != value:

            if nodeToLeft(currentNode, Node(value)):
                currentNode = currentNode.getLeft()
            else:
                currentNode = currentNode.getRight()
            
            if currentNode == None:
                return False
                
        return True
    return False


def printTree(node): # Loops through the entire tree recursively and prints the nodes in inorder.
    if node is None:
        return None
    
    printTree(node.getLeft())   # First step, go to leftmost node.

    print(node.getValue(), end = " ")   # As getLeft() reached None, returns to previous node and prints value.

    printTree(node.getRight())  # Checks to the right of printed node.