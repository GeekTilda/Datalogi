class Song:
    def __init__(self, trackID, songID, artist, songName):
        self.trackID = trackID
        self.songID = songID
        self.artist = artist
        self.songName = songName

    def __lt__(self, other):
        return self.artist < other.artist