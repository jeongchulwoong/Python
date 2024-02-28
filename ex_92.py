class Dog :
    kind = "Bulldog"
    
    def __init__(self, name , age = 0) :
        self.name = name
        self.age = age
        self.kind = Dog.kind        #class name acess
    def print_all(self) :
        print(self.kind, self.name, self.age)
        
a = Dog("Baduk", 2)
print(a.print_all())

b = Dog("Marry", 3)
print(b.print_all())

