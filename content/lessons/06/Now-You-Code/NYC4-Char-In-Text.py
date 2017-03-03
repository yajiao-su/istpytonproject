'''
Now You Code 4: Find a character in text

Description

Write a program to input a character, and then some text. It should then output
the number of times the character was found in the text.

Requirements:

#1 Write a function char_in_text which returns an int value as to
the count of that character in the text

Function: char_in_text
Arguments: char, text
Returns: count of char in text

#2 You're going to need a deterministic loop to iterate over each character in
the text. 

Example Run #1:

    Enter Character: e
    Enter Text: Mike Fudge
    The character 'e' appears 2 times in the text.
    
Example Run #2:

    Enter Character: x
    Enter Text: oakland
    The character 'x' appears 0 times in the text.
    
Start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: Write Todo list then beneath write your code
#Input the character
#Input text
#define a function to count characters in the text

# Write code here 
def char_in_text(character,text):
    count=0
    for i in range(0,len(text)):
        if character==text[i]:
            count=count+1
        else:
            continue
    return count


character=str(input("enter the character here:"))
text=str(input("Enter the text here."))
count=char_in_text(character,text)
print("the character %s appears %d times in the text." %(character,count))
