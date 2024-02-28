class Television : 
    serialNumber = 0    #클래스 변수 (공동사용)
    
    def __init__(self, channel, volume, on) :       #Television을 참조를 해줘야 참조된 변수가 class 변수임을 알게됨
        self.channel = channel
        self.volume = volume
        self.on = on
        Television.serialNumber += 1                
        self.number = Television.serialNumber       #만약 함수 안에 생성된 serialNumber은 함수안의 지역변수 Television.serialNumber 은 클래스 변수
    def show (self) :
        print(self.channel, self.volume, self.on, self.number)
        
def set_SilentMode(t) :
    t.volume = 2            #주소 전달 개념

myTV = Television(11, 10, True)
myTV.show()
myTV.show()
myTV.show()
myTV1 = Television(9, 15, False)
myTV1.show()
myTV1.show()
myTV1.show()

print(Television.serialNumber)
print(myTV.channel)


        