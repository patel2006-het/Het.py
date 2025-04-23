# Write a program that receives an integer an input.
# If a string is entered instead of an integer, thenreport an error and give another chance to user to enter an integer.
# Continue this process till correctinput is supplied

def followup():
    try:
     n=int(input("enter a number"))
     print("you entered a integer",n)
    
    except ValueError:
       print("type integer")
       followup() 

    print(n)   

followup()

# while True:  # run always
#     user_input = input("Enter an integer: ")
#     try:
#         number = int(user_input)
#         print("You entered the integer:", number)
#         break
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")
