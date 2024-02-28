charater = {
    
    "name" : "기사",
    "level" : 12,
    "items" : {                 #dictionary안에 dictionary 사용 가능
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]   
}
 
a = 10
b = 10 
print(charater)
#print(type("문자열") is str)   is 객체가 같은지 비교
#print(type(18) is int)
#print(a == b)       # == : 변수의 값을 비교
print(type([]) is list)
print(type({}) is dict)
print(type(100+2000) is int)

# for key in charater :
#     if type(charater[key])is dict :
#         print("{}의 값 {}: dict 입니다".format(key, charater[key]))
#     #print("{} : {}".format(key, charater[key]))
#     elif (type(charater[key])is list) : 
#         print("{}의 값 {}: list 입니다".format(key, charater[key]))
#     elif (type(charater[key])is int) :
#         print("{}의 값 {}: int 입니다".format(key, charater[key]))
#     else :
#         print("{}의 값 {}: str 입니다".format(key, charater[key]))
        
for key in charater :
    if type(charater[key])is dict :
        for small_key in charater[key] :
            print(small_key, ":", charater[key][small_key])
    #print("{} : {}".format(key, charater[key]))
    elif (type(charater[key])is list) : 
        for small_key in charater[key] :
            print(key, ":", small_key)
    elif (type(charater[key])is int) :
        print("{} : {}".format(key, charater[key]))
    else :
        print("{} : {}".format(key, charater[key]))
