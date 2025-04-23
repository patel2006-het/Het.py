# Write a program that merges lines alternatively from two files and writes the results to new file. 
# If one file has less number of lines than the other,
# the remaining lines from the larger file should be simply copied into the target file
def mergefile():
    try:
        f1=open("file01.txt",'r')
        f2=open("file02.txt",'r')

        lines1=f1.readlines()
        lines2=f2.readlines()

        output=open("output_file.txt","w")
        max_length=max(len(lines1),len(lines2))
        for i in range(max_length):
            if i<len(lines1):
                output.write(lines1[i] +'\n')
            if i<len(lines2):
                output.write(lines2[i] +'\n')
        print("all set")        
        f1.close()
        f2.close()
        output.close()
    except:
        print("something wrong")

mergefile()




 