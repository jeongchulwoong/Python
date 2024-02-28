try : 
    number_input_a = int(input("> Enter int : "))
    print("radius of a circle : ", number_input_a)
    print("radius of a round : ", 3.14 * number_input_a)
    print("radius of a round : ", 3.14 * number_input_a * number_input_a)

except Exception as valuerror:                                        #SyntaxError
    #print("Value Error check a Value")         #IndentationError
    print("type(valuerror) : ", type(valuerror))
    print("valerror : ", valuerror)
        
    


