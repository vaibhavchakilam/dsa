def factorial(n):
    if (n == 1):
        return 1
    else:
        return n*factorial(n-1)

def fact(n):
    k = factorial(n)
    print(f"The factorial of {n} is {k} ")
    
def fibonacci(n):
    if (n == 0):
        return  0 
    elif (n == 1):
        return  1 
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def fib_series(n):
    for i in range(n):
        k = fibonacci(i)
        print(k)
        i = i+1



fact(5)
fib_series(5)