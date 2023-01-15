from tkinter import *

window = Tk()
#gọi link
def submit():
    print("You choose "+ str(scale.get())+ "")
    

scale = Scale(window, from_=0, to=100,
    length = 600, #chiều dài
    orient = HORIZONTAL,
    font= ('Calibri', 20),
    tickinterval = 10, #hiện khoảng giữa hai vòng
    showvalue = 1, #hiện giá trị
    resolution= 10,
    troughcolor= "#F1233C",#màu của thanh
    
)
scale.pack()

button = Button(
    window,
    text="submit",
    command= submit,
)
scale.set(100)#ban đầu
button.pack()
window.mainloop()