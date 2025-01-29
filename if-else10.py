# This program will check for ractangle its area is greater than its perimeter or not.

def rect():
    a = int(input("Enter length : "))
    b = int(input("Enter width : "))

    if((a*b)>(2*(a+b))):
        print("Area of rectangle is greater than its perimeter")
    elif((a*b) == (2*(a+b))):
        print("Area of rectangle is equal to its perimeter")
    else:
        print("Area of rectangle is not greater than its perimeter")

rect()