#number = int("hi")      #ValueError
number = int("12345")
number += 10
print(number)
print()

number = int(52.123)
print(number)
print()


#number = int("52.123")      #ValueError
#print(number)
#print()

number2 = float("52.123")
print(number2)
print()

output_a = str(52)
output_b = str(52.273)
print(type(output_a), output_a)
print(type(output_b), output_b)
