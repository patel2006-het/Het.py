# This program will write absolute value of given number.

def absolute():
    a = float(input("Enter number : "))

    if(a == 0):
        print("Absolute value is :",0)
    elif(a < 0):
        print("Absolute value is :",(-1)*(a))
    else:
        print("Absolute value is :",int(a))

absolute()