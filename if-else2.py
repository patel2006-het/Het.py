# This program will print largest and smallest of three.
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))  
def large():
    
    if(a>b):
        if(a>c):
            print("The largest value is :",a)
        else:
            print("The largest value is :",c)
    else:
        if(b>c):
            print("The largest value is :",b)
        else:
            print("The largest value is :",c)
large()

def small():

    if(a<b):
        if(a<c):
            print("The smallest value is :",a)
        else:
            print("The smallest value is :",c)
    else:
        if(b<c):
            print("The smallest value is :",b)
        else:
            print("The smallest value is :",c)
small()