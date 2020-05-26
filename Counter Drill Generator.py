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
        #master.geometry("1000x600")
        master.config(background = "dark blue")
        master.state('zoomed')
        master.message = ttk.Label(master, font = ('Courier', 130, 'bold'), justify = CENTER, foreground = "white", background = "dark blue")
        master.message1 = ttk.Label(master, font = ('Courier', 130, 'bold'), justify = CENTER, foreground = "white", background = "dark blue")
        master.message2 = ttk.Label(master, font = ('Courier', 130, 'bold'), justify = CENTER, foreground = "white", background = "dark blue")
        master.message3 = ttk.Label(master, font = ('Courier', 130, 'bold'), justify = CENTER, foreground = "white", background = "dark blue")
        master.message.pack()
        master.message1.pack()
        master.message2.pack()
        master.message3.pack()
        master.message.config(text = 'starting...')
        master.update()
        master.message.after(3000)
        for i in range (20):
            master.message.pack_forget()
            master.message1.config(text = str(randint(1,5)) + " #" + str(randint(1,3)))
            master.message2.config(text = str(randint(1,5)) + " #" + str(randint(1,3)))
            master.message3.config(text = str(randint(1,5)) + " #" + str(randint(1,3)))
            
            master.update()
            master.message3.after(4500)

            master.message.config(text = 'switch')
            master.message.pack()
            master.update()
            master.message.after(4500)
        master.message.config(text = 'over', foreground = 'dark red')
            
def main():
    root = Tk()
    win = Generator(root)
    root.lift()
    root.mainloop()

if __name__ == "__main__": main()
    
