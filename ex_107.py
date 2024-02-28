class Stud :
    def __init__(self, name, jum) :
        self.name = name
        self.jum = jum
    
    def print(self) :
        print(self.name, self.jum)
    
    def __add__ (self, other) :     #클래스의 개체에 대한 더하기 연산자 +의 동작을 정의하는 특수 메서드입니다.

        print(self.name, 'add', other.name)
        return Stud("합계 :", self.jum + other.jum)
    
stu1 = Stud("chul woong", 88)
stu2 = Stud("jung", 99)
stu1.print()
stu2.print()
print()

# sum =  stu2 + stu1      # +를 하면 __add__가 호출
# sum.print()

# stst = stu1.__add__(stu2)
# stst
(stu1 + stu2).print()
