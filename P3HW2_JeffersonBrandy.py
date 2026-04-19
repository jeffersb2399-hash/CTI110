#Brandy Jefferson
#18 April 2026
#P3HW2
#The program is to display the following (Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay).

print()
#Request employee info
name = input("Enter employee name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly pay rate: "))

# Evaluate overtime
if hours >40:
    # Calculate overtime hours
    overtime_hours = hours -40
    #Calculate over pay
    overtime_pay = overtime_hours * (rate * 1.5)
    #Calculate salary for regular hours
    regular_pay = 40 * rate
    #Calculate gross pay
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours * rate
    gross_pay = regular_pay

#Display results
print(30 * "-")
print("Employee Name: ", name)
print()
print(f'{"Hours Worked:":<20s}{"Pay Rate:":<15s}{"Overtime Hours:":<20s}{"Overtime Pay:":<20s}{"Regular Pay:":<20s}{"Gross Pay:":<20s}')
print(105 * "-")
print(f'{hours:<20}{rate:<15.2f}{overtime_hours:<20.2f}{overtime_pay:<20.2f}{regular_pay:<20.2f}{gross_pay:<20.2f}')
print()
