   
input_string=input("enter a string")
def countstring(input_string):
    upper_count=0
    lower_count=0
    for char in input_string:
        if char.isupper():
            upper_count+=1
        elif char.islower():
            lower_count+=1
    counts={
        "upper":upper_count,
        "lower":lower_count
    } 
    return counts


result=countstring(input_string)

print("the uppercase letter is ",result["upper"])
print("the lowercase letter is ",result["lower"])
