def count():
    in_string=input("enter a string")
    upper_count=0
    lower_count=0
    for char in in_string:
        if(char.isupper):
            upper_count=upper_count+1
        elif(char.islower):
            lower_count=lower_count+1
    return{"uppercount":upper_count,"lowercount":lower_count}

print(count())