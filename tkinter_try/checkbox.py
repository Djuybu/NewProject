from tkinter import *

window = Tk()

agree = IntVar ()
def display():
    if(agree.get()==1):
        print('You agree')
checkButton = Checkbutton(
    window,
    text= "Im agree!",
    variable= agree,
    onvalue= 1,
    offvalue= 0,
    command=display,
    font=('Arial', 30),
    fg= '#3233FC',
    bg= 'black',
    activebackground='white',
    activeforeground='black',
    padx= 30,
    pady= 20,
)
checkButton.pack()
window.mainloop()