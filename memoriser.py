from tkinter import*
from tkinter.filedialog import*

main=Tk()#
main.geometry("500x500")


def open_file():
    f = askopenfile(title="open_file")
    listbox.delete(0,END)
    items = f.readlines()
    for i in items:
        listbox.insert(END,i)

def add ():
    item = entry_box.get()
    listbox.insert(END, item)

def delete():
    index = listbox.curselection()
    listbox.delete(index)
    
def save():
    f = asksaveasfile(defaultextension=".txt")
    for item in listbox.get(0,END):
        print(item.strip(), file=f)
        

    

 
save_btn = Button(main, text = "save", command = save)
save_btn.pack()
entry_box= Entry(main)
entry_box.place(x=200,y=50)
add_box= Button(main,text = "add", command = add)
add_box.place(x=230, y=80)
open_btn= Button(main,text="open",command= open_file)
open_btn.place(x=20, y=160)
delete_btn= Button(main,text = "delete", command = delete)
delete_btn.place(x=425,y=160)





frame = Frame(main)
frame.place(x = 60 , y = 160)

scrollbar = Scrollbar(frame,orient = "vertical")
scrollbar.pack(side = RIGHT, fill=Y)

listbox= Listbox(frame,width = 56, bg = "black", fg = "white", yscrollcommand = scrollbar.set)
listbox.pack(side = LEFT)

scrollbar.config(command = listbox.yview)







main.mainloop()