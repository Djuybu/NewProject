from tkinter import *
#grid: chia màn hình theo dạng bảng, với các row & column
#các row & column được đánh số từ trái - phải, trên - dưới, bắt đầu từ số 0.

window = Tk()

firstnameLabel = Label(window, text='Firstname:').grid(row=0, column=0)
firstnameEntry = Entry(window).grid(row=0, column=1)
#với grid() được áp dụng, firstNameLabel sẽ xuất hiện trên cùng bên trái, firstNameEntry sẽ nằm trên cùng, phía bên phải firstnameLabel
lastnameLabel  = Label(window, text='Lastname: ').grid(row=1,column=0)
lastnameEntry = Entry (window).grid(row=1, column=1)

emailLabel = Label(window, text='Email: ').grid(row = 2,column=0)
emailEntry = Entry(window).grid(row=2, column=1)

submitButton = Button(text='Submit').grid(row = 3, column=0, columnspan=2)

window.mainloop()