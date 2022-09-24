# average4.py 
# 
# The following program averages numbers for the user, printing the result.  If you don't know where to start, paste the following text in your favorite text editor (such as notepad, if you are a Windows user) and save it as average4.py in a folder that contains other .py programs that work on your computer. 
# Please note that this is functional Python code. No claims are made about its quality, and it is arguably not very "Pythonic" in a number of ways.
# But I wrote it when I was even more of a newbie than I am now to explain it to someone who knew even less by some miracle.


scorenumber = input("How many numbers shall I average? ") 

# Here we explicitly set values for a few variables to zero. 
# We did this a lot in Pascal. 

# Notice that tempnumber2 is a floating point number. 
# Without some step equivalent to this one, if you average 2 and 1, 
# the average will be displayed incorrectly as 1. 

counter = 0 
tempnumber1 = 0 
tempnumber2 = 0.0 

# The numbers to be averaged are requested, added, and the value assigned to scoresum. 

while counter < scorenumber: 
    counter = counter + 1 
    tempnumber1 = input("Provide one of the numbers to average. ") 
    tempnumber2 = tempnumber1 + tempnumber2 
    print tempnumber2 
scoresum = tempnumber2 
print "The sum of your scores is " + str(scoresum) 

# The final result is determined and displayed. 

average = scoresum / scorenumber 
print "The average is " + str(average)

'''The program is called from within the interactive interpreter by importing the module, as follows.  The program instructs the user on how to proceed. 
  
>>>import average4 
How many numbers shall I average? 3 
Provide one of the numbers to average. 3 
3.0 
Provide one of the numbers to average. 2 
5.0 
Provide one of the numbers to average. 1 
6.0 
The sum of your scores is 6.0 
The average is 2.0 
>>> 
'''

