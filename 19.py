# Suppose there are two lists, one containing numbers from 1 to 6, and other containing numbers from 6 to 1.
# Write a program to obtain a list that contains elements obtained by adding corresponding elements of the two lists.
# (hint: use map and lambda functions)
l1=[1,2,3,4,5,6]
l2=[6,5,4,3,2,1]

l3=list(map(lambda l1,l2:l1+l2,l1,l2))
print(l3)