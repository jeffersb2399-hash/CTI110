#Brandy Jefferson
#11 April 2026
#P2HW2
#This program will store grades entered in a list

print()
#Dictionary of modules 
modules = {'Module 1', 'Module 2', 'Module 3', 'Module 4', 'Module 5', 'Module 6'}
print()

#Get grades for each module from user
module_1 = float(input("Enter grade for Module 1:  "))
module_2 = float(input("Enter grade for Module 2:  "))
module_3 = float(input("Enter grade for Module 3:  "))
module_4 = float(input("Enter grade for Module 4:  "))
module_5 = float(input("Enter grade for Module 5:  "))   
module_6 = float(input("Enter grade for Module 6:  "))
print()

print("--------Results--------")
print()

#Find the lowest grade, highest grade, the sum, and the average in the list
lowest_grade = min([module_1, module_2, module_3, module_4, module_5, module_6])
highest_grade = max([module_1, module_2, module_3, module_4, module_5, module_6])
sum_grades = sum([module_1, module_2, module_3, module_4, module_5, module_6])
average_grade = sum_grades / 6

#Display the lowest grade, highest grade, the sum, and the average in the list
print(f"{'Lowest Grade:':20s}{lowest_grade:.1f}")
print(f"{'Highest Grade:':20s}{highest_grade:.1f}")
print(f"{'Sum of Grades:':20s}{sum_grades:.1f}")
print(f"{'Average:':20s}{average_grade:.2f}")
print()

print("-" *30)
print()

##================================
# Comment Block
#================================
#Display a blank line
#Creat a list of module names (Module 1, Module 2, Module 3, Module 4, Module 5, Module 6 )
#Display a blank line
#Ask the user to enter the grade for module 1
#Ask the user to enter the grade for module 2
#Ask the user to enter the grade for module 3       
#Ask the user to enter the grade for module 4
#Ask the user to enter the grade for module 5
#Ask the user to enter the grade for module 6
#Display a blank line
#Display the results header 
#Find the lowest grade in the list
#Find the highest grade in the list 
#Find the sum of the grades in the list
#Find the average of the grades in the list 
#Display the lowest grade
#Display the highest grade 
# Display the sum 
# Display the average 
#Display a line of dashes to separate the results


