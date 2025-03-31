
    #  expansion of sinx
import math

x=float(input("enter a value of x in radian "))
no_term=int(input("enter a number for expansion of sinx "))


sinx=0.0

i=1
while i<no_term+1:
    term= ((-1)**i+1)*(x**(i*2-1))/math.factorial(2*i-1)
    sinx+=term
    i+=1

print(sinx)
