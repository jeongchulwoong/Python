#i = 0

# while i < 10 :
#     print("{}번째 반복입니다".format(i))
#     i = i + 1
    
list_test = [1,2,1,2]
value = 2

#리스트에서 2를 제거한 리스트 출력
while value in list_test:
    list_test.remove(value)
print(list_test)
