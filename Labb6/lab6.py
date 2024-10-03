from song import Song
from searchAlgorithms import *
from mergesort import mergesort
import timeit

class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        """Inserts a key-value pair into the hash table."""
        self.table[key] = value

    def search(self, key):
        """Searches for a key in the hash table and returns its value if found, else None."""
        return self.table.get(key, None)

    def delete(self, key):
        """Deletes a key-value pair from the hash table."""
        if key in self.table:
            del self.table[key]

def fileToList(file):
    songList = []
    with open(file, "r", encoding = "utf-8") as songFile:
        for row in songFile:
            info = row.strip("\n").split("<SEP>")
            songList.append(Song(info[0], info[1], info[2], info[3]))
    return songList

songList = fileToList("unique_tracks.txt")

def main():

    filename = "unique_tracks.txt"

    lista = fileToList(filename)
    lista = lista[0:1000000]
    n = len(lista)
    print("Antal element =", n)


    sista = lista[n-1]
    testartist = sista.artist

    sortedlist = lista.copy()
    sortedlist.sort()

    hashTable = HashTable()
    for  key, value in enumerate(lista):
        hashTable.insert(key, value)

    

    bintid = timeit.timeit(stmt = lambda: binary_search(sortedlist, sista), number = 10000)
    print("Binärsökningen tog", round(bintid, 4) , "sekunder")

    hashtid = timeit.timeit(stmt = lambda: hashTable.search(sista), number = 10000)
    print("Hashsökningen tog", round(hashtid, 4) , "sekunder")

    linjtid = timeit.timeit(stmt = lambda: linear_search(lista, testartist), number = 10000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

main()






