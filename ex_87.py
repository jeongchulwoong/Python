class Student : 
    def __init__(self, name = None, age = 10) :
        self.__name = name
        self.__age = age        #__변수 앞에 붙으면 외부에서 변경 금지
        
    def get_age (self):
        return self.__age
    
    def get_name(self) :
        return self.__name
    def set_age(self, age) :
        self.__age = age
    def set_Name(self, name) :
        self.__name = name
        
obj = Student("홍길동", 20)
obj.__age = 21
print(obj.get_age())
print(obj.__age)
print("None : ", type(None))