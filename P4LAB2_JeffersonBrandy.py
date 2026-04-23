# Brandy Jefferson
# 23 April 2025
# P4LAB2
# Use while loop and for loop together

'''
Get integer from user
Determing if interger is postive or negative
if number is positive, display multiplication table
if number is negative, tell user program cannot accept it
Ask user to run again?
If yes, run program
If no, end program'''

run_again = "yes"

while run_again != "no":

    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
    #displat multiplication table for that value and range (1-12)
        for item in range(1,13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values.")

    run_again = input("Would you like to run the program again? (yes/no): ")

#Loop has broken. User entered 'no'

print("Exiting Program...")
