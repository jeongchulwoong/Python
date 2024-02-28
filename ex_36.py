array = [273, 32, 103, 57, 52]

for element in array :
    print(element)

print(array)            #list
#print(type(element))       int 

#for i in array :
    #print(i)
    #print("{}번째 반복 : {}".format(i, array[i]))  indexError
for i in range(len(array)) :
       print("{}번째 반복 : {}".format(i+1, array[i]))  
#print(len(array))
print()
for i in range(4,-1,-1) :      #   rage (시작문, 종료문, 증감)
    print(i)

for i in reversed (range(5)): 
    print(i)
