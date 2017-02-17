'''
Now You Code 3: Final Grade in IST256

Our Course Syllabus has a grading scale here:

http://ist256.syr.edu/syllabus/#grading-scale

Write a Python program to input a number of points earned out of 600 and then
outpus the registrar grade. After you get it working initially, re-write it
to handle bad input. 

For example:

    IST256 Grade Calculator
    Enter total points out of 600:  550
    Grade: A- 

Start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: List 

#1. input grade out of 600 points
#2. lookup letter grade (use an if else ladder for lower bound of each grade)
#3. print letter grade.

# TODO Write code here
print("IST256 Grade Calculator")
total_points=input("Enter total points out of 600:")
try:
    if 570<=float(total_points)<=600:
       print("Grade:A")
    elif 540<=float(total_points)<=569:
        print("Grade:A-")
    elif 510<=float(total_points)<=539:
        print("Grade:B+")
    elif 480<=float(total_points)<=509:
        print("Grade:B")
    elif 450<=float(total_points)<=479:
        print("Grade:B-")
    elif 420<=float(total_points)<=449:
        print("Grade:C+")
    elif 390<=float(total_points)<=419:
        print("Grade:C")
    elif 360<=float(total_points)<=389:
        print("Grade:C-")
    elif 300<=float(total_points)<=359:
        print("Grade:D")
    elif 0<=float(total_points)<=299:
        print("Grade:F")
except:
    print("It is not in the range")
