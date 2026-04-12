# Brandy Jefferson
# 12 April 2026
# P2HW1
# This program calculates and displays travel expenses

print()
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
print(f"{'Destination:':25s} {destination}")
initial_budget = float(budget)
print(f"{'Initial Budget:':25s} ${initial_budget:.2f}")

num1 = float(fuel)
num2 = float(accommodations)
num3 = float(food)

print(f"{'Fuel:':25s} ${num1:.2f}")
print(f"{'Accommodations:':25s} ${num2:.2f}")
print(f"{'Food:':25s} ${num3:.2f}")
print('-'*35)
sum_result = num1 + num2 + num3
final_result = float(budget) - sum_result 

print(f"{'Remaining Budget:':25s} ${final_result:.2f}")
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
# Convert the fuel, accommodations, and food expenses to float
# Display the fuel, accommodations, and food expenses with :.2f decimal places
# Calculate the sum of the fuel, accommodations, and food expenses
# Calculate the remaining budget by subtracting the sum of expenses from the initial budget
# Display the remaining budget with :.2f decimal places





