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
        
        homeFrame = HomePage(main,self)
        self.frames[HomePage] = homeFrame
        homeFrame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(HomePage)
        
        #makerFrame = MakerPage(main,self)
        #self.frames[MakerPage] = makerFrame
        #makerFrame.grid(row=0,column=1,sticky="nsew")
        #self.show_frame(MakerPage)
    
        
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
        
        
        #self.makerButton = Button(LanguageMakerApp.__init__.homeFrame,text="Maker",
           # command=hide_show_frame(self,homePage,makerPage))
        
        
#class MakerPage(Frame):
#    def __init__(self,parent,controller):
#        Frame.__init__(self,parent)
  #      label = Label(self,text='Maker Page',font=LARGE_FONT)
   #     label.pack(padx=10,pady=10)
       
        #self.newButton = Button(LanguageMakerApp.frames[makerPage],text="new")
        
app = Tk()
LanguageMakerApp = LanguageMakerApp(app)
app.mainloop()