class Animal :
    def __init__(self, age=0) :
        self.age = age
        
    def eat(self) :
        print(" animal eating ")

class Dog(Animal) :
    def __init__(self, name="", age=0):
        super().__init__(age)
        self.name = name

d = Dog()
print(d.age)
e = Animal()
print(e.age)
    