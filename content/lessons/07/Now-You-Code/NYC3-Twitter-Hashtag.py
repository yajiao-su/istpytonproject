'''
Now You Code 3: Twitter Hashtag Detector

Let's write a program which extracts the twitter hashtags from the text.

Example Run 1:

    Enter Tweet: You got a 50 on the exam? #iamsad for you!
    Hashtag: #iamsad
    
Example Run 2:

    Enter Tweet: #lol too funny #joke #haha
    Hashtag: #lol
    Hashtag: #joke
    Hashtag: #haha

Example Run 3:

    Enter Tweet: Happy birthday @mafudge
    Hashtag: none

HINT: to handle the 3rd case you must keep a runnning count of hashtags
you find in the Tweet.


As usual, start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: Write Todo list then beneath write your code

#input the sentence
#if the sentence has no hashtages then print
#if the sentence has hashtages then extract them
#and need to find if hastages in not in the character, if it does, then it's wrong
# Write code here
tweet=input("Enter a tweet here:")
each_word=tweet.split(" ")
count=0
if tweet.count("#")!=0:
    for i in range(0,len(each_word)):
        if(each_word[i].find('#')==0 and each_word[i].count("#")==1):
            print("Hashtage:%s" %each_word[i])
            count=count+1
        elif(each_word[i].find('#')>=0) and (each_word[i].count("#")==1):
            print("You have something wrong with the word %s\n A hashtage should always at the first place of a word." %each_word[i])
        elif(each_word[i].count('#')>1):
                  print("The word %s should not contain more than one hashtag!" %each_word[i])
        else:
                  continue
else:
    print("Hashtag: none")