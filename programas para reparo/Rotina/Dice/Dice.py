# Dice.py
#
# A simple gui to simulate rolling a handfull of dice. Number of dice to roll and
# number of sides are the inputs. A list of each roll and their total are displayed.
#
# Really it's practice using Tkinter.
#
# NOTE: You'll need to have Pmw installed to run Dice.py.  Pmw can be downloaded from
#       http://pmw.sourceforge.net/
#
# Samuel Leming
# 02/12/2001
#
# 02/15/2001 - Added <Return> binding to both Roll & Done buttons.
#              Corrected URL for 0.8.5 release of Pmw.
#              Created app specific Button & Entry subclasses to remove repetitive code
#              from app init.
#              Removed obsolete IntEntry class.
#              Added increment and deincrement functionality to EntryField class.
#              Catching negative number exceptions in roll method.
#              Added SetDisplay method to DiceGui to pare down exception handling
#              in roll method.
#              Added ability to set default value for EntryField class.

import sys
from Tkinter import *
import Pmw
from DiceSet import *

class DiceButton(Button):
    """A standard button for this application."""
    
    def __init__(self, master, side = None, **parameters):
        """Just a constructor."""
        
        Button.__init__(self, master, parameters)
        self.bind('<Return>', parameters['command'])
        self.pack(side = side,
                  expand = NO,
                  padx = 3,
                  pady = 3)

class EntryField(Frame):
    """ """
    
    ARROWFONT = ("times", 4)

    def __init__(self, master,
                 labeltext =  None, labelfont = None, textfont = None, default = 6):
        """ """
        
        Frame.__init__(self, master)
        self.value = IntVar()
        self.value.set(default)
        Label(self,
              text = labeltext,
              font = labelfont,
              width = 7,).grid(row = 0, column = 0, sticky = W)
        self.downbutton = Button(self, text = '<',
                                 font = self.ARROWFONT,
                                 command = self.minus)
        self.downbutton.bind('<Return>', self.minus)
        self.downbutton.grid(row = 0, column = 1, padx = 1)
        self.valuefield = Entry(self,
                                font = textfont,
                                textvariable = self.value)
        self.valuefield.grid(row = 0, column = 2)
        self.upbutton = Button(self, text = '>',
                               font = self.ARROWFONT,
                               command = self.plus)
        self.upbutton.bind('<Return>', self.plus)
        self.upbutton.grid(row = 0, column = 3, padx = 1)
        self.pack(expand = YES,
                  fill = BOTH,
                  padx = 3,
                  pady = 1)

    def __int__(self):
        """ """
        
        return self.value.get()

    def __str__(self):
        """ """
        
        return self.valuefield.get()

    def plus(self, event = None):
        try:
            self.value.set(self.value.get() + 1)
        except ValueError:
            pass
    
    def minus(self, event = None):
        try:
            self.value.set(self.value.get() - 1)
        except ValueError:
            pass

class DiceGui(Tk):
    """Interface for rolling a handfull of dice. """

    LABELFONT = ("arial", 8, "bold")
    TEXTFONT = ("arial", 8)

    def __init__(self):
        """GUI constructor. """
        
        Tk.__init__(self)
        self.title("Digital Dice")
        self.NumDice = EntryField(self, "# Dice:", self.LABELFONT, self.TEXTFONT, 3)
        self.Sides = EntryField(self, "Sides:", self.LABELFONT, self.TEXTFONT, 6)
        ButtonRow = Frame(self,
                          relief = GROOVE,
                          borderwidth = 2)
        DiceButton(ButtonRow,
                   side = LEFT,
                   text = 'Roll',
                   font = self.LABELFONT,
                   command = self.roll,
                   underline = 0)
        DiceButton(ButtonRow,
                   side = RIGHT,
                   text = 'Done',
                   font = self.LABELFONT,
                   command = self.bail,
                   underline = 0)
        ButtonRow.pack(expand = YES,
                       fill = BOTH,
                       padx = 2,
                       pady = 1)
        self.Results = Pmw.ScrolledText(self,
                                        vscrollmode = 'static',
                                        labelpos = "nw",
                                        label_text = "Results:",
                                        label_font = self.LABELFONT,
                                        text_background = 'gray70',
                                        text_font = self.TEXTFONT,
                                        text_height = 6,
                                        text_width = 30,
                                        text_relief = 'sunken',
                                        text_state = 'disabled')
        self.Results.pack(expand = YES,
                          fill = BOTH,
                          padx = 3,
                          pady = 1)
        TotalRow = Frame(self)
        Label(TotalRow,
              text = 'Total:',
              font = self.LABELFONT).pack(side = LEFT)
        self.Total = Label(TotalRow,
                           relief = SUNKEN,
                           font = self.TEXTFONT)
        self.Total.pack(side = RIGHT,
                        expand = YES,
                        fill = BOTH)
        TotalRow.pack(expand = YES,
                      fill = BOTH,
                      padx = 3,
                      pady = 2)

        self.Dice = DiceSet()
        
    def roll(self, event = None):
        """Rolls dice with parameters set in NumDice and Sides. """
        
        try:
            self.SetDisplay(repr(self.Dice.roll(int(self.NumDice), int(self.Sides)))[1:-1],
                            self.Dice.Total)
        except NoSidesError:
            self.SetDisplay("Well, that's a new one!", "How can a die have no sides?")
        except OneSideError:
            self.SetDisplay("Oh come on!", "A die with one side is a sphere.")
        except NegSidesError:
            self.SetDisplay("Get real!", "A die can't have negative sides.")
        except NoDiceError:
            self.SetDisplay("Rolling zero dice.", "Why even bother?")
        except NegDiceError:
            self.SetDisplay("Rolling negative number of dice.", "Are they imaginary dice?")
        except ValueError:
            self.SetDisplay("Invalid data.", "Please try again.")

    def bail(self, event = None):
        """Exit program."""
        self.destroy()

    def SetDisplay(self, Result, Total):
        self.Results.settext(Result)
        self.Total.configure(text = Total)


def main():
    """Run the program. """
    
    # Process any command line arguments here.
    
    DiceGui().mainloop()
    return 0

# To do.
def test():
    """Test Code."""
    pass

if __name__ == '__main__':
    sys.exit(main())
