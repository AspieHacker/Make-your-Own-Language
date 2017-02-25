from tkinter import *
import tkMessageBox
import tkSimpleDialog


class Window:
    def __init__(self, master): 
        def WindowFrame(self, master):
            self.profile = Frame(master)
            profile.grid()
        
        def WindowFrame(self, master):
            self.maker = Frame(master)
            maker.grid()
        
        def WindowFrame(self, master):
            self.options= Frame(master)
            options.grid()
        
        def WindowFrame(self, master):
            self.planner = Frame(master)
            planner.grid()
                    
            
                 
            def Profile(self, bg="", text="", command=""):
                self.profile = button(Red, "Profile", List1)
            def Options(self, bg="", text="", command=""):
                self.options = button(Blue, "Options", List2)
            def Planner(self, bg="", text="", command=""):
                self.planner = button(Green, "Planner", List3)
            def Maker(self, bg="", text="", command=""):
                self.Maker = button(Yellow, "Language Maker", List4)       
            
            def Button(self, master):
                self.button = button(master, bg="", text="", command="")
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