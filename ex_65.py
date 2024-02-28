list_input_a = [1,2,3,4,5]
list_input_b = [1,1,2,3,5, 6, 7]

#inline lambda : 

print(list(map(lambda x : x*x, list_input_a)))
print()

print(list(filter(lambda x : x < 3, list_input_b)))


