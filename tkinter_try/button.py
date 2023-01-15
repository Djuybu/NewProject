from tkinter import *

window = Tk()

def click():
    print("Hi there!")

photo = PhotoImage(file='D:\\OneDrive - xdhn\\Tài liệu\\New_project\\tkinter_try\\doge_coin.jpg')
button = Button(
    window,
    text= 'gimme a try, wont ya?',
    command=click,
    font=('Arial', 30),
    fg = '#ff00ff',
    bg = '#000000',
    activebackground='#c33f4a',
    activeforeground='#ffff0c',
    image= photo,
    compound= 'bottom',
)
#command: dán lệnh vào button
#activeforeground/background: màu khi ấn vào
button.pack()#lệnh để pack cái gì vào
window.mainloop()
