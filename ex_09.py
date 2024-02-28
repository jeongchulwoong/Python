#input()함수 명령 프롬프트에서 사용자로부터 데이터
#입력받을 때 사용

string = input("인사말을 입력하세요 :")

print(string)
print()

#number = int(number) 
number = input("숫자를 입력하세요:")
print(type(number)) #str

#int()함수 : 문자열을 int 자료형으로 변환
#float()함수 : 문자열을 float 자료형으로 변환

string_a = input("입력 A>")
int_a = int(string_a)
print(type(int_a))

string_b = input("입력 B>")
int_b = int(string_b)
print(type(int_b))


print("문자열 자료 : ", string_a+string_b)
print("문자열 자료 : ", int_a+int_b)