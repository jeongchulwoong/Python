#try : 
#   Code that may throw an exception
#except : 
#    Code to run when an exception occurs

#Error that occur program before execution ==> syntax error
#Errors while running the program ==> exception error, runtime error

try : 
    number_input_a = int(input("> Enter int : "))
    print("radius of a circle : ", number_input_a)
    print("radius of a round : ", 3.14 * number_input_a)
    print("radius of a round : ", 3.14 * number_input_a * number_input_a)

except :
    print("Value Error check a Value")