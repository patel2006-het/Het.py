# This program will print given point is inside the circle or outside the circle or on the circle.
import math
def distance():
    x0,y0 = input("Enter co-ordinates of center of circle : ").split()
    x1,y1 = input("Enter co-ordinates of point that you want to check : ").split()
    r = int(input("Enter radius : "))
    x0 = int(x0)
    x1 = int(x1)
    y0 = int(y0)
    y1 = int(y1)
    
    a = pow(x1-x0,2)
    b = pow(y1-y0,2)
    c = a+b
    m = pow(c,1/2)

    if(m < r):
        print("Inside the circle")
    elif(m==r):
        print("On the circle")
    else:
        print("Outside the circle")

distance()