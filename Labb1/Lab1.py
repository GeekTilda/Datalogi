import csv
import random

def main():
    dramaList = fileToList("kdrama.csv")
    
    drama1 = random.choice(dramaList)
    drama2 = random.choice(dramaList)

    print(drama1)
    print("\n")
    print(drama2)
    print("\n")

    if drama1 < drama2:
        print(drama2.name + " is higher rated")
    else:
        print(drama1.name + " is higher rated")

    if Drama.sameNetwork(drama1, drama2):
        print("They're on the same network! Only one subscription necessary :)")
    else:
        print("They're on different networks :(")

    rating = input("Search for K-dramas with a rating of at least: ")
    highRaters = findHighRaters(dramaList, rating)
    
    for drama in highRaters:
        print("\n")
        print(drama)



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
    dramaList = []
    with open(file) as csvFile:
        dramaFile = csv.reader(csvFile, delimiter = ",")
        next(dramaFile)
        for drama in dramaFile:
            dramaList.append(Drama(drama))
    return dramaList

def findHighRaters(dramaList, rating):
    highRaters = []
    for drama in dramaList:
        if drama.highRating(float(rating)):
            highRaters.append(drama)
    return highRaters


main()