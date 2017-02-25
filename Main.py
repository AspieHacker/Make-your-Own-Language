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
        
        for F in (startPage,PageOne,PageTwo):
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
        
        
        button1 = Button(self,text="Maker",
           command=lambda: controller.show_frame(MakerPage))
        
        
        
class MakerPage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text='Maker Page',font=LARGE_FONT)
        label.pack(padx=10,pady=10)
       
        #self.newButton = Button(LanguageMakerApp.frames[makerPage],text="new")
        
app = Tk()
LanguageMakerApp = LanguageMakerApp(app)
app.mainloop()