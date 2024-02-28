#반복문

print(range(10))        #rage(0,10)
print(list(range(10)))      #리스트 구조로 보여줌

a = int()
#print(type(a))
for i in range(10) :    #0 ~ 9
    print("{} 반복문 출력".format(i))
array = [1,2,3,4,5]
print()
for i in array :
    print(i)
print()

list_of_list = [[1,2,3], [4,5,6,7], [8,9]]
for items in list_of_list :
    print(items)        #[8,9]
print()
#print(items)       [8,9]
for items in list_of_list :
    for i in items :
        print(i)
