from tkinter import *
 
window = Tk()

window.title("Hello, World!")
window.geometry("300x100")
photo = PhotoImage(file='D:\\OneDrive - xdhn\\Tài liệu\\New_project\\tkinter_try\\doge_coin.jpg')
#khai báo la bel vào trong tkinter
label1 = Label(window,text = "hello world", font = ('Arial', 40, 'bold'), fg= "#00FF00", bg='#0DC21F', bd=20,padx= 30, pady = 20,image=photo,compound='bottom')#Label
#text: chữ hiện trong label
#font('font',kích cỡ,'loại chữ')
#fg: màu trước
#bg: màu nền
#image: nhét ảnh vào label
label1.pack()
window.mainloop() 
