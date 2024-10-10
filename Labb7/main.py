import csv
from hashtable import Hashtable

class Drama:
    def __init__(self, drama):
        self.name = drama[0]
        self.rating = drama[1]
        self.actors = drama[2]
        self.views = drama[3]
        self.genre = drama[4]
        self.director = drama[5]
        self.writer = drama[6]
        self.year = drama[7]
        self.episodeNo = drama[8]
        self.network = drama[9]

    def __str__(self):
        return self.name + "\n" + "Genre: " + self.genre + "\n" + "Rating: " + str(self.rating) + "/10"
    
    def __lt__(self, otherDrama):
        return self.rating < otherDrama.rating
    
    def sameNetwork(self, otherDrama):
        return self.network == otherDrama.network
    
    def highRating(self, rating):
        return float(self.rating) >= rating


def fileToList(file):
    c = 0   #COUNTER
    dramaList = Hashtable(542)
    with open(file) as csvFile:
        dramaFile = csv.reader(csvFile, delimiter = ",")
        next(dramaFile)
        for drama in dramaFile:
            myDrama = Drama(drama)
            c += dramaList.store(myDrama.name, myDrama) #RETURNED THE COUNTER
    print(c)    #COUNTER
    return dramaList

### MAIN

def main():
    dramaList = fileToList("C:\\Users\\tilda\\Desktop\\KTH\\Datalogi\\Labb7\\kdrama.csv")
    print(dramaList.search("The Heirs"))
    print(dramaList.search("Mamamamamaa"))

main()