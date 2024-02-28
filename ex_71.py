def generator_func(x) : 
    print("First Input * 1: ")
    x *= 1
    yield x
    print("First Input * 2: ")
    x *= 2
    yield x
    print("First Input * 3: ")
    x *= 3
    yield x
for i in generator_func(1) :    #for 문을 쓰면 next가 필요 없음
    print(i)
    
gen_f = generator_func(1)
print(gen_f)

print(next(gen_f))
print(next(gen_f))
print(next(gen_f))