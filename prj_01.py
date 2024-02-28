import random

my_list = [] 

def roll():
    
    return random.randint(1, 6)


for i in range(0,3) :
    my_list.append(roll())      #리스트에 추가는 항상 append

print(my_list)

for i in range(0, len(my_list)) :
    count = 0
    if my_list[i] == my_list[i+1] :
        
        count += 1
    