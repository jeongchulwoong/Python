#in연산자 : 문자열 내부에 어떤 문자열이 있는지 확인
print("안녕"in "안녕하세요")    #True
print("잘자"in "안녕하세요")
print()

#split()함수 : 문자열을 특정한 문자로 자름
a="10 20 30 40 50".split()
print(a)
a="10 20 30 40 50".split()
print(a)

#Python 3.6부터
string_a=f'{10}'
print(string_a)
print(f"3+4={3+4}")

data=['별', 2, 'M', '경기도 안산시 중앙동','Y']
output = """
    이름 : {}
    나이 : {}
    성별 : {}
    지역 : {}
    중성화 여부 : {}
    
""".format(*data)
print(output)
