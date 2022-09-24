#!/usr/bin/env python
# findsimplesubs.py -- accepts ordered pattern
# word substitutions, returns matching words
# from wordlist file.  Rapidly toasts simple 
# substitution ciphers with word divisions.
#
# Examples:
# findsimplesubs.py ABCDEEFCD 
# returns: satellite
# findsimplesubs.py ABACDEA
# returns: Alameda Edenize elevate execute sisters systems
# findsimplesubs.py ABCDDCEA
# returns: grilling gripping spellers

import sys
dict = open('/usr/dict/words')
pattern = sys.argv[1]
pattern = pattern.upper()
word = dict.readline()
word = word[:-1]
while word:
     if len(word) != len(pattern):
          pass
     else: 
         tempdict = {}
         subword = ""      
         alph = list('ZYXWVUTSRQPONMLKJIHGFEDCBA')
         for letter in word:
             if letter.upper() not in tempdict.keys():
                 moretempdict = {letter.upper(): alph.pop()}
                 tempdict.update(moretempdict)
             else:pass
         for letter in word:
              subword = subword + tempdict[letter.upper()]
         if subword == pattern:
              print word,
     word = dict.readline()
     word = word[:-1]
dict.close()



