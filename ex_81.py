class Student :                         #
    #self : 자기자신(Student class)
    def __init__(self,name, korea, math, english, science) :     # self = class Student
       
        self.name = name        # class에 있는 name에 넘어온 변수 name을 대입
        self.korea = korea
        self.math = math
        self.engilsh = english
        self.science = science
        
    def get_sum (self) :             # self 써줘야함 문법
        return self.korea + self.math + \
                self.engilsh + self.science
                
    def get_avg(self) :
        return (self.get_sum() / 4)

    def to_string (self):
        return ("{}\t{}\t{}\t".format(self.name, self.get_sum(), self.get_avg()))
    

students = [
    Student("yoon in sung", 65,73,73,94),
    Student("go so tung", 65,23,98,97),
    Student("kang in ho", 76,83,13,85),
    Student("hansol gks", 78,98,99,31),
    Student("jeng chul woong", 68,97,45,99),
    Student("kim in ho", 56,87,99,33),
]

print("name","all sum","average",sep="\t")
    
for student in students:
    print(student.to_string())      #함수 이므로 꼭 () 필요!!!
    