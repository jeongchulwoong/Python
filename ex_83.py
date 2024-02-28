class Television :
    def __init__(self, channel, volume, on) :
        self.channel = channel
        self.volume = volume
        self.on = on
        
    def show(self) :
        print(self.channel, self.volume, self.on)
        
    def setChannel(self,channel):
        self.channel = channel
    def getChannel(self) :
        return self.channel
        
tel = Television(11,20,"on")
tel.show()

tel.setChannel(9)
tel.show()
channel = tel.getChannel()
print("channel = ", channel)

