'''
Now You Code 4: Syracuse Weather

Write a program to load the Syracuse weather data from Dec 2015 in
JSON format into a Python list of dictionary. The file is:

"NYC4-syr-weather-dec-2015.json"

After you load this data calculate the number of days where the
'Mean TemperatureF' is above freezing ( > 32 degrees)

Store the days above freezing and below freezing into a dictionary
and then print out the dictionary like this:

{'below-freezing': 4, 'above-freezing': 27}

(It was a warm December by Syracuse Standards!)

'''

# TODO: Write Todo list then beneath write your code
#import json
#write a function
#input the file
#enumerate the data

# Write code here
import json

def document():
    f=open("NYC4-syr-weather-dec-2015.json",encoding='utf8')
    file=f.read
    load=json.loads(file)
    return load
data=document()

abovef=0
belowf=0

for i in data:
    if (i.get("Mean TemperatureF",0)<=32):
        abovef+=1
    else:
        belowf+=1
print("In avarage daily temperature, there are %d days are above freezing and %d days are below freezing." %(above,belowf))
