"""
AUTHOR      : Robert James Patterson
DATE        : 05/12/19
SYNOPSIS    : Work thru files for the Tkinter Tutorial at www.python-coures.edu
"""
from tkinter import Tk, Label, BOTH

win = Tk()

lblHello = Label(win, 
                 bg='navy blue', 
                 fg='light pink',
                 font=('Helvetica', 20),
                 text="Howdy, Bitches!!"
                 )
lblHello.pack(fill=BOTH)


if __name__ == "__main__":
    
    win.mainloop()