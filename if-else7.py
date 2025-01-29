# This program will check entered year is leap or not.

def leap():
    a = int(input("Enter year : "))

    if(a%4 == 0):
        print("Year is leap year")
    else:
        print("Year is not a leap year")

leap()