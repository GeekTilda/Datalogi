from bintreeFile import Bintree
from linkedQFile import LinkedQ
from linkedQFile import ParentNode

# Exception to signal when the solution is found
class SolutionFound(Exception):
    pass

# Main function to start the word chain search
def main():
    usedWords = Bintree()  # Bintree for used words.
    q = LinkedQ()          # Queue for wordsearch.

    wordList = makeWordList("C:\\Users\\tilda\\Desktop\\KTH\\Datalogi\\Labb5\\word3.txt")   # My path, but can be replaced by only "word3.txt"

    startWord = input("Ge ett startord: ")
    endWord = input("Ge ett slutord: ")

    # Check if start and end words are in the word list
    if (startWord not in wordList) or (endWord not in wordList):
        print(f"Välj giltiga ord. Orden måste vara riktiga ord och måste vara 3 bokstäver långa!")
        quit()


    startNode = ParentNode(startWord)  # Create ParentNode for startWord (söt)
    q.enqueue(startNode)               # Enqueue the ParentNode

    try:
        while not q.isEmpty():  # Continue until the queue is empty or the solution is found
            currentNode = q.dequeue()
            if currentNode.getWord() == endWord:  # If the current word matches the end word
                print(f"Det finns en väg till {endWord}!")
                writeChain(currentNode)  # Write the entire chain of words
                raise SolutionFound  # Solution found, raise exeption!
            else: 
                makeChildren(currentNode, q, wordList, usedWords)  # Else: Generate and enqueue new children nodes
    except SolutionFound:
        pass  # End the program when solution is found
    else:
        print(f"Det finns ingen väg till {endWord}...")  # If no solution is found

# Function to create children nodes by changing one letter at a time
def makeChildren(currentNode, queue, wordList, usedWords):
    letters = "abcdefghijklmnopqrstuvwxyzåäö"  # Characters.
    usedWords.put(currentNode.getWord())  # Mark current word as used

    # Iterate through each character in the word
    for i in range(len(currentNode.getWord())):
        for letter in letters:
            # Create a new word by replacing the character at index 'i' with 'letter'
            newWord = currentNode.getWord()[:i] + letter + currentNode.getWord()[i+1:]  

            # If the new word is valid and not already used
            if (newWord in wordList) and (newWord not in usedWords):  
                newNode = ParentNode(newWord, currentNode)  # Create a new ParentNode with currentNode as its parent
                queue.enqueue(newNode)  # Add the new node to the queue
                usedWords.put(newWord)  # Mark the new word as used

# Recursive function to write the chain of words from start to end
def writeChain(node):
    if node.getParent() is not None:  # If the node has a parent, print the parent chain first
        writeChain(node.getParent())
    print(node.getWord())  # Then print the current word

# Function to load the word list from a file and insert into a binary tree
def makeWordList(filename):
    wordList = Bintree()

    with open(filename, "r", encoding="utf-8") as wordFile:
        for row in wordFile:
            word = row.strip().lower()  # One lowercase word per row.
            wordList.put(word)          # Puts it into the Bintree.
    return wordList

main()
