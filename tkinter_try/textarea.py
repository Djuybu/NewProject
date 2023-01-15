from tkinter import *


def submit():
    print(text.get("1.0", END))

window = Tk()
#phần text
text = Text(
    window,
    font=('Arial', 20),
    height= 9,
    width= 20,
    bg= "#FFB6C1",
    fg ='black',
)
text.pack()

#nút để submit
button = Button(
    text='submit',
    command=submit,
)

button.pack()
window.mainloop()