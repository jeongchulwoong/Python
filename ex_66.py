
#file open and close
"""
file = open("basic.txt", "w")   #write
file.write("Hello Python Programing...!")

file.close()
"""
# file.close() auto close file      with as 
with open ("basic2.txt", "w") as file :
    file.write("Hello Python Programing...!")
    
with open ("basic.txt", "r") as file :
    contents = file.read()
print(contents)
