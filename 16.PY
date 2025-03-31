#  here is the code for remove the repeating digit in the list
def remove_duplicates(l):
    unique_list = []
    for item in l:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage
l = [34,3,56,2,1,2,5,2,65,45,55,85,0]
print(remove_duplicates(l))

# A list contains rupee denominations like 500, 200, 100, 50, 20, 10, 5, 2 and
# 1. Accept amount from the user and calculate minimum number of notes required 
# for disbursement from ATM. E.g. if amount is 1254, the user will get
#  2 notes of Rs. 500, 1 note of Rs. 200, 1 note of Rs. 50 and 2 notes of Rs.

def atm(amount):
    denomination=[500,200,100,50,20,10,5,2]
    notecount={}

    for note in denomination:
        if amount>=note:
            count=amount//note
            notecount[note]=count
            amount=amount%note       # amount value change to 254

    return notecount     

amount=int(input("enter a valid amount for withdrawing money"))
notes=atm(amount)       #This function calculates how many notes of each denomination are required and returns a dictionary.
#The dictionary notes stores denominations as keys and the corresponding count of notes as values

for note,count in notes.items():          #notes.items() returns key-value pairs from the dictionary.

    print(f"RS{note} and {count}")


    