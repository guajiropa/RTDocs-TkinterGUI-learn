"""
AUTHOR      : Robert James Patterson
DATE        : 05/09/19
SYNOPSIS    : Work thru files for the 'Read The Docs' GUI programming with tkinter
"""
from tkinter import Tk, Label, Button

class MyFirstGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.lblTitle = Label(master, text="This is my first OOP Tk GUI")
        self.lblTitle.pack()

        self.btnGreet = Button(master, text='Greet', command=self.greet)
        self.btnGreet.pack()

        self.btnClose = Button(master, text='Close', command=master.quit)
        self.btnClose.pack()

    def greet(self):
        
        self.lblTitle.config(text="Welcome, Bitches!!")


root = Tk()
win = MyFirstGUI(root)
root.mainloop()
