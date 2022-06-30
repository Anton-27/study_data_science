def fib(n):
    
    if (n <= 1):
        return n
    else:
        return (fib(n-1) + fib(n-2))
        


print(fib(0))
print(fib(2))
print(fib(6))
# 0
# 1
# 8
    