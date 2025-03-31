# Write a recursive function to obtain length of a given string

def length(s1):
    count=0
    for char in s1:
        count+=1
    return count    

s1=input("enter a string")
print(length(s1))
     