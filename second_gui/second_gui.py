"""
AUTHOR      : Robert James Patterson
DATE        : 05/09/19
SYNOPSIS    : Work thru files for the 'Read The Docs' GUI programming with tkinter
"""
from tkinter import Tk, Label, Button, StringVar


class MyFirstGUI:

    # This member variable (field) is our list of strings for the click event 
    # wired up to the lblMessage control.
    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We've made it more interesting . . . ",
        ". . . by making the label interactive.",
        "Go ahead, click on me again."
        ]

    # This is our 'Pythonic' constructor. 
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        # Set up the variables to handle rotating thru the list of strings.
        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])

        # Define our controls and place them on the form using 'pack'.
        self.lblTitleBar = Label(master,
                                 bg = 'maroon',
                                 fg = 'white',
                                 font = ('Helvetica', 18),
                                 text = "This is the Python GUI called Tkinter!"
                                 )
        self.lblTitleBar.pack(fill='x')

        # This is the label control that will respond to th click event.
        self.lblMessage = Label(master,
                                bg = 'maroon',
                                fg = 'white',
                                font = ('Arial', 13),
                                textvariable = self.label_text
                                )
        # This is the customer event handler for the label that handles the left
        # mouse button click when the pointer is over the control.
        self.lblMessage.bind('<Button-1>', self.cycle_label_text)
        self.lblMessage.pack(fill='x')

        # This is the button that will change the Title text when clicked.
        self.btnGreet = Button(master,
                               bg = 'black',
                               fg = 'white',
                               font = ('Times', 12),
                               text = "Greet",
                               command = self.greet
                               )
        self.btnGreet.pack(fill='x')

        # This is the button that will close the app
        self.btnClose = Button(master,
                               bg = 'black',
                               fg = 'white',
                               font = ('Times', 12),
                               text = "Close",
                               command = master.quit
                               )
        self.btnClose.pack(fill='x')

    # This is the method used to change the text in the Title label.
    def greet(self):

        self.lblTitleBar.config(text = "Howdy, Bitches!! Welcome to the Mothership!")
    
    # This is the method to handle cycling thru our list of strings to be displayed. 
    def cycle_label_text(self, event):
        
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        

# Run the app, pass in the Tk object to the constructor.
root = Tk()
win = MyFirstGUI(root)
root.mainloop()
