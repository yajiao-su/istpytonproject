'''
Now You Code 4: Guess A Number

Write a program to play the classic "Guess a number" game.

In this game the computer selects a random number between 1 and 100.
It's your job to guess the number. Whenever you guess, the computer will
give you a hint of higher or lower. This process repeats until you guess
the number, after which the computer reports the number of guesses it took you.

For Example:

I'm thinking of a number between 1 and 100...
Your guess: 50
Too low. Guess higher.
Your guess: 75
Too high. Guess lower.
Your guess: 62
You guessed it in 3 tries.

Your indefinite loop should continue until your input guess equals the
computer generated random number.

Start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: Write Todo list then beneath write your code


# Write code here (some provided for you)
import random
number = random.randint(1,100) # random number between 1-100
print("I'm thinking of a number between 1 and 100...")
count=0
while True: 
    try:
        guess=input("Enter your guess here")
        count=count+1
        guess=int(guess)
        if guess==number:
            print("You guessed it in",count,"tries")
            break
        elif 1<guess<number:
            print("Your guess: %d" %(guess))
            print("You guessed too low. Guess higher.")
        elif number<guess<100:
            print("Your guess: %d" %(guess))
            print("You guessed too high. Guess lower.")
        else: 
            print("that's not in the range")
    except:
            print("that's not a number")
        
