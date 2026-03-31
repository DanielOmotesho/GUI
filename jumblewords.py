from tkinter import *
from tkinter import messagebox
import random

main = Tk()
main.geometry("400x400")
main.title("Jumble words game")
main.config(bg = "white")

scor_num = 0

words = {
    "apple":"papel",
    "basket":"skabte",
    "flashlight":"ghlaftlihs",
    "bottle":"ttelob",
    "olive":"eloiv",
    "computer":"rmocptue"}

correct_wrd = ""
jumbled_wrd = ""

def random_wrd(): 
    global correct_wrd, jumbled_wrd
    correct_wrd, jumbled_wrd = random.choice(list (words.items()))
    jumble_wrd_l.config (text =jumbled_wrd )

def check_answer():
    global correct_wrd, scor_num
    guess = eb.get()
    if guess == correct_wrd:
        messagebox.showinfo("correct","you are correct")
        scor_num += 1
        scor.config(text= "SCORE:"+ str(scor_num))
    
        random_wrd()
    else:
        scor_num -= 1
        scor.config(text = "SCORE:" + str(scor_num))



scor = Label(main, text = "SCORE:" )
scor.place(x=250, y=250)

t = Label(main , text = "Jumble words game", font = 20)
t.pack()

jumble_wrd_l = Label(main , text = "")
jumble_wrd_l.pack(pady= 30)

eb = Entry(main)
eb.pack(pady = 40)

check_btn = Button(main, text = "CHECK",fg = "green", command = check_answer)
check_btn.pack(pady = 30)

reset_btn = Button(main, text = "RESET", command = random_wrd)
reset_btn.pack (pady = 10)

random_wrd()







main.mainloop()
