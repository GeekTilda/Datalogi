from bintreeFile import Bintree
from linkedQFile import LinkedQ

def main():
    startWord = input("Ge ett startord: ")
    endWord = input("Ge ett slutord: ")

    svenska = Bintree()     # Bintree with all words.
    gamla = Bintree()       # Bintree with used words.
    q = LinkedQ()           # Queue for going through words for wordsearch.

    with open("C:\\Users\\tilda\\Desktop\\KTH\\Datalogi\\Labb4\\word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # One three-letter-word per row.
            svenska.put(ordet)                 # Puts it into the Bintree.

    q.enqueue(startWord)
    while not q.isEmpty():  # Searches through all words related to startWord until it finds endWord.
        word = q.dequeue()
        if word == endWord:
            print(f"Det finns en väg till {endWord}!"); quit()
        makeChildren(word, q, svenska, gamla)
    print(f"Det finns ingen väg till {endWord}...")

def makeChildren(startWord, queue, svenska, gamla):
    letters = "abcdefghijklmnopqrstuvwxyzåäö"       # Characters.
    gamla.put(startWord)

    for i in range(len(startWord)):
        for letter in letters:
            newWord = startWord.replace(startWord[i], letter)       # Creates a new word with one letter changed.

            if (newWord in svenska) and (newWord not in gamla):     # Adds it to the word-queue if newWord is valid.
                queue.enqueue(newWord)
                gamla.put(newWord)

main()
