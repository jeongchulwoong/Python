a, b = 10,20

print("#교환 전 값 : {}, {}".format(a, b))
print()

a,b = b, a

print("#교환 후 값 : {}, {}".format(a, b))

def test():
    return 10,20  
a,b = test()
print(print("#교환 후 값 : {}, {}".format(a, b)))
