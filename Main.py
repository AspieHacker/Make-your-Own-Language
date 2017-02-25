from Tkinter import *

LARGE_FONT=("Calibri",12)


frames = {}

class LanguageMakerApp:
    
    def __init__(self, master):
                
        main = Frame(master) 
        main.pack(side="top",fill="both",expand=True)
        
        main.grid_rowconfigure(0,weight=1)
        main.grid_columnconfigure(0,weight=1)
        
        self.frames = {}
        
        for F in (HomePage,MakerPage,ProfilePage,PlannerPage):
            frame = F(main,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(HomePage)
        
    
    def show_frame(self,main):
        frame = self.frames[main]
        frame.tkraise()
            
        
class HomePage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text="Home Page",font=LARGE_FONT)
        label.pack(padx=10, pady=10)       
            
        button3 = Button(text="Profiles",
            command=lambda: controller.show_frame(ProfilePage))
        button3.pack()
        
        button1 = Button(text="Maker",
           command=lambda: controller.show_frame(MakerPage))
        button1.pack()
        
        button2 = Button(text="Planner",
            command=lambda: controller.show_frame(PlannerPage))
        button2.pack()
        
class MakerPage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text='Maker Page',font=LARGE_FONT)
        label.pack(padx=10,pady=10)
       
        homeButton = Button(self,text="Home",
            command=lambda:controller.show_frame(HomePage))
        homeButton.pack()

class ProfilePage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text='Profiles',font=LARGE_FONT)
        label.pack(padx=10,pady=10)
       
        homeButton = Button(self,text="Home",
            command=lambda:controller.show_frame(HomePage))
        homeButton.pack()

class PlannerPage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text='Planner',font=LARGE_FONT)
        label.pack(padx=10,pady=10)
       
        homeButton = Button(self,text="Home",
            command=lambda:controller.show_frame(HomePage))
        homeButton.pack()


app = Tk()
LanguageMakerApp = LanguageMakerApp(app)
app.mainloop()