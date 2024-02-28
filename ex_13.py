a = "Hello Python Programing...!"
a=a.upper()       #대문자
print(a)
print()
a=a.lower()
print(a)

input_a="""
    안녕하세요
문자열을의 함수를 
            알아봅니다.
"""
print(input_a)
print(input_a.strip())    #양옆의 공백 제거
print(input_a)
print()

# lstrip: 왼쪽 공백 제거 rstrip():오른쪽 공백 제거
print("TrainA10".isalnum()) #isalnum():문자열이 알파벳 또는 숫자로 구성되어 있는지 확인
print("10".isdigit())   #isdigit() : 문자열이 숫자로 인식될 수 있는것인지 확인

#찾는 문자가 존재하면 해당위치 index반환
#찾는 문자가 존재하지 않는다면 -1반환
output_a="안녕하세요".find("반녕")      #
print(output_a)

output_b="안녕안녕하세요".rfind("안녕")
print(output_b)
output_c="안녕안녕하세요".find("안녕")
print(output_c)
