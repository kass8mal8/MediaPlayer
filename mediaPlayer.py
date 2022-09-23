from random import randint
import time

class  Queue :
    def __init__(self) :
        self.tracks = []
        self.size = 0
        
    def enqueue (self,data) :
        add = self.tracks.append(data)
        self.size += 1
        
        return add
        
    def dequeue (self) :
        remove = self.tracks.pop(0)
        self.size -= 1
        
        return remove
    
class Track :
    def __init__(self,title = None) :
        self.title = title
        self.length = randint(3,10)
    
class MediaPlayerQueue (Queue) :
    def __init__(self):
        super().__init__() 
    
    def addSong (self,song) :
        self.enqueue(song)
        
    def play (self) :
         time_sleep = 0
         
         while self.size >= 1 :
             current_track = self.dequeue()
             print(f"Now playing : {current_track.title} ")
             time.sleep(current_track.length)
             
             time_sleep += current_track.length
             if self.size == 0 :
                 print (f"Playlist ended after : {time_sleep} seconds")
                 
mediaplayer = MediaPlayerQueue ()
songs = ["Morio wa nzeza","masanse","XXXL","Geri Inengi"]

for song in songs :
    track = Track (song)
    mediaplayer.addSong(track)
    
mediaplayer.play()
             