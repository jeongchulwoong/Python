dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨"],
    "origin" : "필리핀" 
}

key = input("> 접근하고자 하는 키 : ")
# if, else ,in

if key in dictionary :
    print("{} 값이 존재 합니다.". format(key))
    print("{} : {}".format(key, dictionary[key]))
else :
    print("존재하지 않는 키에 접근하고 있습니다")