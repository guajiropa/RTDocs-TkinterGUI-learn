"""
AUTHOR      : Robert James Patterson
DATE        : 05/12/19
SYNOPSIS    : Work thru files for the Tkinter Tutorial at www.python-coures.edu
"""
from tkinter import Tk, Toplevel, Label, BOTH

class dlgManyFonts:

    def __init__(self, master):
        self.master = master
     
        master.title("Many colors, many fonts!")

        self.lblRed = Label(master,
                            bg = 'dark red',
                            fg = 'red',
                            font = ('Times 22 bold'),
                            text = "Red text in times bold"
                            ).pack(fill = BOTH)
        
        self.lblBlue = Label(master,
                             bg = 'dark blue',
                             fg = 'light blue',
                             font = ('Helvetica 32'),
                             text = "Blue text in Helvetica"
                             ).pack(fill = BOTH)

        self.lblGreen = Label(master,
                              bg = 'dark green',
                              fg = 'light green',
                              font = ('Verdana 18 italic'),
                              text = "Blue text in Verdana italic"
                              ).pack(fill=BOTH) 


if __name__ == "__main__":
    root = Tk()
    win = dlgManyFonts(root)
    root.mainloop()
