# Write a program that defines a function called frequency() which computes the frequency of 
# words present in a string passed to it. The frequencies should be returned in sorted order of words in the string.

def frequency(str):
    words=str.split()         #In Python, str.split() is a method that splits a 
    fre={}                    #string into a list of words based on whitespace by 'default'.

    for word in words:
        word=word.lower()
        fre[word]=fre.get(word,0) + 1  # *IMP* 
                                        #freq.get(word, 0) checks if word is already in freq.
                                        #  If word exists, it returns its current count.
                                        #  If word is not found, it returns 0 (default value)
                                        #  + 1 increments the count of word by 1.
                                        #  The updated count is then assigned back to freq[word

    sort_fre=sorted(fre.items())
    return sort_fre


str=input("enter a string")
print(frequency(str))

#       example of split function
# data = "apple(*_*)banana(*_*)grape(*_*)orange"                       
# fruits = data.split("(*_*)")  # Splitting using "(*_*)"
# print(fruits)

