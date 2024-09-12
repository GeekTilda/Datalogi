from bintreeFile import Bintree

def printCommonWords():

    svenska = Bintree()
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                 # Ett trebokstavsord per rad
            svenska.put(ordet)                  # in i sökträdet
    
    english = Bintree()
    with open("engelska.txt", "r", encoding = "utf-8") as englishFile:
        for row in englishFile:
            for word in row.split(" "):
                word = word.strip()
                if word in english:
                    pass
                else:
                    english.put(word)
                    if svenska.__contains__(word):
                        print(word, end = " ")
        
printCommonWords()