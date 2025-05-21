class Music: #this is the parent class
    counter = 0 # this is variable of the class and it will be shared by all the instances of the class
    def __init__(self, Artist, SongName, popularity):
        self.Artist = Artist
        self.SongName = SongName
        self.popularity = popularity
        Music.counter += 1
    def set_mycomment(self, comment):
        self.coment = comment
        
M1 = Music("Rose", "APT", "really popular")
M2 = Music("A-ha", "Take on me", "really popular")
M1.set_mycomment("I love this song, but I'm a bit tired of it")
M2.set_mycomment("this song is really good, thaks Lucas for the recommendation")
print(M1.__dict__, M1.counter) # this will print the dictionary of the object M1


class Kpop(Music): #this is the child class of Music
    pass
class Groups(Kpop): 
    pass

class Blackpink(Groups):
    pass
    
        
class NJZ(Groups):
    pass
    
class Gidle(Groups):
    pass
    


class Rock(Music): #this is the child class of Music
    pass

class band(Rock):
    pass

class BringMeTheHorizon(band):
    pass

class LinkinPark(band):
    pass

