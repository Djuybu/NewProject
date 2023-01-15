from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import time

#lệnh demo cái progress bar:

def barRun():
    tasks = 10
    x = 0
    def update():
        nonlocal x
        if x < tasks:
            x += 1
            bar["value"] += 10
            window.after(1000, update)

    update()


window = Tk()
butt = Button(
    window,
    text= 'Press me',
    command= barRun,
    )
butt.pack()
# label = Label(butt, text="Press me", font=("Arial", 30))
# label.pack()

#khai báo bar
bar = Progressbar(window, orient=HORIZONTAL, length= 300)
bar.pack(pady = 10)

window.mainloop()