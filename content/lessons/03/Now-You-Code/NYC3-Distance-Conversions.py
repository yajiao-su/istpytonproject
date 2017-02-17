'''
Now You Code 3: Distance Conversions

Write a Python program to enter a distnace in feet then convert that
distance to yards and miles. 

For example:

    Enter distance in FEET:15000
    That's 5000.0 yards or 2.8

NOTES:
    - Research the converion formulas on your own.
    - Format output to one decimal place

Start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: Write Todo list then beneath write your code

distance_feet=float(input("Enter the distance in feet here"))
distance_yards = (distance_feet / 3.0)
distance_miles = (distance_feet / 5280.0)
print("Distance in yards is %.2f" % distance_yards)
print("Distance is miles is %.2f" % distance_miles)
