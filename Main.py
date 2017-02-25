import tkinter as tk
from tkinter import ttk

LARGE_FONT=("Calibri",12)

class LanguageMakerApp(tk.Tk):
    
    def __init__(self, master):
                
        main = tk.Frame(master) 
        main.pack(side="top",fill="both",expand=True)
        main.grid_rowconfigure(0,weight=1)
        main.grid_columnconfigure(0,weight=1)

        menu = tk.Menu(master)
       
        
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
        label = tk.Label(self,text="Home Page",font=LARGE_FONT)
        label.pack(padx=10, pady=10)       
            
        button3 = ttk.Button(self,text="Profiles",
            command=lambda: controller.show_frame(ProfilePage))
        button3.pack(side='left')
        
        button1 = ttk.Button(self,text="Maker",
           command=lambda: controller.show_frame(MakerPage))
        button1.pack()
        
        button2 = ttk.Button(self,text="Planner",
            command=lambda: controller.show_frame(PlannerPage))
        button2.pack()
        
class MakerPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text='Maker Page',font=LARGE_FONT)
        label.pack(padx=10,pady=10)
       
        homeButton = tk.Button(self,text="Home",
            command=lambda:controller.show_frame(HomePage))
        homeButton.pack()

class ProfilePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text='Profiles',font=LARGE_FONT)
        label.pack(padx=10,pady=10)
       
        homeButton = tk.Button(self,text="Home",
            command=lambda:controller.show_frame(HomePage))
        homeButton.pack()

class PlannerPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text='Planner',font=LARGE_FONT)
        label.pack(padx=10,pady=10)
       
        homeButton = tk.Button(self,text="Home",
            command=lambda:controller.show_frame(HomePage))
        homeButton.pack()

app.config(menu=menu)
LanguageMakerApp = LanguageMakerApp(app)
app = tk.Tk()
app.mainloop()
