def print_n_times(*values, n = 2) :      #가변 매개변수 : 넘기는 값의 제한이 없다 그래서 후자에 써준다
    for i in range(n) :
        for value in values :
         print(value)
    print()

print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍")
