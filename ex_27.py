numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]     #리스트 구조 안에 숫자가 들어가면 자동으로 int 
#print(type(numbers[9]))
sorted_number = sorted(numbers)
for i in sorted_number:
    if i > 100 :
        #print("100 이상인 숫자는 ", i, "입니다.") 
        print("100 이상인 숫자는 {} 입니다.".format(i))
print()

for i in sorted_number :
    if i % 2 == 0 :
        print("{} 짝수 입니다.".format(i))
    else :
        print("{} 홀수 입니다.".format(i))
        print()
print()
# for i in sorted_number :
#     if i % 2 == 1 :
#         print("{} 홀수 입니다.".format(i))

# 숫자 길이(자릿수)계산 1(한자리) 12(두자리) 123(세자리)

#sorted_number = str(sorted_number)
for i in sorted_number :
    if len(str(i)) == 1 : 
        print("{}은 한자리 숫자입니다.".format(i))
    elif len(str(i)) == 2 :
        print("{}은 두자리 숫자입니다.".format(i))
    else :
        print("{}은 세자리 숫자입니다.".format(i))



