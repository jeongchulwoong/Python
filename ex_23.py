list_a = [1,2,3,4,5]
#list_b = [4,5,6]

print("#리스트 뒤에 요소 추가하기")

list_a.append(9)        #c에서는 선언뒤에 추가가 안되지만 파이썬은 선언 뒤 요소 추가 가능 
list_a.remove(9)
print(list_a)
print()

print("#리스트에 요소 추가하기")

#list_a.insert(6)    #TypeError
list_a.insert(0,10)
print(list_a)
print(len(list_a))

list_a.extend([6,7,8])
print(list_a)

del list_a[0]
print(list_a)
print(len(list_a))

list_a.pop(2)
print("pop(2) : ", list_a)      #꺼내오는 것 사라지는 것이 아님 

del list_a[3:7]
print(list_a)
print()

#del list_a
del list_a[0:]
print(list_a)
print()
# 1,2,2
list_a.append(1)
list_a.append(2)
list_a.append(2)

print(list_a)

print()     # [1,2,2]

#값으로 제거 2제거

list_a.remove(2)    #remove는 값으로 제거
list_a.remove(1)
print(list_a)   #[2]

list_a.clear()
print(list_a)


