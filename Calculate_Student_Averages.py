students = [["Alice", "S001", [85, 90, 78]], 
            ["Bob", "S002", [80, 88, 92]], 
            ["Charlie", "S003", [95, 85, 87]], 
            ["David", "S004", [70, 75, 80]], 
            ["Eve", "S005", [100, 95, 98]]] 

averages = []  # Initialize an empty list to store averages

# Loop through each student to calculate their average, max, and min grades
for index in range(len(students)):
    
    # Extract the student's name and grades
    name = students[index][0] 
    grades = students[index][2] 

    # Calculate the average by summing the grades and dividing by the number of grades
    average = sum(grades) / len(grades)  
    
    # Get the highest and lowest grade for each student
    max_grade = max(grades)
    min_grade = min(grades)
    
    # Print the student's average, highest, and lowest grade
    print("Average:", average, " Max_grade:", max_grade, " Min_grade:", min_grade) 
    
    # Store each student's average in the list for later comparison
    averages.append(average)

# Find the highest average from the list
highest_average = max(averages)
print("Highest Average:", highest_average)
