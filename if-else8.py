# This program will check triangle is valid or not.

def triangle():
    a = int(input("Enter angle : "))
    b = int(input("Enter angle : "))
    c = int(input("Enter angle : "))

    if((a+b+c) == 180):
        print("Triangle is valid")
    else:
        print("Triangle is not valid")

triangle()