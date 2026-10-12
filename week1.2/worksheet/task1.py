# Worksheet 1.2: Task 1 Solution

import sys

grade = input("Enter your grade please: ")
if not grade.isdecimal():
    sys.exit("Error: Grade must be an integer between 0 and 100")
grade = int(grade)
if grade < 0 or grade > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")  
if grade < 40:
    result = "Fail"
elif grade < 70:
    result = "Pass"
else: 
    result = "Distinctiom"
print(grade, "is a", result)    
