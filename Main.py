import tkinter as tk
from tkinter import ttk

LARGE_FONT=("Calibri",12)

class LanguageMakerApp(tk.Tk):
    
    def __init__(self, master):
                
        main = tk.Frame(master) 
        main.pack(side="top",fill="both",expand=True)
        main.grid_rowconfigure(0,weight=1)
        main.grid_columnconfigure(0,weight=1)

        bottom = tk.Frame(master)
        bottom.pack(fill='both',expand=True)
        bottom.grid_rowconfigure(0,weight=1)
        bottom.grid_columnconfigure(0,weight=1)
        
        self.frames = {}
        self.bottomframes = {}
        
        for F in (HomePage,MakerPage,ProfilePage,PlannerPage):
            frame = F(main,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
            
        for G in (BotMakerPage,BotHomePage,BotProfilePage,BotPlannerPage):
            botframe = G(bottom,self)
            self.bottomframes[G] = botframe
            botframe.grid(row=0,column=0,sticky="nsew")
            
        self.show_frame(HomePage,BotHomePage)
        
    def show_frame(self,mainframe,bottomframe):
        frame = self.frames[mainframe]
        botframe = self.bottomframes[bottomframe]
        frame.tkraise()
        botframe.tkraise()

class HomePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text="Home Page",font=LARGE_FONT)
        label.grid(row=0,column=0,sticky='ns')       
            
        profilebutton = ttk.Button(self,text="Profile",
            command=lambda: controller.show_frame(ProfilePage,BotProfilePage))
        profilebutton.grid(row=1,column=0)
        
        makerbutton = ttk.Button(self,text="Maker",
           command=lambda: controller.show_frame(MakerPage,BotMakerPage))
        makerbutton.grid(row=2,column=0)
        
        plannerbutton = ttk.Button(self,text="Planner",
            command=lambda: controller.show_frame(PlannerPage,BotPlannerPage))
        plannerbutton.grid(row=3,column=0)
        
class MakerPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text='Maker Page',font=LARGE_FONT)
        label.grid(row=0,column=1,sticky='nsew')

class ProfilePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text='Profiles',font=LARGE_FONT)
        label.grid(row=0,column=1,sticky='nsew')
       
class PlannerPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text='Planner',font=LARGE_FONT)
        label.grid(row=0,column=1,sticky='nsew')

class BotHomePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

class BotProfilePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        homeButton = ttk.Button(self,text="Home",
                command=lambda:controller.show_frame(HomePage,BotHomePage))
        homeButton.grid(row=0,column=0,sticky='se')

class BotMakerPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        homeButton = ttk.Button(self,text="Home",
                command=lambda:controller.show_frame(HomePage,BotHomePage))
        homeButton.grid(row=0,column=0,sticky='se')

class BotPlannerPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        homeButton = ttk.Button(self,text="Home",
                command=lambda:controller.show_frame(HomePage,BotHomePage))
        homeButton.grid(row=0,column=0,sticky='se')
    
app = tk.Tk()
LanguageMakerApp = LanguageMakerApp(app)
app.mainloop()
