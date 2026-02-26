from tkinter import*
from tkinter.filedialog import*

main = Tk()
main.geometry("500x500")

main.title("MY ADDRESS BOOK")
ab= Label(main, text="MY ADDRESS BOOK")
ab.place(x=150,y=10)
ab_btn = Button(main,text = "Open")
ab_btn.place(x= 270, y=10)

address_box = Listbox(width=35)
address_box.pack(side= LEFT)

frame = Frame(main)
frame.place(x = 220, y= 180)


name_l= Label(frame,text = "NAME")
name_l.grid(row= 0, column= 0)






















main.mainloop()
