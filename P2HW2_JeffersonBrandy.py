#Brandy Jefferson
#11 April 2026
#P2HW2
#This program will store grades entered in a list

print()
#Dictionary of modules 
modules = {'Module 1', 'Module 2', 'Module 3', 'Module 4', 'Module 5', 'Module 6'}
print()

#Get grades for each module from user
module_1 = float(input("Enter grade for Module 1: "))
module_2 = float(input("Enter grade for Module 2: "))
module_3 = float(input("Enter grade for Module 3: "))
module_4 = float(input("Enter grade for Module 4: "))
module_5 = float(input("Enter grade for Module 5: "))   
module_6 = float(input("Enter grade for Module 6: "))
print()

print("--------Results--------")
print()

#Find the lowest grade, highest grade, the sum, and the average in the list
lowest_grade = min([module_1, module_2, module_3, module_4, module_5, module_6])
highest_grade = max([module_1, module_2, module_3, module_4, module_5, module_6])
Sum_grades = sum([module_1, module_2, module_3, module_4, module_5, module_6])
average_grade = Sum_grades / 6

#Display the lowest grade, highest grade, the sum, and the average in the list
print(f"Lowest grade: {lowest_grade:.1f}")
print(f"Highest grade: {highest_grade:.1f}")
print(f"Sum of grades: {Sum_grades:.1f}")
print(f"Average grade: {average_grade:.2f}")
print()

print("------------------------------------")
print()

##================================
# Comment Block
#================================
#Create a dictionary of modules
#Get grades for each module from user   
#Find the lowest grade, highest grade, the sum, and the average in the list
#Display the lowest grade, highest grade, the sum, and the average in the list


