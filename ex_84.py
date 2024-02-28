import math

class Circle :
    def __init__(self, radius = 0) :
        self.radius = radius
        
    def get_Area(self) :
        return math.pi * self.radius * self.radius
    
    def get_Perimeter(self) :
        return 2 * math.pi * self.radius

c = Circle(10)

print("원의 면적 : ", c.get_Area())
print("원의 둘레 : ", c.get_Perimeter())