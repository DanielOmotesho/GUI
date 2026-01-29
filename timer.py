from tkinter import *
from tkinter import messagebox
import time

main = Tk()
main.geometry("250x350")

hour =StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")



hour_box = Entry(main,textvariable=hour, width=3 , font = ("Arial",18,""))
minute_box = Entry(main,textvariable=minute, width = 3, font = ("Arial",18,""))
second_box = Entry(main,textvariable=second, width=3 , font = ("Arial",18,""))

hour_box.place(x=55, y=10)
minute_box.place(x=95,y=10)
second_box.place(x=135,y=10)

def countdown():
    total_time= int(hour.get())*3600+int(minute.get())*60+int(second.get())
    while total_time>-1:
        mins,sec = divmod(total_time,60)
        hours = 00
        if mins>60:
            hours,mins = divmod(mins,60)
        main.update()
        time.sleep(1)
        hour.set(str(hours))
        minute.set(str(mins))
        second.set(str(sec))
        total_time-=1
        if total_time==-1:
            messagebox.showinfo("timer is up","timer is up")


tc_btn = Button( width = 20, bd = 0, bg = 'white',text="set timer countdown", pady = 3,command=countdown)
tc_btn.place(x=50, y=150)



   















main.mainloop()