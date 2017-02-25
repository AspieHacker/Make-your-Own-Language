import tkinter as tk
from tkinter import ttk

LARGE_FONT=("Calibri",12)

class LanguageMakerApp(tk.Tk):
    
    def __init__(self, master):
                
        main = tk.Frame(master) 
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
            
        
class HomePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text="Home Page",font=LARGE_FONT)
        label.grid(row=0,column=1,sticky='nsew')       
            
        button3 = ttk.Button(self,text="Profiles",
            command=lambda: controller.show_frame(ProfilePage))
        button3.grid(row=1,column=0)
        
        button1 = ttk.Button(self,text="Maker",
           command=lambda: controller.show_frame(MakerPage))
        button1.grid(row=2,column=0)
        
        button2 = ttk.Button(self,text="Planner",
            command=lambda: controller.show_frame(PlannerPage))
        button2.grid(row=3,column=0)
        
class MakerPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text='Maker Page',font=LARGE_FONT)
        label.grid(row=0,column=1,sticky='nsew')
       
        homeButton = ttk.Button(self,text="Home",
            command=lambda:controller.show_frame(HomePage))
        homeButton.grid(row=10,column=10,sticky='se')

class ProfilePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text='Profiles',font=LARGE_FONT)
        label.grid(row=0,column=1,sticky='nsew')
       
        homeButton = ttk.Button(self,text="Home",
            command=lambda:controller.show_frame(HomePage))
        homeButton.grid(row=10,column=10,sticky='se')

class PlannerPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text='Planner',font=LARGE_FONT)
        label.grid(row=0,column=1,sticky='nsew')
       
        homeButton = ttk.Button(self,text="Home",
            command=lambda:controller.show_frame(HomePage))
        homeButton.grid(row=10,column=10,sticky='se')
app = tk.Tk()
LanguageMakerApp = LanguageMakerApp(app)
app.mainloop()
