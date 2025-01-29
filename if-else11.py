# This program will check that given three points are in co-linear.

def co_linear():
    x1, y1 = (input("Enter first point (x1,y1): ")).split()
    x2, y2 = (input("Enter second point (x2,y2): ")).split()
    x3, y3 = (input("Enter third point (x3,y3): ")).split() 

    x1 = int(x1)
    x2 = int(x2)
    x3 = int(x3)
    y1 = int(y1)
    y2 = int(y2)
    y3 = int(y3)

    m = (y2-y1)/(x2-x1)
    n = (y3-y1)/(x3-x1)
    
    if(m == n):
        print("Points are co-linear")
    else:
        print("Points are not co-liner")

co_linear()