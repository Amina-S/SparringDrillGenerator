from tkinter import *
from tkinter import ttk
from random import randint

import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

class Generator():

    def __init__(self, master):
        master.geometry("1000x600")
        master.config(background = "light yellow")
        master.message = ttk.Label(master, font = ('Courier', 140, 'bold'), justify = CENTER, foreground = "dark green", background = "light yellow")
        master.message.pack()
        master.update()
        for i in range (50):
            drill = randint(1, 8) 
            if (randint(1,10) % 2 == 0):
                master.message.config(text = 'switch')
                master.update()
                master.message.after(1700)         
            if (drill == 1 or drill == 3):
                master.message.config(text = drill)
                master.update()
                master.message.after(3800)
            elif (drill == 2 or drill == 5 or drill == 6):
                master.message.config(text = drill)
                master.update()
                master.message.after(2600)
            else:
                master.message.config(text = drill)
                master.update()
                master.message.after(3200)
        master.message.config(text = 'over', foreground = 'dark red')
            
def main():
    root = Tk()
    win = Generator(root)
    root.lift()
    root.mainloop()

if __name__ == "__main__": main()
    
    



















    
