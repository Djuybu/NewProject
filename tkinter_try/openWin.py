from tkinter import *

def winOpen():
    #new_window = Toplevel(): là window trên của window ban đầu, sẽ bị đóng nếu cái bé hơn bị đóng
    new_window = Tk()

window = Tk()

butt = Button(
    window,
    text='Open new window',
    command=winOpen,
)

window.mainloop()