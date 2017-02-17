'''
Now You Code 4: Fahrenheight to Celcius

Write a Python program to enter temperature in degrees Fahrenheight and convert
that temperature to degrees Celcius. 

For example:

    Enter temperature in deg F: 212
    That's 100.0 deg C

NOTES:
    - Research the converion formulas on your own.
    - Format output to one decimal place

Start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: Write Todo list then beneath write your code
#(°F - 32) x 5/9 = °C
#(°C × 9/5) + 32 = °F
temperature_in_deg_F=float(input("Enter the temperature in deg F here"))
temperature_in_deg_C=((temperature_in_deg_F-32))*5/9
print("temperature_in_deg_C is %.2f" % (temperature_in_deg_C))
 
