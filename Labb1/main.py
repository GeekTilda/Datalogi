import csv

### CLASSES

class Drama():
    
    def __init__(self,data):
        self.name = data[0]
        self.rating = float(data[1])
        self.actors = data[2]
        self.viewship = float(data[3])
        self.genre = data[4]
        self.director = data[5]
        self.writer = data[6]
        self.year = int(data[7])
        self.episodes = int(data[8])
        self.network = data[9]

    def __str__(self):  #Only writes the dramas name
        return self.name

    def __lt__(self, other):    #Checks which drama has the lowest rating
        if self.rating < other:
            return True
        else:
            return False
        
    def noe(self):  #Returns the amount of episodes
        return self.episodes
    
    def ratingview(self):   #Returns the rating * viewship
        return (self.rating * self.viewship)
    
    def rating(self):   #Returns the rating
        return self.rating

### MAIN 

def main():
    with open('kdrama.csv') as kdramafile:
        reader = csv.reader(kdramafile, delimiter=',')
        next(reader)    #Skip the first line (header)
        dramas = MakeDramaList(reader)
    MaxRank(dramas)

### FUNCTIONS 

def MakeDramaList(reader):
    dramas = []     #Make empty list
    for row in reader:
        dramas.append(Drama(row))   #Append all the dramas to the list
    return dramas

def MaxRank(dramas):
    max = float(0)
    for drama in dramas:
        if drama.rating > max:
            max = drama.rating
            name = drama.name
    print(name, max)
    return name, max

### CALLING MAIN

main()