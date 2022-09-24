#! /usr/bin/python
import sys
#TO BE DONE -editing of existing files!
#last revised 30/12/2000
print """     Welcome to Braindead!
  Web Page Creation for Idiots
     by Johnno, Nov. 2000"""
print ""
print ""
print """This is a script to help create simple web pages. It can help make a
basic page with text, background, images, tables, links and so on, but cannot
do any fancy stuff like forms, frames, java or javascript etc."""
print ""
print ""
print """A web page is simply an object composed of one or more elements
such as headings, paragraphs, images etc. Choose the desired item from the
menus and follow the prompts. Add the items in the same order as they will be
read,ie; from left to right and top to bottom."""
print ""
print """Your finished page will be saved as a html file, so before we start
we'd better give it a name. Remember to use the .html suffix."""
print ""
htmfile=raw_input("What is the filename? ")
print ""
print "#############################################################################"
print ""
print """OK, the first thing we need is a title for your page. This is what is
shown on top of the browser window as well as the history and bookmarks list."""
print ""
doctitle=raw_input("What is the title? ")
print ""
print "#############################################################################"
print ""
colours="""At the prompt type the colour number from the list below.

Black--------1
White--------2
Light Blue---3
Dark Blue----4
Light Green--5
Dark Green---6
Yellow-------7
Mauve--------8
Red----------9
Pink--------10
Orange------11
Brown-------12
Grey--------13
Maroon------14"""
print """Now we need to decide on a background for the page. The options here are:

NONE: just shows the background colour as set in the browser
(usually white or grey)

COLOUR: A single colour (that you specify) as the background.

IMAGE: An image file (usually a .gif), could be a picture or a textured colour
or pattern.
"""
print """At the prompt hit 'n' for none, 'c' for a colour, or 'i' for an image,
then hit <enter>"""
docbgd=raw_input("Background type= ")
print ""
if docbgd=="c":
	print colours
	print ""
	docbgcol=raw_input("Colour number= ")
else:
	if docbgd=="i":
		docbgdimg=raw_input("Type in the image filename and hit <enter> ")
	else:
		if docbgd=="n":
			pass

print "#############################################################################"
print ""						
print """Now we need the text colour. Use something that will contrast from
the background."""
print colours
print ""
doctxtcol=raw_input("Colour number= ")
colorcode={"1":"000000","2":"ffffff","3":"99ccff","4":"3366cc","5":"33ffcc","6":"006600","7":"ffff99","8":"9999ff","9":"ff3333","10":"ffcccc","11":"ff6633","12":"996666","13":"cccccc","14":"990033"}			
print ""
print ""
nl="\n"
f=open(htmfile,'w')
f.write("<HTML>")
f.write(nl)
f.write("<HEAD>")
f.write(nl)
f.write("<TITLE>")
f.write(doctitle)
f.write("</TITLE>")
f.write(nl)
f.write("</HEAD>")
f.write(nl)
if docbgd=="c":
	f.write('<BODY BGCOLOR="#')
	f.write(colorcode[docbgcol])
	f.write('">')
else:
	if docbgd=="i":
		f.write("<BODY BACKGROUND=")
		f.write(docbgdimg)
		f.write(">")
			
