def test(a,b=10,c = 100) :  #변수명 일치가 중요
    print(a+b+c)

test(10,20,30)
test(a=10,b=100,c=200)
test(c=10, a=100, b=200)
test(10,c=200)

# def print_n_times(*values, n = 2) :      #키워드 매개변수
#     for i in range(n) :
#         for value in values :
#          print(value)
#     print()

# print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", 5)
