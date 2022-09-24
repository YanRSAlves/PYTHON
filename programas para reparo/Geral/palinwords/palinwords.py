##############################################################
#
# ACM Programming Challenge 
# http://acm.uva.es/problemset/v2/257.html
# 
# My attempt at answering the Palinwords problem
# This was pretty easy after Gregor LINGL did all the hard work
#
# Eoghan Barr, Ireland
# eoghan.barr@propylon.com
# http://smalleyboy.nav.to
##############################################################

def is_palindrome(w):	
    # if w is empty
    # or first character equals last character and 
    # word between those two also forms a palindrome
    return w == '' or (w[0]==w[-1]) and is_palindrome(w[1:-1])

def count_palindromes(word):
    palindromes = []  # will collect all occuring palindromes
    for i in range(len(word)):
        for j in range(len(word)-i):
            sub = word[j:j+i+1]
            if not sub in palindromes and is_palindrome(sub):
                palindromes.append(sub)
    return palindromes

def count_palinwords(word):
    palindromelist = count_palindromes(word)
    templist = []	# will contain candidate palinwords
    palinwordlist = []  # will collect confirmed palinwords
    for palindrome in palindromelist:
        if len(palindrome) >=3:
    	    templist.append(palindrome)
    	if len(templist) >=2 and not word in templist: 
    	    palinwordlist = templist
            print word #For the output specified by ACM, or the following which looks nicer :-)
            #print "The following string is palinword : %s which contains: %s " %(word,palinwordlist)
   

import sys
import string
if len(sys.argv) == 2:   			# if command-line argument is present ...
    input = open(sys.argv[1],'r').read() 	# read file
else:                                      	# default test-data
    input = """	MOEILIJKHEDEN INVOER
		VERNEDEREN
		AMUMA AMAMA MUMMUM
		AMATRAMA AAAA
		ABATRABAR
		DUMMY
		WORDS
	"""

wordlist = string.split(input)
    
for word in wordlist:
    word = string.strip(word)
    count_palinwords(word)
