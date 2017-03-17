'''
Now You Code 4: Email Harvesting Training

Description

Write a program to extract the email addresses from the mailbox
file "NYC4-mbox-short.txt" and save them into another file
"NYC4-emails.txt" with one extracted email address per line.

The best way to find the emails in the mailbox file is to search
for lines in the file that begin with "From:". When you find an email
write just the address (not "From:" and the address) to
"NYC4-emails.txt", and don't worry about duplicates.

The program should print the number of emails it wrote to the file.

Example Run:

Wrote 27 emails to NYC4-emails.txt


Start out your program by writing your TODO list of steps
you'll need to solve the problem!
'''

# TODO: Write Todo list then beneath write your code
#connect the file to the code 
#find each line in the code
#count the number of emails it wrote to the file.
# Write code here 

readname="NYC4-mbox-short.txt"
writename="NYC4-emails.txt"
count=0
with open(writename, 'w') as f_w:
    f_w.write('')
with open(readname, 'r') as f_r:
    for line in f_r:
        if line.startswith("From:")==True:
            count=count+1
            with open(writename,'a')as f_w:
                f_w.write("%s\n" % line.replace('From: ','').strip())
print("Wrote %d emails to %s" %(count,writename))