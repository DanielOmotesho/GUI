from tkinter import*
from tkinter.ttk import*

main=Tk()
title = Label(main,text="TIMES TABLES")
title.pack()
title2 = Label(main,text = "ENTER NUMBER AND RANGE")
title2.place(x=20, y=80)

def show_table():
    tables = ""
    for i in range(times.get()):
        tables+=str(num.get())+ " x " +str(i)+ " = " +str(num.get()*i)+"\n"
    
    output_label.config(text = tables)



num= IntVar()
numbers = Combobox(main,textvariable=num,width=5)
numbers["values"]=tuple(range(101))
numbers.place(x=190, y=80)

times = IntVar()
radio1 = Radiobutton(main,text="10",variable=times,value = 11)
radio1.place(x=300, y=80)
radio2 = Radiobutton(main,text="20",variable = times, value = 21)
radio2.place(x=300,y= 100)
radio3 = Radiobutton(main,text="30",variable = times, value = 31)
radio3.place(x=300,y= 120)

result_btn = Button(main,text="SHOW RESULT",command=show_table)
result_btn.place(x=190, y=140)

output_label = Label(main)
output_label.place(x=190, y=170)







main.mainloop()

               