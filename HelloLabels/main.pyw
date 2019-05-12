"""
AUTHOR      : Robert James Patterson
DATE        : 05/12/19
SYNOPSIS    : Work thru files for the Tkinter Tutorial at www.python-coures.edu
"""
from tkinter import Tk, Label, BOTH

root = Tk()

lblHello = Label(root, 
                 bg='black', 
                 fg='light pink',
                 font=('Helvetica', 40),
                 text="Howdy, Bitches!!"
                 )
lblHello.pack(fill=BOTH)


if __name__ == "__main__":
    
    root.mainloop()