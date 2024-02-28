def fatorial(n):        #   **재귀함수** 
    
    if n == 0:
        return 1
    else : 
        return n * fatorial(n-1)
    
print("1! : ", fatorial(1))
print("2! : ", fatorial(2))
print("3! : ", fatorial(3))
print("4! : ", fatorial(4))
print("5! : ", fatorial(5))