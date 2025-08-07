#Dictionary_student_grades.py

"""
In this script we have some grades for eahc student,we show each student average score alongside whole class average value.
"""

#Create dictionary of students and their grades
dict_student_grades = {
    "Susan" : [92,78,84],
    "Adam" : [70,78,100],
    "Azizi" : [87,45,76]
    }

#Create variables for total grades and total number of grades
total_grades = 0

total_numbers = 0


#Loop through dictionary and print average of scores
for name,grades in dict_student_grades.items():

    print(f"{name} : {sum(grades) / len(grades)}")

    total_grades += sum(grades)

    total_numbers += 1

#Print average of class
print(f"average of entire class: {total_grades / total_numbers}")