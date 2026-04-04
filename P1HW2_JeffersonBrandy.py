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



