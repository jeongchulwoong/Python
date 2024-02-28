def test() :
    print("Passed A point")
    yield(1)
    print("Passed B point")
    yield(2)
    print("Passed C point")
    yield(3)            #yield 키워드를 사용함으로써 제너레이터는 대량의 데이터나 무한한 시퀀스와 
                        #같은 경우에도 메모리를 효율적으로 사용하여 값을 생성할 수 있습니다.
    
output = test()
print("Passed D point")
a = next(output)
print(a)

print("Passed E point")
b = next(output)
print(b)

print("Passed F point")
c = next(output)
print(c)


