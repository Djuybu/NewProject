#front-end cho window nhỏ, chạy cùng với win khi mở lên.
from tkinter import *
from tkinter import ttk
import bigWindow
#các chức năng về thời gian: có thể dùng hoặc không
## from time import *


## hour = strftime('%H')
## minute = strftime('%M')

#tên các biến demo
#các loại biến tên
user = 'Duy'
curDeadline ='Hoàn thành bài tập giải tích 1'

#thời gian của deadline:
deadDay = 30
deadMonth = 10
deadYear = 2023
deadHour = 12
deadMinute = 30
#số deadline còn lại
rDeadline = 3
rPlan = 1

#hàm mở cửa sổ to hơn
def openBigWin():
    bigWindow.createBigWin()
#phần front-end

#hiện khung màn hình
smallWindow = Tk()
smallWindow.title('HeyU Demo')
smallWindow.geometry('320x220')
smallWindow.config(bg='#F8C8DC')

#các label: phần chữ
greetLabel = Label(
    smallWindow,
    text= 'Xin chào ' + user + '!',
    font=('Arial', 18, 'bold'),
    bg='#F8C8DC',
    pady = 3,
    justify= 'left',
    wraplength=315,
)
greetLabel.grid(row=0 ,column=0, sticky=W)
notiLabel = Label(
    smallWindow,
    text= 'Deadline tiếp theo của bạn là ' + ' "' + curDeadline +'"' +  ' vào ' + str(deadDay) + ' tháng ' 
    + str(deadMonth) + ' năm ' + str(deadYear) + ', lúc ' + str(deadHour) + ':' +str(deadMinute),
    font=('Arial', 12),
    bg='#F8C8DC',
    pady = 5,
    justify= 'left',
    wraplength=300,
)
notiLabel.grid(row=1, column=0, sticky=W)
extendLabel = Label(
    smallWindow,
    text= 'Ngoài ra, bạn còn ' + str(rDeadline) + ' deadline và ' + str(rPlan) + ' kế hoạch cần hoàn thành ',
    font=('Arial', 12),
    bg='#F8C8DC',
    pady = 5,
    justify= 'left',
    wraplength=300,
)
extendLabel.grid(row= 2,column=0, sticky=W)
#nút ấn: chuyển sang khung to hơn

openButton = Button(
    smallWindow,
    text= 'Xem thêm',
    font= ('Arial', 18),
    bg= '#fe5bac',
    fg= 'white',
    highlightthickness= 0,
    borderwidth=0,
    activebackground= '#fe5bac',
    activeforeground= 'white',
    command= openBigWin,
)
openButton.grid(row=3)
smallWindow.mainloop()