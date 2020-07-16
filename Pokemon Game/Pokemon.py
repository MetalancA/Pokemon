from playsound import playsound
from tkinter import *
from PIL import ImageTk, Image
import tkinter.filedialog
import os
import shutil


playsound('pokemonmusic.mp3', False)
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(1200, 500))
        self.master.title('POKEMON BATTLE GAME')
        

        self.varfromfiles = StringVar()
        self.vartofiles = StringVar()
        self.varfileext = StringVar()
        self.varfromdir = StringVar()
        self.varlistfield = StringVar()
        self.varmovefileext = StringVar()



        self.txtF2name = Entry(self.master,text=self.varmovefileext, font=("Times New Roman", 12),fg='black', bg='white', width=60)
        self.txtF2name.grid(row=1, column=1, columnspan=3, padx=(20,0), pady=(10,0))

        self.lbl_fname = Label(self.master,text='What is the name of your Pokemon?: ')
        self.lbl_fname.grid(row=1,column=0,padx=(27,0),pady=(10,0),sticky=N)


        self.btnCancel = Button(self.master, text="Close Program", width=15, height=2, command=lambda: ask_quit())
        self.btnCancel.grid(row=15, column=6, padx=(0,0), pady=(20,0), sticky=NE)



        self.btnCancel = Button(self.master, text="BATTLE GABE!", width=12, height=2, command=lambda: openGabe())
        self.btnCancel.grid(row=6, column=0, padx=(30,0), pady=(0,0), sticky=N)

        self.btnOpen = Button(self.master, text="BATTLE NICK!", width=12, height=2, command=lambda: openNick())
        self.btnOpen.grid(row=7, column=0, padx=(30,0), pady=(30,0), sticky=N)

            

        def ask_quit():
            self.master.destroy()
            os._exit(0)

      


def GabeText():
    scrollbar1 = Scrollbar(orient=VERTICAL)
    lstList1 = Listbox(exportselection=0,width=100,height=15,yscrollcommand=scrollbar1.set)
    scrollbar1.config(command=lstList1.yview)
    scrollbar1.grid(row=6,column=7,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    lstList1.grid(row=6,column=1,rowspan=7,columnspan=6,padx=(20,0),pady=(0,0),sticky=N+E+S+W)
    lstList1.insert(1, "Oh no... Gabe is far too powerful to face! Quick, click Flee!")

def NickText():
    scrollbar1 = Scrollbar(orient=VERTICAL)
    lstList1 = Listbox(exportselection=0,width=100,height=15,yscrollcommand=scrollbar1.set)
    scrollbar1.config(command=lstList1.yview)
    scrollbar1.grid(row=6,column=7,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    lstList1.grid(row=6,column=1,rowspan=7,columnspan=6,padx=(20,0),pady=(0,0),sticky=N+E+S+W)
    lstList1.insert(1, "Oh no... Nick is far too powerful to face! Quick, click Flee!")

 


def openNick():
    NickText()
    top = Toplevel()
    top.title("Pokemon Battle! NICK")
    top.geometry("600x600+500+300")
    top.configure(background="white")
    btn = Button(top, text="CLICK HERE TO FLEE!", command=top.destroy).pack()
    e = Nick(top)
    e.pack(fill=BOTH, expand=YES)
    print("Oh no... Nick is way too powerful! Click the flee button to get the hell out of there!")

def openGabe():
    GabeText()
    top = Toplevel()
    top.title("Pokemon Battle! GABE")
    top.geometry("600x600+500+300")
    top.configure(background="white")
    btn = Button(top, text="CLICK HERE TO FLEE!", command=top.destroy).pack()
    e = Gabe(top)
    e.pack(fill=BOTH, expand=YES)






class Gabe(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("gabe.jpg")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
        #btn = Button(root, text="Click to open a new window to see your OPPONENT!", command=open).pack()

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)



class Nick(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("nick.jpg")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
        
        


    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)




if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    root = Tk()
    root.title("POKEMON BATTLE GAME")
    root.geometry("600x600")
    root.configure(background="white")
    App = ParentWindow(root)    
    print("Welcome to the Pokemon game!")
    #e = Gabe(root)
    #e.pack(fill=BOTH, expand=YES)
    root.mainloop()

