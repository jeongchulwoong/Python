
for i in range(1,5) :
    print()
    for k in range(0, i) :
        print("*", end="")
print()

# A = input("정수를 입력하세요 :")  
# A = int(A)
# B = input("정수를 입력하세요 :") 
# B = int(B)
# if (A > 0 and B < 10) :
#     print(A * B)
output = ""
for i in range(1,10) : 
    for j in range(0,i) :
        output += "*"
    output += "\n"
print(output)
    