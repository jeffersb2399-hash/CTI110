# Brandy Jefferson
# 3 April 2026
# P1HW2
# This program calculates and displays travel expenses

print("----------This Program Calculates and Displays Travel Expenses----------")
print()
budget = input("Enter Budget: ")
print()
destination = input("Enter travel destination: " )
print()
fuel = input("How much do you think you will spend on gas? ")
print()
accommodations = input("Approximately, how much do you think you will spend on accommodation/hotel? ")
print()
food = input("Last, how much do you need for food? ")
print()
print("----------Travel Expenses----------")
print()
print("Destination:", destination)
print("Initial Budget:", budget)
print()

num1 = int(fuel)
num2 = int(accommodations)
num3 = int(food)

print("Feul:", fuel )
print("Accommodations:", accommodations)
print("Food:", food)
print()

sum_result = num1 + num2 + num3
final_result = int(budget) - sum_result 

print("Remaining Budget:", final_result)
print()

#================================
# Comment Block
#================================
# Display the message if the remaining budget is negative or positive
# Ask the user to enter budget
# Ask the user to enter travel destination
# Ask the user to enter how much they think they will spend on gas
# Ask the user to enter how much they think they will spend on accommodation/hotel
# Ask the user to enter how much they need for food
# Display the travel expenses
# Display the destination and initial budget
# Convert the fuel, accommodations, and food expenses to integers
# Display the fuel, accommodations, and food expenses   
# Calculate the sum of the fuel, accommodations, and food expenses
# Calculate the remaining budget by subtracting the sum of expenses from the initial budget
# Display the remaining budget





