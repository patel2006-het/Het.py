# Write a program that defines a function count_alpha_digits() that accepts a string and 
# calculates the number of alphabets and digits in it. It should return these values as a dictionary

def count_alpha_digits(str):
    
    d={"alphabet":0 ,"digit":0,"space":0}
    for char in str:
        if char.isalpha():
           d["alphabet"]+=1
           
        elif char.isdigit():

            d["digit"]+=1
        else:
            d["space"]+=1    

    return d        



str=input("enter a string")
print(count_alpha_digits(str))