import tkinter

from tkinter import *
from tkinter.ttk import*

main = Tk()
main. geometry("700x700")

#spinbox
spin = Spinbox(main,from_=0,to= 10)
spin.pack()

#progress
progress = Progressbar(main,orient = HORIZONTAL, length=100, mode="indeterminate")
progress.pack()

def progress_bar():
    import time
    progress["value"]= 20
    main.update_idletasks()
    time.sleep(1)


    progress["value"]= 40
    main.update_idletasks()
    time.sleep(1)

    progress["value"]= 60
    main.update_idletasks()
    time.sleep(1)

    progress["value"]= 80
    main.update_idletasks()
    time.sleep(1)

    progress["value"]= 100


Button(main,text = "START",command=progress_bar).pack()

# menu bar
menu = Menu(main)
file = Menu(menu,tearoff=1)

menu.add_cascade(label = "File", menu=file)
file.add_command(label = "new_file")
file.add_command(label = "save_file")
file.add_command(label = "open_file")
file.add_command(label = "close_file")




edit = Menu(menu,tearoff=0)
menu.add_cascade(label = "Edit", menu=edit)
edit.add_command(label = "undo")
edit.add_command(label = "redo") 
edit.add_separator()
edit.add_command(label = "cut")
edit.add_command(label = "copy")

selection = Menu(menu,tearoff=0)

menu.add_cascade(label = "Selection", menu=selection)
selection.add_command(label = "select_all")
selection.add_command(label = "expand_selection")
selection.add_command(label = "shrink_selection")
selection.add_command(label = "copy_line_up")

main.config(menu = menu)








    














main.mainloop()