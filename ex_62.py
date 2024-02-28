def call_10_times(func2) :
    for i in range(10) :
        func2()

def print_hello():
    print("hi")

call_10_times(print_hello)

