from tkinter import*
from tkinter.filedialog import*
from tkinter.ttk import*

main=Tk()#
main.geometry("500x500")

main.title("STUDENT REGISTRATION")

def enroll ():
    display = "registered for " + topics.get() + " in the " + session.get()
    output.config(text = display)



course_select= Label(main,text="select your course:")
course_select.pack()


topics = StringVar()
options = Combobox (main, textvariable = topics  ,width=10)
options["values"]= ["Game development","Web design", "python"]
options.place(x=200,y=30)

batch_timing = Label(main,text = "Select batch timing:")
batch_timing.place(x=200,y=60)

session = StringVar()
radio1 = Radiobutton(main,text= "Morning (10am)", variable= session, value= "Morning (10am)")
radio1.place(x=150, y=99)
radio2 = Radiobutton(main,text= "Evening (5pm)",variable = session, value = "Evening (5pm)")
radio2.place(x=260,y=99)

enroll_btn = Button(main,text= "enroll", command = enroll)
enroll_btn.place(x=210, y=140)

output = Label(main, text = "")
output.place(x= 150,y= 270)


#fix radio button clicking both at the same time
#fix combo box values
#link function to enroll button












main.mainloop()