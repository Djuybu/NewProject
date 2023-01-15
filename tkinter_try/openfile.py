from tkinter import *
from tkinter import filedialog


#lenh de mo file
def openFile():
    filePath = filedialog.askopenfilename(
        # initialdir="C:\\" : dùng để mở địa chỉ
        title="Open file okay?",
        filetypes= (("text files", "*.txt"),
        ("all files", "*.*")),

    )
    file = open(filePath,'r')
    print(file.read())
    file.close()



window = Tk()


butt1 = Button(
    window,
    text='open file:',
    command= openFile
)
butt1.pack()

window.mainloop()