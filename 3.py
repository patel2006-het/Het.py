# str = input("enter a string :")
# print(len(str))

str1=input("enter a first string")
str2=input("enter a sec string")

def remove(str1,str2):
    str3 = str1.replace(str2, " ")
    print("reslting string after removal",str3)

remove(str1,str2)  