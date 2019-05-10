"""
AUTHOR      : Robert James Patterson
DATE        : 05/09/19
SYNOPSIS    : Work thru files for the 'Read The Docs' GUI programming with tkinter
"""
from tkinter import Tk, Label, Button, StringVar


class MyFirstGUI:
    
    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We've made it more interesting . . . ",
        ". . . by making the label interactive.",
        "Go ahead, click on me again."]

    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])

        self.lblTitleBar = Label(master,
                                 bg = 'maroon',
                                 fg = 'white',
                                 font = ('Helvetica', 18),
                                 text = "This is the Python GUI called Tkinter!"
                                 )
        self.lblTitleBar.pack(fill='x')

        self.lblMessage = Label(master,
                                bg = 'maroon',
                                fg = 'white',
                                font = ('Arial', 13),
                                textvariable = self.label_text
                                )
        self.lblMessage.bind('<Button-1>', self.cycle_label_text)
        self.lblMessage.pack(fill='x')

        self.btnGreet = Button(master,
                               bg = 'black',
                               fg = 'white',
                               font = ('Times', 12),
                               text = "Greet",
                               command = self.greet
                               )
        self.btnGreet.pack(fill='x')

        self.btnClose = Button(master,
                               bg = 'black',
                               fg = 'white',
                               font = ('Times', 12),
                               text = "Close",
                               command = master.quit
                               )
        self.btnClose.pack(fill='x')


    def greet(self):

        self.lblTitleBar.config(text = "Howdy, Bitches!! Welcome to the Mothership!")

    def cycle_label_text(self, event):
        
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])


root = Tk()
win = MyFirstGUI(root)
root.mainloop()
