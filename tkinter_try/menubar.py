from tkinter import *

def openFile():
    print('Open the file!')

def saveFile():
    print('Save the file!')

def exitFile():
    print('The file exited!')

def cutFile():
    print('The file cut!')

window = Tk()

#phan menu ben ngoai
menubar = Menu(window)
window.config(menu=menubar)

#add ảnh
imageDemo = PhotoImage(file='D:\\filedemo.png')
#add phan chinh
fileMenu = Menu(menubar, tearoff = 1)#biến fileMenu thành menu
menubar.add_cascade(label="File", menu=fileMenu) #add label tên là menubar vào fileMenu
fileMenu.add_command(label = "Open", command=openFile)
fileMenu.add_command(label= "Save", command=saveFile)
fileMenu.add_command(label= "Exit", command=exitFile)

editBar = Menu(window)
menubar.add_cascade(label="Edit", menu=editBar)
editBar.add_command(label='Cut', command= cutFile)


# editbar.add_ca
window.mainloop()  