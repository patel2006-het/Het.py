# Write a function to create and return a list containing tuples 
# of the form (x,x2,x3) for all x between 1 and given ending value

def hee():
    l=[]
    n=int(input("enter a number"))
    for i in range(1,n+1):
        l.append((i,i**2,i**3))
    print(l)    

hee()




