                # removal of empty tuple from list
list=[(3,6),(),545,(),45]

filterlist=[]

for tup in list:
    if tup != ():
        filterlist.append(tup)  

print(filterlist) 

# import math         

# number=16
# m=math.sqrt(number)
# print(m)


