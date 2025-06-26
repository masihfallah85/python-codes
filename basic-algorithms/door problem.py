# Door Problem

"""
In this problem, we have 'm' doors and 'n' students. Each student chooses a door that currently has 
the least number of students who have entered through it. 

If there are multiple such doors, the student picks one at random. We want to find the **maximum number 
of students that could pass through door 1** under this rule.

This is a classic application of the pigeonhole principle.
"""

#we use build-in math module for ceil() fucntion for pigeon hole rule
import math

#first we get number of doors and students
doors = int(input("enter number of doors: "))
students = int(input("enter number of students: "))
 
#now we use pigeon hole rule for solving the problem(ceiling of students/doors)
maximum_students_of_door_1 = math.ceil(students/doors)
print("maximum number of students passing through door one:",maximum_students_of_door_1)