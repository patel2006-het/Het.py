#  program to calculate the total money in any general store
sum=0
while(True):
    user=input(" enter a number")
    if(user!='q'):
        sum=sum+int(user)
        print("continue tour shopping")
    else:
        print("thanks for useing")
        print(f"your bill is {sum}")
        break # if break not use then loop continue forever
        


           

    