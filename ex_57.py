def return_test() :
    print("A위치입니다.")
    return 100
    print("B위치입니다.")
    
value = return_test()
print(value)   #100

#None  넘어온 값이 없다

def sum_all(start = 0, end = 100, step = 1) :
    output = 0
    
    for i in range(start, end+1, step) :
        output += i
    return output
print("sum_all : ", sum_all(10))
print("sum_all : ", sum_all(end = 50))
print("sum_all : ", sum_all(end = 100, step = 2))