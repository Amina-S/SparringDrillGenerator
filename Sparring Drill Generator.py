from tkinter import *
from tkinter import ttk
from random import randint

class Generator():

    def __init__(self, master):
        master.geometry("1000x600")
        master.message = ttk.Label(master, font = ('Courier', 120, 'bold'), justify = CENTER, foreground = "dark green")
        master.message.pack()
        
        for i in range (50):
            drill = randint(1, 8)
            print(drill)
            if (randint(1,10) == 9):
                master.update()
                master.message.after(1000, master.message.config(text = 'switch'))                
            if (drill == 1 or drill == 3):
                master.update()
                master.message.after(3500, master.message.config(text = drill))                
            elif (drill == 2 or drill == 5):
                master.update()
                master.message.after(1500, master.message.config(text = drill))                
            else:
                master.update()
                master.message.after(5000, master.message.config(text = drill))                
            
def main():
    root = Tk()
    win = Generator(root)
    root.lift()
    root.mainloop()

if __name__ == "__main__": main()
    
    



















    
