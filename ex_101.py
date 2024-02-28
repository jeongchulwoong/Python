class MyTime (object):
    def __init__(self, hour, minute, second = 0) :
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __str__(self) :
        
        return"{:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)    #format 형식으로 만들어주면 출력 가능 이전처럼 return문에 그냥 넣어서는 안됨 
                                                                                        #이유는 문자열 반환이 아니라 튜플로 반환 했기 때문 
time = MyTime(1,55)
print(time)
        