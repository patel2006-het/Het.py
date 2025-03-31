# Define three functions fun(), disp() and msg(). Store them in a list and call them one by one in a loop
def fun():
    print("this is fun")
def disp():
     print("this is disp")
def msg():
     print("this is msg")

functiob_list=[fun,disp,msg]

for func in functiob_list:
     func()