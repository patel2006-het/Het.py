#   check armstrong number 
n=int(input("enter a number"))
copy=n
sum=0
order=len(str(n))

while(n>0):
    digit=n%10
    sum+=digit**order      # in python why we use '//'
    n=n//10               #  for example 88/10=8.8 and 88//10=8
    
if(sum==copy):
     print("yes,armstrong number")
else:
    print("not armstrong number")


    
 




