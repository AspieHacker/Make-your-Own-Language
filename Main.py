from tkinter import *
import tkMessageBox
import tkSimpleDialog


class Window:
    def __init__(self, master):
        self.windowFrame = __init__.Frame(master, width="500", height="600")
        
        def Button(self, master):
            self.submitButton = button.Submit(master, bg="",)
        
        
        
        #textField1 = Layout(master, text="Username:  ")
        #textField2 = Layout(master, text="Password:  ")
        #input1 = Entry(master)
        #input2 = Entry(master)
        
        #textField1.grid(row=0, sticky="E")
        #textField2.grid(row=1, sticky="E")
        #input1.grid(row=0, colunm=1)
        #input2.grid(row=1, colunm=1)

app = Tk()
Window1 = Window(app)
app.mainLoop()