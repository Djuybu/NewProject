from tkinter import *
#tên các nút
emergency = ["easy", "medium", "hard"]
#set các ảnh


window = Tk()
easyImage = PhotoImage("D:\\OneDrive - xdhn\\Tài liệu\\New_project\\tkinter_try\\green.png")
normalImage = PhotoImage("D:\\OneDrive - xdhn\\Tài liệu\\New_project\\tkinter_try\\yellow.png")
hardImage = PhotoImage("D:\\OneDrive - xdhn\\Tài liệu\\New_project\\tkinter_try\\red.png")
emergencyImage = [easyImage,normalImage,hardImage]
x = IntVar()
#code để lấy các option cần thiết
for index in range(len(emergency)):
    radiobutton = Radiobutton(window, 
    text=emergency[index],
    variable=x,
    value=index,
    font=('Arial', 35)
    )
    radiobutton.pack(anchor=W),
    image = emergencyImage[index],
    indicatoron = 0
    compound = "left",

window.mainloop()