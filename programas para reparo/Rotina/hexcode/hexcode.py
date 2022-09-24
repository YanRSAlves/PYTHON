#!/usr/bin/env python
##############################################
# for each number entered writes "\x<number>"
# to outfile (prompts for it) in append mode 
# breaks line after x entries
# march 2001 by joewoe 
# mailto:<lumbricus@gmx.net>
# TODO: Error checking
#       command line parameters
#       other styles "\x<number>\x<number>..."
##############################################
import os.path
import string
import sys

SCREENWIDTH=80

__doc__='''
hexcode.py:
2001 by joewoe
eases writing of "\x<number>", style codes
end input with single .
have fun :-)
'''
print __doc__
  
line_length=int(raw_input("how many entries per line?\n> "))
file_name=raw_input("which file?\n> ")
line_count=0

file=open(os.path.abspath(file_name),'a+')

while 1:
    line=[]
    for item in range(line_length):
	num=raw_input("> ")
	hexcode='"\x'+num+'",'
	if num == ".":
	    # end of input: cleaning up
	    file.write(string.join(line))
	    file.close()
	    print SCREENWIDTH*"_"
	    print "File written.\npraps it needs some editing ;-)\nTschö Jö!!!"
	    print SCREENWIDTH*"~"
	    sys.exit(0)
	else:
	    line.append(hexcode)
    
    line_count=line_count+1
    line.append("\n")
    file.write(string.join(line))
    print SCREENWIDTH*"_"
    print line_count,"lines written"  # added this because I always mixed up 
    print SCREENWIDTH*"~"             # the lines while typing
