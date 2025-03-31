# If a positive integer is entered through the keyword,
# write a recursive function to obtain the prime factors of the number

def moj(n):
    l=[]
    for i in range(1,n):
        if(n%i==0):
            l.append(i)
    return l

n=int(input("enter a number"))
print(moj(n))
        

