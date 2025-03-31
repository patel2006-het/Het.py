# Write a program that defines a function convert() that receives a string containing
# a sequence of whitespace separated words and returns a string after removing all duplicate words 
# and sorting them alphanumerically. Hint: use set(), list () , sorted(), join()

def convert():
    str=input("enter a string")
    l_str=set(str)
    s_str=sorted(l_str)
    return "".join(s_str)

print(convert())    

