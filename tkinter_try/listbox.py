from tkinter import *
#code cho cái submit:


window = Tk()
#các lệnh
def submit():
    # đây là insert 1 cái
    # print("bạn đã chọn: ")
    # print(listbox1.get(listbox1.curselection()))
    #insert nhiều cái:
    food = []
    
    for index in listbox1.curselection():
        food.insert(index, listbox1.get(index))
    print('You have ordered: ')
    for index in food:
        print(index)
def addup():
    listbox1.insert(listbox1.size(), entry.get())
    listbox1.config(height=listbox1.size())
def delete():
    listbox1.delete(listbox1.curselection())
    listbox1.config(height=listbox1.size())

#listbox ở đây:
listbox1 = Listbox(window,
    bg = "#123cf2",
    fg= "#223212",
    font= ('Arial', 30),
    selectmode= MULTIPLE, #select nhiều cái
)

listbox1.pack()
#insert các element vào trong: vị trí, tên
listbox1.insert(1, "bún đậu mắm tôm")
listbox1.insert(2, "thịt chó")
listbox1.insert(3, "phở")
listbox1.insert(4, "bánh mì")
listbox1.config(height=listbox1.size())
#nút để submit
submit_butt = Button(window, text='submit', font=('Arial', 30), command=submit)
submit_butt.pack()
#nút để thêm thêm thứ vào:
entry = Entry(
    window,
    font=('Arial',30),
    )
entry.pack()
sub2 = Button(window, text='thêm món', font=('Arial', 10), command= addup)
sub2.pack()
del1 = Button(window, text='xoá', font=('Arial', 10), command= delete)
del1.pack()
window.mainloop()