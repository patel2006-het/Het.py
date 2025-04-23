# Given a text file, write a program to create another text file deleting the words 
# ‘a’, ‘the’, ‘an’ and replacing each one of them with a blank space.
def remove_words():
    word_to_remove=['a','the','an']
    try:
        with open("ex8.txt",'r')as f:
            text=f.read()
            words=text.split()
            new_text=[]
            for word in words:
                if word.lower() not in word_to_remove:
                 new_text.append(word)
            else:
                new_text.append("")

            sentence=" ".join(new_text)

        with open("ex8.txt",'w')as f:
            f.write(sentence)
    except:
       print("not ok ")

remove_words()
