numbers = [1,2,6,8,4,3,2,1,1,9,5,4,97,2,1,3,5,4,8,9,7,2,3]
#print(type(numbers[0]))

counter = {}

for number in numbers :
    if number in counter :
        counter[number] = counter[number] + 1
    else :
        counter[number] = 1
print(counter)
