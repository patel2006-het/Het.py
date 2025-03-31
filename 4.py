# fibonacci series

num=int(input("enetr a number for fibonacci series"))

def rec(n):
    if n==0:
        return 0
    elif(n==1):
        return 1
    else:
        return rec(n-1)+rec(n-2)
    
print(f" value of fib{num} is {rec(num)}")



