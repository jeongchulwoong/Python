class Animal() :
    pass

class Dog(Animal) :
    def __init__(self, name) :
        super().__init__()
        self.name = name
class Person() :
    def __init__(self, name) :
        self.name = name
        self.pet = None     #객체를 저장하려고 None을 줬음
        
dog1 = Dog("dog1")
person1 = Person("hansol")
person1.pet = dog1
print(person1.pet.name)
