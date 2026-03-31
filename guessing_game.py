from tkinter import *
from tkinter import messagebox
import random
#messagebox.showinfo("INFORMATION","info_box")
#messagebox.showwarning ("WARNING", "show_warning")
#messagebox.showerror("ERROR","show_error")

#result = messagebox.askquestion("ASK QUESTION", "ask _question")
main = Tk()
main.geometry("300x300")

def ok():
    name = name_box.get()
    messagebox.showinfo("GUESS NUMBER","hi "+name+" im thinking of a number between 1 and 20")

random_num= random.randint(1,20)
def game():
    user = int(guess_box.get())
    if user <random_num:
        messagebox.showinfo("guess hint","too low")

    elif user >random_num:
        messagebox.showinfo("hint","too high")

    else: 
        messagebox.showinfo("hint", "correct")



main.title("GUESS THE NUMBER GAME")
label = Label(main,text =("WELCOME TO YOUR GAME"))
label.pack()
label2= Label(main,text=("enter your name:"))
label2.place(x=10, y=90)


name_box = Entry(main)
name_box.place(x=10, y =110)

#find button widget from rps code
label3 = Label(main,text = ("take a guess!!"))
label3.place(x=10, y=180)
guess_box= Entry(main)
guess_box.place(x=10, y=200)

ok_btn = Button( width = 4, bd = 0, bg = 'white',text="ok", pady = 3, command = ok)
ok_btn.place(x=140, y=110)

guess_btn = Button( width = 4, bd = 0, bg = 'white',text="guess", pady = 3, command= game)
guess_btn.place(x=140, y=200)


    



main.mainloop()
