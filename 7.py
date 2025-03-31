     #  p2 from list
l=[]

while len(l)<4:

   n=int(input("enter a number")) 
   l.append(n)
    

print(l)


m=int(input("enter a number"))
if m in l:
   print(f" index of given number {m } is {l.index(m)}")




