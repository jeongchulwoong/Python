# raise : 의도적으로 에러를 발생시켜야하는 경우
# 상위 클래스를 설계할 떄 하위 클래스에서 반드시
# 오버라이드하여 상세하게 구현해야하는 함수를 
# 명시하고자 하려면 해당 함수의 내용으로
# raise NotImplementError(메세지)로 처리한다

import math

class Shape :
    def __init__(self, name) :
        self.name = name
        
    def get_Area(self) : 
        raise NotImplementedError("이것은 추상합수 입니다.")
        #추상함수 :  내용이 없는 함수
class Circle(Shape) :
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def get_Area(self):
        
        return math.pi * self.radius **2
    
class Rectangle(Shape) :
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
     
    def get_Area(self):
         
         return self.width * self.height

list = [Circle("hansol", 10), Rectangle("chul woong", 10,10)]       #리스트로 객체 생성

for i in list :
    print(f"이름 : {i.name} 면적 : {i.get_Area()}")