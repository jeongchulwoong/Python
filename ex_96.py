class Person : 
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
    def show(self) :
        print(self.name, self.age)
        
class Student :
    
    def __init__(self, id) :
        self.id = id
        
    def get_id(self) :
        return self.id

class CollegeStudent(Person, Student):     #다중상속을 할 때는 super()를 사용하는 것이 아니라 각 클래스명을 사용
    def __init__( self, name, age, id):
        Person.__init__(self,name, age)
        Student.__init__(self,id)
        
          
stu = CollegeStudent("kim", 22,"20230524")
stu.show()
print(stu.get_id())
