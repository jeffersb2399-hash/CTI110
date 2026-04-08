#Brandy Jefferson
#8 April 2026
#P2LAB1
#This program will calculate the diameter, circumference, and area of a circle.
print()

import math

#Get the radius from the user
radius = float(input("What is the radius of the circle? "))
print()

#calculate the diameter
diameter = 2 * radius

#Display the diameter with 1 decimal point
print(f"The diameter of the circle is {diameter:.1f}." )
print()


#calulate the circumference
circumference = 2 * math.pi * radius

#Display the circumference with 2 decimal places
print(f"The circumference of the circle is {circumference:.2f}")
print()

#Calculate the area
area = math.pi * radius ** 2

#Display the area with 3 decimal places
print(f"The area of the circle is {area:.3f}.")
print()

print()