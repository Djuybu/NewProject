from tkinter import *

window = Tk()

#khai báo frame
frame = Frame(window)
# frame.pack(side=BOTTOM): đơn giản
frame.place(x=100, y=100)   
#tạo những nút để đưa vào frame
wButt = Button(frame,text = "W", font = ('Calibri', 30),width=5).pack(side=TOP)
sButt = Button(frame,text = "A", font = ('Calibri', 30),width=5).pack(side=LEFT)
aButt = Button(frame,text = "S", font = ('Calibri', 30),width=5).pack(side=LEFT)
dButt = Button(frame,text = "D", font = ('Calibri', 30),width=5).pack(side=LEFT)




window.mainloop()