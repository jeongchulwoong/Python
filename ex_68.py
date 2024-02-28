with open("info.txt","r") as file :
    for line in file :
        #strip() : 문자열 앞뒤에 있는 공백제거
        #split() : 문자를 구분
        name, weight, height = line.strip().split(",")  # ** 중요 **
        
        if (not name) or (not weight) or (not height) :
            continue
        bmi = (int (weight) / (int(height)/100 ) **2)    #m*2이므로 10000 곱한다
        
        
        if 25 <= bmi :
            result = "과체중입니다"
        elif 18.5 >= bmi : 
            result = "정상체중입니다"
        print("이름 : {}, 몸무게 : {}, 키 : {}, bmi : {}, 결과 : {}".format(name, weight, height, bmi,result))
        print()