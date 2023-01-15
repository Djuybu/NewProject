from tkinter import *
#lệnh đi kèm các button
def submit():
    print("submit completed!")

def delete():
    entry.delete(0, END )
    print("deleted!")

window = Tk()
#khai báo entry: phần ghi chữ vào
entry = Entry(
    window,
    font=('Arial', 30),
)
#một số button nên được đi theo
submit_button = Button(
    window,
    text='submit',
    command= submit,
)
delete_button = Button(
    window,
    text= 'delete',
    command= delete,
)
submit_button.pack(side=RIGHT)
delete_button.pack(side=RIGHT)
entry.pack(side=LEFT)
window.mainloop()