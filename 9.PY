def ispangram():
    alphaset={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "}
    sentence=input("enter sentence for pangram identifier")
    set_sentence=set(sentence)
    set_sentence_lower={char.lower() for char in set_sentence }
   
    if(set_sentence_lower==alphaset):
            print(" yes it is parangram")
    else:
            print("not parangram")

ispangram()            
       

 