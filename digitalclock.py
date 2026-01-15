from tkinter import *
from tkinter.ttk import *
from time import strftime
import tkinter.font as font
 
main = Tk()
main.geometry("250x50")
main.title("DIGITAL CLOCK")
main.config (background= "LightSeaGreen")
game_font = font.Font(size = 19)

label = Label(main,font = game_font, background= "LightSeaGreen", foreground= "white")
label.pack()

def show_time():
    result = strftime("%H:%M:%S %p")
    label.config(text = result) 
    label.after(1000,show_time)
    
show_time()

main.mainloop()