"""number = int (input("정수입력 > "))

if number % 2 == 0 :
        print("{} : 짝수입니다.".format(number))
else : 
        print("{} : 홀수입니다.".format(number)) 

print("::".join("1+2+3"))
#print("::".join("1","2","3"))
#print("::".join(1,2,3))
"""
number = int (input("정수입력 > "))

if number % 2 == 0 :
        print("\n".join(["{} : 짝수입니다."]).format(number))
else : 
        print("\n".join(["{} : 홀수입니다."]).format(number)) 

