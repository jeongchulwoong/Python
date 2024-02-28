def print_n_times(n, *values) :      #가변 매개변수 : 넘기는 값의 제한이 없다 그래서 후자에 써준다
    for i in range(0, n) :
        for value in values :
         print(value)
    print()

print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")
print("\n")

def print_n_times2(value, n = 2) :      #default 
    for i in range(n) :
        print(value)

print_n_times2("안녕하세요", 3)         # 넘기는 인자 값이 우선 3번 반복