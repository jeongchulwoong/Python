class Counter :
    def __init__(self, init_value = 0, ) :
        self.count = init_value
        
    def increment(self) :
        self.count += 1

        

a = Counter()       #자동으로 __init__() 생성자 호출, 객체 생성
b = Counter(100)

print(a.increment())
print("a 생성자 값 : ", a.count)
print(b.increment())
print("b 생성자 값 :", b.count)

        