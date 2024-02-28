list_input_a=["52","273", "32", "spy", "103"]

list_number = []

for item in list_input_a :
    
    try :
        float(item)
        list_number.append(item)
    except :    
        print("Error")

print("list_input_a have inside number : {}".format(list_input_a))
print()
print("Now list_number have inside number : {}".format(list_number))

