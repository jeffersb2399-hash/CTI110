#Brandy Jefferson
#26 April 2026
#P4HW2
#Salary calculator with loops

print()
#Request employee info
name = input("Enter employee's name or 'done' to finish: ")

# Create Accumulator variables for overtime pay, regular pay, and gross pay and employee count
overtimepay_total = 0
regularpay_total = 0    
grosspay_total = 0
employee_count = 0

while name != 'done':
    #Add to employee count plus one
    employee_count += 1
    #Ask for employmee info
    hours = float(input("How many hours did "+name+ " work this week? "))
    rate = float(input("What is " + name + "'s hourly pay rate? "))
  
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

    # Add accumulator variables for overtime pay, regular pay, and gross pay
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay

#Display results for this employee
    print(30 * "-")
    print("Employee Name: ", name)
    print(f'{"Hours Worked:":<20s}{"Pay Rate:":<15s}{"Overtime Hours:":<20s}{"Overtime Pay:":<20s}{"Regular Pay:":<20s}{"Gross Pay:":<20s}')
    print(105 * "-")
    print(f'{hours:<20}{rate:<15.2f}{overtime_hours:<20.2f}{overtime_pay:<20.2f}{regular_pay:<20.2f}{gross_pay:<20.2f}')

    name = input("Enter employee's name or 'done' to finish: ")

print("Total number of employees processed: ", employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total, ',.2f'))
print("Total amount paid for regular hours: $", format(regularpay_total, ',.2f'))
print("Total amount paid in gross pay: $", format(grosspay_total, ',.2f'))
print()



