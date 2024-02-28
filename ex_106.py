# mem = {
#     "aaa" : {"pw" : "1111", "name" : "jang dong gun"},
#     "aaa" : {"pw" : "1111", "name" : "jang dong gun"},
#     "aaa" : {"pw" : "1111", "name" : "jang dong gun"},
#     "aaa" : {"pw" : "1111", "name" : "jang dong gun"},
#     "aaa" : {"pw" : "1111", "name" : "jang dong gun"}
# }

class Par :
    def __init__(self, a, b) :
        self.a = a
        self.b = b
        print("부모 생성자")
        
    def __str__(self) :
        return "%d, %d"%(self.a, self.b)
    
class Child(Par) :
    def __init__(self, aa, bb):
        super().__init__(aa, bb)
        
        print("자식 생성자")

ch = Child(10, 40)

print(ch.a)