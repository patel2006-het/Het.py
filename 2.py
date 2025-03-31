#  factorial and it's zero

number=int(input(" enter a number"))
# def factorial(number):
#     if(number==0 or number==1):
#         return 1
#     # return number*factorial(number-1)
#     else:
#         return number*factorial(number-1)

def countzero(number):   
    
    count=0
    i=5
    while(number//i!=0):
        count+=int(number/i)
        i=i*5
    return count    
      

# print(factorial(number))
print(countzero(number))
