

from tkinter import *


main = Tk()
main. geometry("300x150")

label=Label(main,text = "daniel omotesho", font="50")
label.pack()

frame = Frame(main,bg="red")
frame.pack()

button_frame = Frame(main)
button_frame.pack(side = BOTTOM)

button1 = Button(main, text="Hello" )
button1.pack(side= LEFT)


button2= Button(main, text="Hello" ,fg= "blue", bg="brown")
button2.pack(side= LEFT)


button3 = Button(main, text="Hello")
button3.pack(side= BOTTOM)


button4 = Button(main, text="Hello" )
button4.pack(side= BOTTOM)

main.mainloop()