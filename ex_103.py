class Person :
    def __init__(self, name, number) :
        self.name = name
        self.number = number
        
class Student(Person) :
    UNDERGRADUATE = 0
    POSTGRADUATE = 1
    
    def __init__(self, name, number, studentType):
        super().__init__(name, number)
        self.studentType = studentType
        self.gpa = 0
        self.classes = []
        
    def enrollCourse(self, course) :
        self.classes.append(course)      #리스트에는 값이 그냥 들어가지 않음 append사용
    
    def __str__(self) :
                                                # (+/) 줄바꿈시 뒤에는 +기호 필요없음
        return "\n이름 : " + self.name + "\n 주민번호 : " + str(self.number) + "\n 학생유형 : " + str(self.studentType) +\
                 "\n  : " + str(self.classes) + "\n 수강과목 : " + str(self.classes) + "\n 평점 :" + str(self.gpa)
    
class Teacher (Person) :
    def __init__(self, name, number):
        super().__init__(name, number)
        self.course = []
        self.salary = 3000000
    
    def assignTeaching(self, course) :
        self.course.append(course) 
    
    def __str__(self) :
        
        return "\n이름 : " + self.name + "\n 주민번호 : " + str(self.number) + \
                "\n 강의과목 : " + str(self.course) + "\n 월급 :" + str(self.salary)
 
student = Student("hansol", 12345678, Student.UNDERGRADUATE)   
student.enrollCourse("자료구조")   
print(student) 
teacher = Teacher("chul woong", 7800089)
teacher.assignTeaching("Python")
teacher.assignTeaching("C")
teacher.assignTeaching("SQL")
print(teacher)