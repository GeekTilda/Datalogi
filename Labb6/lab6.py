from song import Song
from searchAlgorithms import *
from mergesort import mergesort
from bubble_sort import bubble_sort
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

#songList = fileToList("C:\\Users\\tilda\\Desktop\\KTH\\Datalogi\\Labb6\\unique_tracks.txt")

def main():

    filename = "C:\\Users\\tilda\\Desktop\\KTH\\Datalogi\\Labb6\\unique_tracks.txt"

    lista = fileToList(filename)
    lista = lista[0:100000]
    n = len(lista)
    print("Antal element =", n)


    bubtid = timeit.timeit(stmt = lambda: bubble_sort(lista), number = 1)
    print("Bubble sorten tog ", round(bubtid, 4) , "sekunder")

    mergtid = timeit.timeit(stmt = lambda: mergesort(lista), number = 1)
    print("Mergesort tog ", round(mergtid, 4) , "sekunder")

main()






