# This program will print that student is pass or fail and its average.

def student():

    a = int(input("Enter marks of first subject : "))
    b = int(input("Enter marks of second subject : "))
    c = int(input("Enter marks of third subject : "))

    print("Total of subject is :",a+b+c)
    print("Average of three subjects is :",(a+b+c)/3)

    if(a<=39 or b<=39 or c<=39):
        print("The student is failed")
    else:
        print("The student is passed")
    print("In first subject student get : ")
    if(a<=39):
        print("F grade")
    elif(a<=44):
        print("P grade")
    elif(a<=49):
        print("C grade")
    elif(a<=54):
        print("B grade")
    elif(a<=59):
        print("B+ grade")
    elif(a<=69):
        print("A grade")
    elif(a<=79):
        print("A+ grade")
    elif(a<=100):
        print("O grade")
    else:
        print("NA grade")

    print("In second subject student get ")
    if(b<=39):
        print("F grade")
    elif(b<=44):
        print("P grade")
    elif(b<=49):
        print("C grade")
    elif(b<=54):
        print("B grade")
    elif(b<=59):
        print("B+ grade")
    elif(b<=69):
        print("A grade")
    elif(b<=79):
        print("A+ grade")
    elif(b<=100):
        print("O grade")
    else:
        print("NA grade")

    print("In third subject student get : ")
    if(c<=39):
        print("F grade")
    elif(c<=44):
        print("P grade")
    elif(c<=49):
        print("C grade")
    elif(c<=54):
        print("B grade")
    elif(c<=59):
        print("B+ grade")
    elif(c<=69):
        print("A grade")
    elif(c<=79):
        print("A+ grade")
    elif(c<=100):
        print("O grade")
    else:
        print("NA grade")

student()