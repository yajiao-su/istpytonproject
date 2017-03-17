'''
Now You Code 3: Sentiment 2.0

Let's improve on our basic sentiment analyzer in Python.

Copy the code from 1.0 most of it will be the same.

We will improve on this program by writing a user-defined
function load_words() to load the positve or negative words from a file.

For example, instead of:

pos = "happy glad joy"

we do this:

pos = load_words("NYC3-pos.txt")

We can now make the program "smarter" simply by adding positive and
negative words to the text files!


'''

# TODO: Write Todo list then beneath write your code
#write function for test
#connect files to the code
#check if the word in the text
#use the while loop to set input
# Write code here
def load_words(filename):
    with open(filename,'r') as f:
        return(f.read().split(' '))
def sentiment(positive_text,negative_text,input_text):
    each_word=input_text.split(' ')
    list_symbol=(' ', '!', '@', '$', '%', '^', '&', '*', '()', '_', '-', '+', '=', '{}', '[]')
    score=0
    for i in range(len(each_word)):
        if each_word[i].endswith(list_symbol)==True:
            each_word[i]=each_word[i][0:(len(each_word[i])-1)]
        if each_word[i] in positive_text:
            score=score+1
        if each_word[i] in negative_text:
            score=score-1
        elif each_word[i].startswith(list_symbol)==True:
            each_word[i]=each_word[i][1:(len(each_word[i]))]
            if each_word[i] in positive_text:
                score=score+1
            if each_word[i] in negative_text:
                score=score-1
        else:
            if each_word[i] in positive_text:
                score=score+1
            if each_word[i] in negative_text:
                score=score-1
    return score
positive_text=load_words("NYC3-pos.txt")
negative_text=load_words("NYC3-neg.txt")
while True:
    input_text=str(input("Enter your sentence here to detect the sentiment score"))
    if input_text=="quit":
        break
    else:
        score=sentiment(positive_text,negative_text,input_text)
        if score==0:
            state="neutral"
        elif score>0:
            state="positive"
        elif score<0:
            state="negative"
        print("Your sentiment score is %d,and your state is %s" %(score,state))
          
              