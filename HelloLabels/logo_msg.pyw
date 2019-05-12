"""
AUTHOR      : Robert James Patterson
DATE        : 05/12/19
SYNOPSIS    : Work thru files for the Tkinter Tutorial at www.python-coures.edu
"""
from tkinter import Tk, Label, PhotoImage, RIGHT, LEFT, CENTER

root = Tk()
logo = PhotoImage(file='python_logo_small.gif')

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface exists to
allow additional image file formats to be added."""

lblHello = Label(root, 
                 #justify=LEFT,
                 compound=CENTER,
                 padx=10,
                 font=('Helvetica', 16),
                 text=explanation,
                 image=logo
                 )
lblHello.pack(side=RIGHT)


if __name__ == "__main__":
    
    root.mainloop()