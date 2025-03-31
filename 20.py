# Generate the list of 10 different random numbers between -15 and 15.
# Create a new list by obtaining square of all numbers in a list.
l1=[2,5,8,7,4,1,-6,-3,-9,-15]
l2=list(map(lambda l1:l1*l1,l1))
print(l2)