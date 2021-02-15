def fib1(n):
    """print the Fibonacci numbers upto n."""
    a,b = 0,1
    while a <= n:
        print(a)
        a,b = b, a + b

def fib2(n):
    """return the Fibonacci numbers up to n"""
    list = []
    a,b = 0,1
    while a <= n:
        list.append(a)
        a,b = b, a + b
    
    return list



