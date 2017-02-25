from tkinter import *
import tkMessageBox
import tkSimpleDialog


class Window:
    
    def __init__(self, master):
        windowFrame = Frame(master, width="500", height="600")
        windowFrame.pack()
        
        self.profileButton = Button(windowFrame, text="Profiles")
        self.makerButton = Button(windowFrame, text='Maker')
        self.optionButton = Button(windowFrame, text='Options')
        self.plannerButton = Button(windowFrame, text='Planner') 
        
        
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