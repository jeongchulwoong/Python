example_dictionary = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C"
}

print("#딕션너리의 item()함수")
print("iems() : ", example_dictionary)
print("iems() : ", example_dictionary.items())

print("#딕션너리의 item()함수와 반복문 조합 하기")

for key, element in example_dictionary.items() : 
    print("dictionary[{}] = {}".format(key, element))

for key, element in example_dictionary.items() : 
    print("dictionary[{}] ".format(key))
