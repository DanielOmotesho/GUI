from tkinter import *
from tkinter import messagebox
import random

main = Tk()
main.geometry("400x400")
main.title("Jumble words game")
main.config(bg = "black")


words = {
    "apple":"papel",
    "basket":"skabte",
    "flashlight":"ghlaftlihs"}

correct_wrd = ""
jumbled_wrd = ""

def random_wrd(): 
    global correct_wrd, jumbled_wrd
    correct_wrd, jumbled_wrd = random.choice(list (words.items()))
    jumble_wrd_l.config (text =jumbled_wrd )

def check_answer():
    global correct_wrd
    guess = eb.get()
    if guess == correct_wrd:
        messagebox.showinfo("correct","you are correct")


t = Label(main , text = "Jumble words game", font = 20)
t.pack()

jumble_wrd_l = Label(main , text = "")
jumble_wrd_l.pack(pady= 30)

eb = Entry(main)
eb.pack(pady = 40)

check_btn = Button(main, text = "CHECK",fg = "green")
check_btn.pack(pady = 30)

reset_btn = Button(main, text = "RESET")
reset_btn.pack (pady = 10)

random_wrd()







main.mainloop()