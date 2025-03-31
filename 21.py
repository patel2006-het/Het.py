# Consider the following list:
# lst = ['madam','Python',"malayalam",12321]
# Write a program to print those strings which are palindromes.
lst = ['madam','Python',"malayalam",12321]
lst2=list(reversed(lst))

        

haha=list(filter(lambda word:str(word)==str(word)[::-1],lst))
print(haha)