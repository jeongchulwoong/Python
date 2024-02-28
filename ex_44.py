# 1*99, 2*98

max_value = 0
a = 0
b = 0


for i in range(1,100) :
    j = (100 - i)
    
    current = i * j
    
    if max_value < current :
        max_value = current
        a = i   
        b = j
    # elif max_value > current : 
    #     continue
    print("{} * {} = {}".format(i, j, current))
print("최댓값 : {} * {} = {}".format(a, b,max_value))