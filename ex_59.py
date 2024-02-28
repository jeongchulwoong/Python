#튜플 : 리스트와 다른 점 : 한번 결정된 값은 수정불가

tuple_test = (10,20,30)

print(tuple_test)
print(tuple_test[0])
#tuple_test[0] = 100    대입연산자 append함수 등등 다 안됨
print(tuple_test)

a,b = 10, 20
print(a, b)

[a,b] = [10, 20]
print("a = {}, b = {}".format(a, b))

(a,b) = (10, 20)
print("a = {}, b = {}".format(a, b))

