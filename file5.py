# Write a program to copy contents of one file to another.
# While doing so, replace all lowercase characters into uppercase character
def copytouppercase ():
    input_file="exam.txt"
    output_file="finalout.txt"
    try:
        material=open("exam.txt",'r')
        text=material.read()
        upper_text=text.upper()
        destination=open("finalout.txt",'w')
        destination.write(upper_text)
    
        material.close()
        destination.close()
    except:
       print("something wrong happen")

copytouppercase()