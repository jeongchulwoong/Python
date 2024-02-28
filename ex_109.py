class AAA :
    def __init__(self, a, b) :
        self.a = a
        self.b = b
        
    def __add__ (self, other) :
        
        return AAA("더하기",  self.b + other.b)
    
    def __sub__(self, other) :
        return AAA("빼기", self.b - other.b)
    
    def __mul__(self, other) :
        #큰값
        a = self.a
        if self.a < other.a :
            a = other.a
        return AAA(a, self.b * other.b)
    
    def __truediv__(self, other) :
        #작은값
        a = self.a 
        
        if self.a > other.a :
            a = other.a
        return AAA(a, self.b / other.b)
        
    def __str__(self) :
        return " AAA {}, {}".format(self.a, self.b)

a1 = AAA("장동건", 10)
a2 = AAA("장서건", 20)

print((a1 + a2))
print((a1 - a2))
print((a1 * a2))
print((a1 / a2))

print("--------------------------------------------")