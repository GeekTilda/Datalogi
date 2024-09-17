from bintreeFile import Bintree
from linkedQFile import LinkedQ

def main():
    usedWords = Bintree()       # Bintree with used words.
    q = LinkedQ()               # Queue for going through words for wordsearch.

    wordList = makeWordList("C:\\Users\\tilda\\Desktop\\KTH\\Datalogi\\Labb4\\word3.txt")

    startWord = input("Ge ett startord: ")
    endWord = input("Ge ett slutord: ")
    if (startWord not in wordList) or (endWord not in wordList):
        print(f"Välj giltiga, {len(wordList.root.getValue())} bokstäver långa ord att gå emellan!"); quit()


    q.enqueue(startWord)
    while not q.isEmpty():      # Searches through all words related to startWord until it finds endWord.
        word = q.dequeue()
        if word == endWord:
            print(f"Det finns en väg till {endWord}!"); quit()
        makeChildren(word, q, wordList, usedWords)
    print(f"Det finns ingen väg till {endWord}...")


def makeChildren(startWord, queue, wordList, usedWords):
    letters = "abcdefghijklmnopqrstuvwxyzåäö"       # Characters.
    usedWords.put(startWord)

    for i in range(len(startWord)):
        for letter in letters:
            newWord = startWord.replace(startWord[i], letter)           # Creates a new word with one letter changed.

            if (newWord in wordList) and (newWord not in usedWords):    # Adds it to the word-queue if newWord is valid.
                queue.enqueue(newWord)
                usedWords.put(newWord)

def makeWordList(filename):
    wordList = Bintree()

    with open(filename, "r", encoding = "utf-8") as wordFile:
        for row in wordFile:
            word = row.strip().lower()          # One lowercase word per row.
            wordList.put(word)                  # Puts it into the Bintree.
    return wordList

    
main()
