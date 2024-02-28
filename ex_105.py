import random

class Dice :
    def __init__(self) :
        self.sides_count = 6
    
    def get_sides_count(self) :
        return self.sides_count
    
    def roll(self) :
        x = random.random()
        print(x)
        return random.randint(1,self.sides_count)   #random 함수
        #randint(a <= x <=b)

class FraudDice(Dice) :
    
    def __init__(self):
        super().__init__()
    
    def roll(self):
    
        while True :
            r = super().roll()
            if r > 3 :
                return r
            
e = FraudDice()
print(e.roll()) 

        