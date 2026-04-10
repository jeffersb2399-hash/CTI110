#Brandy Jefferson
#10 April 2026
#P2LAB2
#Write a program that creates a dictionary

#Dictionary of cars and their miles per gallon
print()
cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

#Get keys from the dictionary
cars_keys = cars.keys()
print(cars_keys)
print()
print(*cars_keys, sep =",")
print()

#Get a car from user
car_name = input("Enter a vehicle to see it's mpg: ")
print()

#Get mpg for the given car
car_mpg = cars[car_name]
print(f"The {car_name} gets {car_mpg} miles per gallon.")
print()

#Get miles to be driven from user
miles_driver = float(input(f"How many miles will you drive the {car_name}? "))
print()


#Calculate gallons needed
gallons_needed = miles_driver / car_mpg

#Display Results
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driver} miles.")
print()



