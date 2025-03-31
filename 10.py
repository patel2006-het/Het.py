# A palindrome is a word or phrase that reads the same in both directions.
# Write a program that defines a function ispalindrome() which checks whether
# a given string is a palindrome or not. Ignore spaces and case mismatch while checking for palindrome.
def ispalindrome():
    sentence=input("enter a sentence")
    l_sentence=list(sentence)
    check=[]
    for i in l_sentence:
        check.append(i)

    check.reverse()

    
    print(f"original order{l_sentence}")
    print(f"reverse order{check}")
    if(l_sentence==check):
            print("palindrome")
    else:
            print("not palindrome")


ispalindrome() 

        