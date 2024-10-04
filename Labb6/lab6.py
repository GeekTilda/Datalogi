from song import Song
from searchAlgorithms import *
from mergesort import mergesort
from bubblesort import bubblesort
import timeit

def fileToList(file):
    songList = []
    with open(file, "r", encoding = "utf-8") as songFile:
        for row in songFile:
            info = row.strip("\n").split("<SEP>")
            songList.append(Song(info[0], info[1], info[2], info[3]))
    return songList

def main():

    filename = "unique_tracks.txt"

    lista = fileToList(filename)
    searchList = lista[0:250000]
    n = len(searchList)
    print("Antal element =", n)

    sista = searchList[n-1]
    testartist = sista.artist

    sortedlist = searchList.copy()
    sortedlist.sort()

    hashTable = HashTable()
    for  key, value in enumerate(searchList):
        hashTable.insert(key, value)

    bintid = timeit.timeit(stmt = lambda: binary_search(sortedlist, sista), number = 10000)
    print("Binärsökningen tog", round(bintid, 4) , "sekunder")

    hashtid = timeit.timeit(stmt = lambda: hashTable.search(sista), number = 10000)
    print("Hashsökningen tog", round(hashtid, 4) , "sekunder")

    linjtid = timeit.timeit(stmt = lambda: linear_search(searchList, testartist), number = 10000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    listToSort = lista[0:10000]
    mergtid = timeit.timeit(stmt = lambda: mergesort(listToSort), number = 1)
    print("Mergesort tog", round(mergtid, 4) , "sekunder")

    bubtid = timeit.timeit(stmt = lambda: bubblesort(listToSort), number = 1)
    print("Bubble-sort tog", round(bubtid, 4) , "sekunder")

main()

'''
Linjär sökning bör teoretiskt ha tidskomplexiteten O(n), vilket våra resultat visar:
n = 250 000: 326,7506 s (1)
n = 500 000: 658,2066 s (2)
n = 1 000 000: 1433,0759 s (3)
då resultat (3) ≈ 2*(2) ≈ 4*(1)

Binärsökning ska vara O(log(n)), vilket ses i resultaten:
n = 250 000: 0,0717 s (1)
n = 500 000: 0,0746 s (2)
n = 1 000 000: 0,0795 s (3)
då om vi antar att Tbin(n) = k * log(n), ger resultat (1) att k ≈ 0,004 och resultat (2) ≈ 0,004 * log(500 000)
och resultat (3) ≈ 0,004 * log(1 000 000)

Hashsökning ska ha komplexiteten O(1), vilket lätt ses genom resultaten:
n = 250 000: 0,0013 s (1)
n = 500 000: 0,0014 s (2)
n = 1 000 000: 0,0013 s (3)

För sorteringsalgoritmer använde vi Bubble-sort och Mergesort, som ska ha tidskomplexiteten O(n^2) respektive O(nlog(n)).
Bubble-sort resultat:
n = 1000: 0,1145 s (1)
n = 10 000: 11,815 (2)
n = 100 000: 1926,1649 (3)
n = 1 000 000: Körde ej, teoretisk tid ≈ 27 timmar.

Mergesort resultat:
n = 1000: 0,002 s (4)
n = 10 000: 0,0329 s (5)
n = 100 000: 0,4152 s (6)
n = 1 000 000: 6,7594 s (7)

Dessa resultat stämmer generellt överens med teorin, men lite sämre än testerna för sökningsalgoritmerna,
bl.a. då sorteringsmetoderna endast kördes en gång jämfört med 10 000 gånger för sökningen. Bubble-sort tog
även lite längre tid än väntat i resultat (3) då datorn programmed kördes på blev väldigt varm.
'''
