class Stud :
    def __init__(self, name, jum) :
        self.name = name
        self.jum = jum
        
    def print(self) :
        
        print(self.name, self.jum)
        
    def __add__(self, other) :
        
        print(self.name, 'add', other.name)
        
        res = []
        for i in range(len(self.jum)) :         #각 자리수의 합
            res.append(self.jum[i] + other.jum[i])
            
        return Stud("합계 :", res)
            
        
        # for x, y in zip(self.jum, other.jum) :
        #     res.append(x + y)
        
        # return Stud("합계 : ", res)
        #return Stud("합계 :", (self.cal_list(self.jum) + self.cal_list(other.jum)))
        #return Stud("합계 :", (sum(self.jum) + sum(other.jum)))     # sum()함수를 쓰던가 다른 함수를 만들어서 쓰던가
    
    def cal_list(self, jum) :       #인자 값이 있으면 꼭 매개변수로 받아서 사용하자!
        self.sum = 0
        
        for i in jum :
            self.sum += i
            
        return self.sum
    
st1 = Stud("장동건", [88,87,86])
st2 = Stud("장서건", [66,65,68])

st1.print()
st2.print()

(st2 + st1).print()