f.write(nl)
f.write('<BODY TEXT="#')
f.write(colorcode[doctxtcol])
f.write('">')
f.write(nl)	
f.write("<BODY>")
themenu="""Select an item to add to your page from the list below, then type
it's code at the prompt.

Heading-----------h
Paragraph---------p     (can contain links, images, blockquotes, bold or
                         italic text, linebreaks)
Image-------------i     (typically a .gif or .jpg)
Bullet List-------bl
Table-------------t
Horiz.Ruled Line--hr    (nice for separating sections)
End of page-------q     (all done!)

"""
while __name__=="__main__":
      print ""
      print "#############################################################################"
      print themenu
      nextitem=raw_input("Item Code= ")
      if nextitem=="h":
      	        print """Choose a heading size. The sizes run from 1 to 6, with 1 being the largest."""
        	hedsize=raw_input("Heading Size Number= ")
        	print""
        	print """Specify how the heading will be positioned - left, right or centred."""
        	hedposn=raw_input("Heading position - (l/r/c)= ")
        	print""
        	difhedcol=raw_input("Use a different colour for the heading? (y/n) ")
        	if difhedcol=="y":
        	    print colours
        	    hedcolour=raw_input("Colour number=  ")
        	if hedposn=="l":
        	    hedalign=" ALIGN=LEFT>"
        	else:
        	    if hedposn=="r":
        	        hedalign=" ALIGN=RIGHT>"
        	    else:
        	        if hedposn=="c":
        	            hedalign=" ALIGN=CENTER>"
        	
        	f.write("<H")
	        f.write(hedsize)
	        f.write(hedalign)
	        if difhedcol=="y":
	            f.write('<FONT COLOR="#')
	            f.write(colorcode[hedcolour])
	            f.write('">')
	        print""
        	hedcontent=raw_input("Now type the heading..")
	        f.write(hedcontent)
	        if difhedcol=="y":
	            f.write("</FONT>")
	        f.write("</H")
	        f.write(hedsize)
	        f.write(">")
                f.write(nl)
                print "Heading completed."
      else:
	      if nextitem=="p":
	          print """Type the text of the paragraph at the prompt.Word wrap will be done by
the browser, so you can just put everything on to one line. When you want to
end the paragraph, or insert an object (such as a link, an image, bold or
italic text etc.) press <enter>."""
	          f.write("<P>")
	          while __name__=="__main__":
	          	paratext=raw_input("enter text= ")
	          	f.write(paratext)
	          	insertinp=raw_input("Enter <i> to insert an item, or <e> to end the paragraph.(i/e) ")
	          	if insertinp=="i":
		      		print """Choose an item from the list below:
Link--l
Image--i
Italics--it
Bold--b
Line Break--lb
Block Quote--bq"""
		      		menuitem=raw_input("Enter the code of the item to insert-  ")		
		      		if menuitem=="bq":
		          		f.write("<BLOCKQUOTE>")
		          		bqtext=raw_input("Type in the block quote  ")
		          		f.write(bqtext)
		          		f.write("</BLOCKQUOTE>")
		          		contp=raw_input("Continue paragraph (y/n)? ")
			  		if contp=="y":
			  			continue
			  		else:
			  		   if contp=="n":
			  		     break
		      		if menuitem=="lb":
		          		f.write("<BR>")
		          		continue
			  	if menuitem=="b":
			  		f.write("<B>")
			  		boldbit=raw_input("Type in the text to be shown in bold ")
			  		f.write(" ")
			  		f.write(boldbit)
			  		f.write(" ")
			  		f.write("</B>")
			  		contp=raw_input("Continue paragraph (y/n)? ")
			  		if contp=="y":
			  			continue
			  		else:
			  		   if contp=="n":
			  		     break
		      		if menuitem=="it":
			  		f.write("<I>")
			  		italicbit=raw_input("Type in the text to be shown in italics ")
			  		f.write(" ")
			  		f.write(italicbit)
			  		f.write(" ")
			  		f.write("</I>")
			  		contp=raw_input("Continue paragraph (y/n)? ")
			  		if contp=="y":
			  			continue
			  		else:
			  		   if contp=="n":
			  		     break	
			  	if menuitem=="i":
		          		imgurl=raw_input("Enter the filename of the image..")
	                  		print """At the prompt, enter a text label for the image. This will only be visible
on text only browsers, or if for any reason the image can't be displayed."""
                          		imglabel=raw_input("Label for image= ")
                          		f.write('<IMG SRC="')
                          		f.write(imgurl)
                          		f.write('" ALT="')
                          		f.write(imglabel)
                          		f.write('">')
                          		contp=raw_input("Continue paragraph (y/n)? ")
			  		if contp=="y":
			  			continue
			  		else:
			  		   if contp=="n":
			  		     break
                      		if menuitem=="l":
                	  		lnkurl=raw_input("Enter the URL the link will point to ")          	
			  		paralink=raw_input("Highlighted link text= ")
                          		f.write('<A HREF="')
                          		f.write(lnkurl)
                          		f.write('">')
                          		f.write(" ")
                          		f.write(paralink)
                          		f.write(" ")
                          		f.write("</A>")
                          		contp=raw_input("Continue paragraph (y/n)? ")
			  		if contp=="y":
			  			continue
			  		else:
			  		   if contp=="n":
			  		     break
                      	else:
                      	        if insertinp=="e":
                	            f.write("</P>")
                	  	    f.write(nl)
                	  	    print "Paragraph completed.."        	                    	
		          	    break

	      else:
	            if nextitem=="i":
	                  imgurl=raw_input("Enter the filename of the image..")
	                  print """At the prompt, enter a text label for the image. This will only be visible
on text only browsers, or if for any reason the image can't be displayed."""
                          imglabel=raw_input("Label for image= ")
                          print """Do you want to centre the image on the page (the default location is
to the left)?"""
                          imgposn=raw_input("Centre the image (y/n)?")
                          if imgposn=="y":
                              f.write("<CENTER>")
                          f.write('<IMG SRC="')
                          f.write(imgurl)
                          f.write('" ALT="')
                          f.write(imglabel)
                          f.write('">')
                          if imgposn=="y":
                              f.write("</center>")
                          f.write(nl)
                          print "Image done.."
                    else:
                          if nextitem=="hr":
                                f.write("<HR>")
                                f.write(nl)
                                print "Horizontal line drawn.."
                          else:
                                if nextitem=="bl":
                                      print """Enter the list items at the prompt, bullets will be added automatically."""
                                      listmem=raw_input("Enter the first line of the list.")
                                      f.write("<UL>")
                                      f.write(nl)
                                      f.write("<LI>")
                                      f.write(listmem)
                                      morlines=raw_input("Add another line? (y/n) ")
                                      if morlines=="n":
                                            f.write("</UL>")
                                            f.write(nl)
                                      else:
                                            while morlines=="y":
                                                  listmem=raw_input("Enter next line..")
                                                  f.write(nl)
                                                  f.write("<LI>")
                                                  f.write(listmem)
                                                  morlines=raw_input("Add another line? (y/n) ")
                                                  if morlines=="n":
                                                        f.write(nl)
                                                        f.write("</UL>")
                                                        f.write(nl)
                                                        print "List done.."
                                else:
                                      if nextitem=="t":
                                          firstiteration="YES"
                                          tableposi=raw_input("Put the table on the left, right or centre? (l,r,c) ")
                                          if tableposi=="l":
                                      	      tableposi="LEFT"
                                          else:
                                      	      if tableposi=="r":
                                      		  tableposi="RIGHT"
                                      	      else:
                                      		  if tableposi=="c":
                                      			tableposi="CENTER"
                                          f.write("<TABLE ALIGN=")
                                          f.write(tableposi)
                                          useborder=raw_input("Use a border? (y/n) ")
                                          if useborder=="y":
                                              f.write(" BORDER")
                                          print ""
                                          tabbg=raw_input("Choose a table background--coloured or transparent (c/t).. ")
                                          if tabbg=="c":
                                              print colours
                                              print ""
                                              tabcol=raw_input("Colour number= ")
                                          print ""
                                          print """You can set the width of the table as a percentage of the page width,
or you can just leave this up to the browser. Setting the width manually
will give more predictable results."""
                                          setwidth=raw_input("Set table width? (y/n) ")
                                          if setwidth=="y":
                                              print"Type in the table width--don't use a percentage sign, just the number."
                                              tabwidth=raw_input("Percentage of page width-- ")
                                              f.write(" WIDTH=")
                                              f.write(tabwidth)
                                              f.write("%")
                                          if tabbg=="c":
                                              f.write(' BGCOLOR="')
                                              f.write(colorcode[tabcol])
                                              f.write('" ')			
                                          f.write(">")
                                          f.write(nl)
                                          tablecaption=raw_input("Use a caption for the table? (y/n) ")
                                          if tablecaption=="y":
                                      	      capalign=raw_input("Put caption at (t)op or (b)ottom? (t/b) ")
                                      	      if capalign=="t":
                                      		  capalign="TOP"
                                      	      else:
                                      		  if capalign=="b":
                                      		      capalign="BOTTOM" 	
                                      	      f.write("<CAPTION ALIGN=")
                                      	      f.write(capalign)
                                      	      f.write(">")
                                      	      caption=raw_input("Type in the caption..")
                                      	      f.write(caption)
                                      	      f.write("</CAPTION>")
                                      	  f.write(nl)
                                          print " "
                                          f.write("<TR>")
                                          print "Choose an item to put into the first table cell"
                                          cellmenu="""Heading-------1
Plain text---2
Bold text----3
Italic text--4
Link---------5
Image--------6"""
                                          while __name__=="__main__":
                                              print (cellmenu)
                                              cellitem=raw_input("Enter the item number...")
                                              if firstiteration=="YES":
                                                  if cellitem!="1":
                                                      f.write("<TD>")
                                              if cellitem=="1":
                                          	  f.write("<TH ")
                                          	  colspan=raw_input("How many columns should the heading span?  ")
                                          	  f.write("COLSPAN=")
                                          	  f.write(colspan)
                                          	  f.write(">")
                                          	  cellheding=raw_input("Type in the heading...")
                                          	  f.write(cellheding)
                                          	  f.write("</TH>")
                                              else:
                                                  if cellitem=="2":
                                          	      celtext=raw_input("Type in the cell text...")
                                          	      f.write(celtext)
                                          	  else:
                                          	      if cellitem=="3":
                                          		  f.write("<B>")
                                          		  boldcell=raw_input("Type in the bold cell text...")
                                          		  f.write(boldcell)
                                          		  f.write("</B>")
                                          	      else:
                                          		  if cellitem=="4":
                                          		      f.write("<I>")
                                          		      italcell=raw_input("Type in the italic cell text...")
                                          		      f.write(italcell)
                                          		      f.write("</I>")
                                          		  else:
                                          		      if cellitem=="5":
                                          			  firsttext=raw_input("Type in any text that will precede the link...")
                                          			  f.write(firsttext)
                                          			  cellink=raw_input("Type the highlighted link text= ")
                                        			  lnkurl=raw_input("Enter the URL the link will point to ")
                                                                  f.write('<A HREF="')
                                                                  f.write(lnkurl)
                                                                  f.write('">')
                                                                  f.write(" ")
                                                                  f.write(cellink)
                                                                  f.write(" ")
                                                                  f.write("</A>")
                                                                  aftertext=raw_input("Type in any text that follows the link...")
                                                                  f.write(aftertext)
                                          		      else:
                                          			  if cellitem=="6":
                                          			      imgurl=raw_input("Enter the filename of the image..")
	                                                              print """At the prompt, enter a text label for the image. This will only be visible
on text only browsers, or if for any reason the image can't be displayed."""
                                                                      imglabel=raw_input("Label for image= ")
                                                                      f.write('<IMG SRC="')
                                                                      f.write(imgurl)
                                                                      f.write('" ALT="')
                                                                      f.write(imglabel)
                                                                      f.write('">')
                                              firstiteration="NO"
                                              print""
                                              print "Choose from the menu below"
                                              if cellitem!="1":
                                                  print "Insert another item into the current cell--1"
                                              print """Go to next cell in current row-------------2
Start a new row----------------------------3
Table completed----------------------------4"""
                          	    	      cellchoice=raw_input("Type in the number...")
                          	    	      if cellchoice=="1":
                          	    	          f.write(" ")
                          	    	  	  continue
                          	    	      else:
                          	    	  	  if cellchoice=="2":
                          	    	  	      if cellitem!="1":
                          	    	  	          f.write("</TD>")
                          	    	  	      f.write(nl)
                          	    	  	      f.write("<TD>")
                          	    	  	      print""
                          	    	  	      print "Choose an item for the next cell..."
                          	    	  	      continue
                          	    	  	  else:
                          	    	  	      if cellchoice=="3":
                          	    	  	          if cellitem!="1":
                          	    	  	              f.write("</TD>")
                          	    	  		  f.write("</TR>")
                          	    	  		  f.write(nl)
                          	    	  		  f.write("<TR><TD>")
                          	    	  		  print""
                          	    	  		  print "Choose an item for the first cell in the new row..."
                          	    	  		  continue
                          	    	  	      else:
                          	    	  		  if cellchoice=="4":
                          	    	  		      if cellitem!="1":
                          	    	  		          f.write("</TD>")
                          	    	  		      f.write("</TR>")
                          	    	  		      f.write(nl)
                          	    	  		      f.write("</TABLE>")
                          	    	  		      print "Table completed.."
                          	    	  		      break        				
                                      else:
                                              if nextitem=="q":
                                                    mailok=raw_input("Would you like to link to your email address at the bottom of the page (y/n)")
                                                    if mailok=="y":
                                                    	emailadd=raw_input("Enter your email address ")
                                                    	emailink=raw_input("Enter any text preceding your address ")
                                                    	f.write("<P>")
                                                    	f.write(emailink)
                                                    	f.write(" ")
                                   		        f.write('<A HREF="')
                                   		        f.write("mailto:")
                                   		        f.write(emailadd)
                                   		        f.write('">')
                                   		        f.write(emailadd)
                                   		        f.write(" ")
                                   		        f.write("</A>")
                                   		        f.write("</P>")
                                   		    f.write("</BODY>")
                                                    f.write(nl)
                                                    f.write("</HTML>")
                                                    f.close()
                                                    print "Page done..."
                                                    sys.exit()                               	                  			            				        										