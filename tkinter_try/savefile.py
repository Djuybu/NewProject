from tkinter import *
from tkinter import filedialog


#lenh de luu file
def saveFile():
    file = filedialog.asksaveasfile(
        defaultextension= '*.txt',
        filetypes=[
            ("Text file", ".txt"),
            ("HTML file", ".html"),
            ("All files", "*.*"),
        ]
    )
    fileText = str( text.get(1.0, END))
    file.write(fileText)
    file.close()
    if file is None:
        return


window = Tk()
#khu text:
text = Text(window)
text.pack()
button = Button(
    window,
    text='save',
    command=saveFile,
)
button.pack()

window.mainloop()