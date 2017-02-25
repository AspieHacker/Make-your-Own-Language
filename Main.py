from Tkinter import *

LARGE_FONT=("Calibri",12)


self.frames = {}

class LanguageMakerApp:
    
    def __init__(self, master):
                
        main = Frame(master) 
        main.pack(side="top",fill="both",expand=True)
        
        main.grid_rowconfigure(0,weight=1)
        main.grid_columnconfigure(0,weight=1)
        
        self.frames = {}
        
        homeFrame = HomePage(main,self)
        self.frames[HomePage] = homeFrame
        homeFrame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(HomePage)
        
        makerFrame = MakerPage(main,self)
        self.frames[MakerPage] = makerFrame
        makerFrame.grid(row=0,column=1,sticky="nsew")
        self.show_frame(MakerPage)
    
    def frame_container(frame):
        self.frame_container = {}
        self.frame[frame] = frame
        print self.frame_container
        
    def show_frame(self,main):
            frame = self.frames[main]
            frame.tkraise()
            
    def hide_frame(self,main):
        frame = self.frames[main]
        frame.tkhide()
    def hide_show_frame(self,hide,show):
        hideFrame = self.frames[hide]
        showFrame = self.frames[show]
        hideFrame.tkhide()
        showFrame.tkraise()
        
class HomePage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text="Home Page",font=LARGE_FONT)
        label.pack(padx=10, pady=10)
        
        
        self.makerButton = Button(LanguageMakerApp.__init__.homeFrame,text="Maker",
            command=hide_show_frame(self,homePage,makerPage))
        
        
class MakerPage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text='Maker Page',font=LARGE_FONT)
        label.pack(padx=10,pady=10)
        
        self.newButton = Button(LanguageMakerApp.frames[makerPage],text="new")
        
        
        
        #windowFrame = Frame(master, width="500", height="600")
        #windowFrame.pack()
        
        #self.profileButton = Button(windowFrame, text="Profiles")
        #self.makerButton = Button(windowFrame, text='Maker')
        #self.optionButton = Button(windowFrame, text='Options')
        #self.plannerButton = Button(windowFrame, text='Planner') 
        
        
        #textField1 = Layout(master, text="Username:  ")
        #textField2 = Layout(master, text="Password:  ")
        #input1 = Entry(master)
        #input2 = Entry(master)
        
        #textField1.grid(row=0, sticky="E")
        #textField2.grid(row=1, sticky="E")
        #input1.grid(row=0, colunm=1)
        #input2.grid(row=1, colunm=1)
app = Tk()
LanguageMakerApp = LanguageMakerApp(app)
app.mainloop()