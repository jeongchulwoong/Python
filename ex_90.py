class Television : 
    def __init__(self, channel, volume, on) :
        self.channel = channel
        self.volume = volume
        self.on = on
    def show (self) :
        print(self.channel, self.volume, self.on)
        
def set_SilentMode(t) :
    t.volume = 2            #주소 전달 개념

myTV = Television(11, 10, True)
myTV.show()

set_SilentMode(myTV)
myTV.show()


        