#Brandy Jefferson
#23 April 2026
#P4HW1
#This program will store grades entered in a list

print()

# Ask user for number of scores they would like to enter
num_scores = int(input("How many scores would you like to enter? "))
print()

# Create an empty list to store the grades
scores = []

# Get grades from user and store them in the list
for i in range(num_scores):
    score = float(input(f"Enter score # {i + 1}: "))
    scores.append(score)
print()


#Evaluate if the score is valid
for score in scores:
    if score < 0 or score > 100:
        print(f"Invalid score: {score}. Scores should be between 0 and 100.")

#If invalid score is found, reenter and update the score in the list
for i in range(len(scores)):
    if scores[i] < 0 or scores[i] > 100:
        new_score = float(input(f"Enter score # {i + 1} again: "))
        scores[i] = new_score

#Find the lowest score in the list
lowest_score = min(scores)

#Update the list with the modified list
modified_list = scores.copy()

#Remove the lowest score from the modified list
modified_list.remove(lowest_score)

#Calculate the sum of the modified list
sum_modified = sum(modified_list)

#Calculate the average of the modified list
average_modified = sum_modified / len(modified_list)
print()

print("-----------Results-----------")

#Display the lowest score, highest score, the sum, and the average in the list
print(f"{'Lowest Score:':15s}{lowest_score:.1f}")
print(f"{'Modified List:':15s}{modified_list}")
print(f"{'Sum of Scores:':15s}{sum_modified:.1f}")
print(f"{'Score Average:':15s}{average_modified:.2f}")

print("-" *30)

#Determine letter grade for average
if average_modified >= 90:
    letter_grade = 'A'
elif average_modified >= 80:
    letter_grade = 'B'  
elif average_modified >= 70:
    letter_grade = 'C'
elif average_modified >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'
print(f"{'Your grade is: ':}{letter_grade}")
print()
    

#Comment
# Ask user for number of scores they would like to enter
# Create an empty list to store the grades
# Get grades from user and store them in the list
#Evaluate if the score is valid
#If invalid score is found, reenter and update the score in the list
#Find the lowest score in the list
#Update the list with the modified list
#Remove the lowest score from the modified list
#Calculate the sum of the modified list
#Calculate the average of the modified list
#Display the lowest score, highest score, the sum, and the average in the list
#Determine letter grade for average




