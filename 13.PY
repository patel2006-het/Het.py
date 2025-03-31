# mylist=[1,6,3,4]

# squarelist=[i*i for i in mylist]

# print(squarelist)
datainput=[5,9,10,54.7,12]
even=[]
for item in datainput:
    if item%2==0:
        even.append(item)
print(even)          

suare=[i*i for i in even]
print(suare)
