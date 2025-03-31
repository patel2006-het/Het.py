def pattern(n):
    if(n==0):
        return               # here function can not procced further 
    print("*"*n)
    pattern(n-1)

pattern(5)    