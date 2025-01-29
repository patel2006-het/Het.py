# This program will check number is divisible by 10 or not.

def div_10():
    a = int(input("Enter number : "))

    if(a%10 == 0):
        print("Number is divisible by 10")
    else:
        print("Number is not divisible by 10")

div_10()