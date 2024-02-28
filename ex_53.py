def print_3_times():        #함수 만드는 키워드 : def 
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

#print_3_times()
print()


def print_n_times(value, n):
    for i in range(0,n):
        print(value)

print_3_times()
print("\n")
print_n_times("안녕하세요", 5)