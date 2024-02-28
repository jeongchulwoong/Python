i = 0
#a = input()
#print(type(a))



while True :
    print("{}번째 반복문입니다.".format(i))
    i = i + 1
    input_text = input(">종료하시겠습니까?(y,Y) : ")
   # if (input_text == 'y'or input_text == 'Y') :
    if (input_text in ['y', 'Y']) :
         print("반복을 종료합니다.")
         break
    else : 
        continue

    