number = input(">정수입력")

number = int(number)

if number > 0:
#임시적으로 비워둘 때
    pass
else:
    #print("0보다 작습니다")
    pass
    
#리스트 : 여러가지 자료를 저장할 수 있는 공간구조

arry = [273, 32, 103, "문자열", True, False]
print(arry)
print(arry[0])
print(arry[:6])
arry[0] = "change"
print(arry)

list_a=[[1,2,3],[4,5,6],[7,8,9]]
#print(list_a[0][0])
#print(list_a[0][1])
#print(list_a[0][2])
print(list_a[0])
print(list_a[1])
print(list_a[2])

print(list_a[1][0])