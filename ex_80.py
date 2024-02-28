class Student :                         #
    #self : 자기자신(Student class)
    def __init__(self,name, korea, math, english, science) :     # self = class Student
       
        self.name = name        # class에 있는 name에 넘어온 변수 name을 대입
        self.korea = korea
        self.math = math
        self.engilsh = english
        self.science = science
#클래스 이름과 같은 함수를 생성자라고 한다.

students = [
    #Student(),              # 생성자 호출 = > 호출 후 (init)이 호출 된 후 값을 넣어주면 객체가 생성이 된다.
    Student("yoon in sung", 65,73,73,94),       #객체 생성, 생성자 호출
    Student("go so tung", 65,23,98,97),
    Student("kang in ho", 76,83,13,85),
    Student("hansol gks", 78,98,99,31),
    Student("jeng chul woong", 68,97,45,99),
    Student("kim in ho", 56,87,99,33),
]
#print(students[0].name, students[0].korea,students[0].math, students[0].engilsh, students[0].science)

# for student in students :
#     print(student)

# for student in students :    
#     for value_student in list(student) :
#         print(value_student)
        
        