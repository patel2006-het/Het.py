# This program will print major if person's age is above 18 otherwise minor.

def major_minor():
    a = int(input("Enter age : "))
    
    if(a>=18):
        print("Major")
    else:
        print("Minor")

major_minor()