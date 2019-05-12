"""
AUTHOR      : Robert James Patterson
DATE        : 05/09/19
SYNOPSIS    : Work thru files for the 'Read The Docs' GUI programming with tkinter
"""
from tkinter import Tk
from gui import MyNewGUI

if __name__ == "__main__":
    
    # Run the app, pass in the Tk object to the constructor.
    root = Tk()
    win = MyNewGUI(root)
    root.mainloop()
