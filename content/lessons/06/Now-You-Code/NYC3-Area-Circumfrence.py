'''
Now You Code 3: Area and Circumfrence

Write a program to input the radius of a cicle, then output the area
and circumfrence of that circle. Feel free to research the formulas online.

Requirements:

#1 Import the Python library math, so you can use the constant math.PI

#2 The program should handle bad input (entering non numerical values should
not cause a run-time error).

#3 Be sure to write two functions:

Function: calc_area
Arguments: radius
Returns: circle's area

Function: calc_circ
Arguments: radius
Returns: circle's circumfrence

Example Run #1:

    Enter Circle Radius : 1
    A circle with radius 1.000 has a
    Circumfrence of 6.283
    and an Area of 3.142

Example Run #2:

    Enter Circle Radius : r
    Invalid radius!

As usual start out your program by writing your TODO list of steps
you'll need to solve the problem!

'''

# TODO: Write Todo list then beneath write your code
#input the radius of a circle
#use the equation to get the area and the circumference 
#area=πr2
# Write code here 
import math
def cal_area(r):
    cal_area=math.pi*r**2
    return cal_area
def cal_circ(r):
    cal_circ=2*math.pi*r
    return cal_circ


try:
    r=float(input("Enter radius here:"))
    cal_area=cal_area(r)
    
    cal_circ=cal_circ(r)
    print("A circle with radius %.3f has an area of %.3f and a circumference of %.3f." %(r,cal_area,cal_circ))
except:
    print ("that can't be convert to a float.")
    
  
    
    
