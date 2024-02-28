class Student : 
    def __init__(self, name = None, age = 0) :
        self.name = name
        self.age = age
        
obj = Student("홍길동", 20)
obj.age = 21
print(obj.name)
print(obj.age)
print("None : ", type(None))