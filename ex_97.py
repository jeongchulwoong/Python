import math

class Shape :
    def __init__(self) :
        pass
    def draw(self) :
        print("draw()가 호출됨") 
        
    def get_area(self) :
        print("get_area()가 호출됨")

class Circle(Shape) :
    
    def __init__(self, radius = 0) :
        #부모생성자 호출
        #super().__init__()
        self.radius = radius
        
    def draw(self):            #함수 오버라이딩 :  부모자식간 동일한 함수가 있을 때 자식이 실행되는 것(자식우선)
        #super().draw()
        print("원을 그립니다.")  
         
         
    def get_area(self) :
        return math.pi * self.radius **2

c = Circle(10)
c.draw()
print("원의 면적 : ", c.get_area())