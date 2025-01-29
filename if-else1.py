# This program will print largest and smallest value  of two.
def large_small():
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    if(a>=b):
        print("The largest value is : ",a)
        print("The smallest value is : ",b)
    else:
        print("The largest value is : ",b)
        print("The smallest value is : ",a)

large_small()