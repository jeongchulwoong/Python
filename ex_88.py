import ex_87

student = ex_87.Student() 

#student.__age = 20      #외부접근 금지이므로 value변환도 안됨.
student.name = "hansol"
#student("hansol", 25)

print(student.name)         
#print(student.__age)        # 접근 불가능
#print(student.get_age())       #함수로 리턴값으로 접근 가능    0
print(student._Student__age)    #접근가능 //  mangling으로 접근 하면 가능    0
student.set_Name("chul woong")
student.set_age(25)
print(student.get_name())
print(student.get_age())



