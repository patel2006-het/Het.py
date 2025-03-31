# A list contains names of Faculty Members. 
# Write a program to filter out those names whose length is more than 8 characters.

faculty=["rama","niyati","ankur","shivangi","sivaraman","vima"]
bolte=list(filter(lambda word:len(word)>=8,faculty))
print(bolte)        