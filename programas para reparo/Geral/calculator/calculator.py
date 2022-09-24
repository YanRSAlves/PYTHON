#Simple calculator app with a GUI front end, as per the "Python Challenge".
#Written in __exactly__ 1 hour.
#By Jesse Weinstein-jessw@loop.com
#Released on June 24, 2001, at 2:42 PM, Pacific Standard Time

from Tkinter import *

class Calculator:
    def __init__(self, font_size=12):
        self.font_size=font_size
        self.make_window()
    def make_window(self):
        self.root=Tk()
        self.root.title('Calculadora')
        self.opersF=Frame(self.root)
        self.opers=[]
        for item in ['+', '-', '*', '/']:
            self.opers.append(Button(self.opersF, text=item[0],\
                                     height=1, width=2,\
                                     font=('', `self.font_size`, '')))
            self.opers[-1].bind('<1>', self.buttonCB)
            self.opers[-1].pack(side=TOP)

        self.display=Entry(self.root, font=('', `self.font_size`, ''),\
                           state=DISABLED, width=2)
        
        self.numsF=Frame(self.root)
        self.nums=[]
        for item in range(1, 10):
            self.nums.append(Button(self.numsF, text=`item`,\
                                    height=1, width=2, \
                                    font=('', `self.font_size`, '')))
            self.nums[-1].bind('<1>', self.buttonCB)
            self.nums[-1].grid(column=(item-1) % 3, row=(item-1)/3)
        self.othersF=Frame(self.root)
        self.others=[]
        for item in [('=', self.equals), ('C', self.clear),\
                     ('d', self.backspace)]:
            self.others.append(Button(self.othersF, text=item[0],\
                                      command=item[1], height=1, width=2,
                                      font=('', `self.font_size`, '')))
            self.others[-1].pack(side=RIGHT)
            
        self.display.grid(column=0, row=0, columnspan=4, sticky=NW+E)
        self.opersF.grid(column=3, row=1, rowspan=2, sticky=W)
        self.numsF.grid(column=0, row=1, columnspan=3, sticky=SE)
        self.othersF.grid(column=2, row=2, sticky=NE)
    def buttonCB(self, event):
        val=event.widget.cget('text')
        self.display.config(state=NORMAL)
        self.display.insert(END, val)
        self.display.config(state=DISABLED)
    def equals(self):
        if self.display.get():
            ans=eval(self.display.get())
            self.display.config(state=NORMAL)
            self.display.delete(0, END)
            self.display.insert(0, ans)
            self.display.config(state=DISABLED)
    def clear(self):
        self.display.config(state=NORMAL)
        self.display.delete(0, END)
        self.display.config(state=DISABLED)
    def backspace(self):
        self.display.config(state=NORMAL)
        self.display.delete(len(self.display.get())-1)
        self.display.config(state=DISABLED)
        
if __name__=='__main__':
    it=Calculator()
    print """If you are seeing this message because nothing else has appeared
on your screen, then I suggest you run this from IDLE, or uncomment out the line
directly below this one, which starts a Tkinter mainloop.  (If you start a
mainloop in IDLE, it locks up.)"""
    #it.root.mainloop()
    #Note: the above should be uncommented if running outside of IDLE
