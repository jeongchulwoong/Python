list_number = [52,273,32,72,100]

try : 
    number_input = int(input("> Enter int :"))
    #number_input2 = int(input("> Enter int :"))     #NameError
    print("{} th element : {}".format(number_input, list_number[number_input]))
except ValueError as exception :
    print("please Enter integer!")
    print(type(exception), exception)
except IndexError as exception :
    print("out of index in list!")
    print(type(exception), exception)
except NameError as exception :
    print("occur except NameError!")
    print(type(exception), exception)
except Exception as exception : 
    print("Throwing an uncaught exception!")
    print(type(exception), exception)
