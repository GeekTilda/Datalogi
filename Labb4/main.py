from bintreeFile import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()
gamla = Bintree()
q = LinkedQ()

with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        svenska.put(ordet)                 # in i sökträdet

def makeChildren(startWord, queue):
    letters = "abcdefghijklmnopqrstuvwxyzåäö"
    gamla.put(startWord)

    for i in range(len(startWord)):
        for letter in letters:
            newWord = startWord.replace(startWord[i], letter)

            if (newWord in svenska) and (newWord not in gamla):
                queue.enqueue(newWord)
                gamla.put(newWord)

def main():
    startWord = input("Ge ett startord: ")
    endWord = input("Ge ett slutord: ")

    q.enqueue(startWord)
    while not q.isEmpty():
        word = q.dequeue()
        if word == endWord:
            print(f"Det finns en väg till {endWord}!"); quit()
        makeChildren(word, q)
    print(f"Det finns ingen väg till {endWord}...")

main()