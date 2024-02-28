class Employee : 
    def __init__(self, name, salary) :
        self.name = name
        self.salary = salary        #월급
    
    def get_Salary(self) :
        return self.salary
    
class Manager(Employee) :
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
        
    def get_Salary(self):
        
        salary = super().get_Salary()
        return salary
    
  
    def get_Salary_Bonus(self) :
        
        total_salaty = self.get_Salary() + self.bonus
        return total_salaty
    
    def __str__(self) :         #변수이름만 출력하면 주소값만 나오지만 __str__ 함수를 쓰면 값이 나온다
                                #str 쓰는 이유 정수를 문자열로 바꿔줌
        return "이름 : " + self.name + " 월급 : " + str(self.salary) + \
             " 보너스 : " + str(self.bonus)
    
c = Manager("hansol", 2000000, 800000)
print(c.name ,c.get_Salary(), c.bonus, c.get_Salary_Bonus())
print(c)

