array = []

for i in range(0,20,2) :
    print("i =", i)
    array.append(i * i)
print(array)

array = [i*i for i in range(0,20,2)]    #list comprehension 리스트 내포
print(array)

array = ["자두", "사과", "초콜릿", "바나나", "체리"]

output = [fruit for fruit in array if fruit != "초콜릿"]
print(output)