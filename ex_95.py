class Par1 :
    a = 10
    b = 20
    def __init__(self) :
        print("부모생성자")
    
    def fn_1(self) :
        print("부모1 fn_1() 실행")
    
    def fn_2(self) :
        print("부모1 fn_2() 실행")

class Child1(Par1) :
    
    c = 3333
    
    def fn_3(self) :
        print("자식1 fn_3() 실행")
pp1 = Par1()
cc1 = Child1()
print(pp1.a)
print(pp1.b)
#print(pp1.c)       AttributeError
print(cc1.b)
pp1.fn_1()
pp1.fn_2()
cc1.fn_1()      #가능 자식이 부모한테 있는 것은 다 사용가능
print("---------------------------------")


    
