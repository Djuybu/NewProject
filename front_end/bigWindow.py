from tkinter import *
from time import *

#biến thời gian:
minute = strftime('%H')
hour = strftime('%M')
day = strftime('%d')
month = strftime('%m')
year = strftime('%Y')
#biến tên người dùng
user = 'Duy'
def createBigWin():
    bigWin = Tk()
    bigWin.geometry('1050x750')
    bigWin.config(bg='#F8C8DC')
    #config grid cho phần ngoài cùng (dùng cho dòng trên cùng)
    for i in range(3):
        bigWin.columnconfigure(i, minsize= 1050/3, weight=1)
        bigWin.rowconfigure(i)
    date = Label(
        bigWin,
        text= 'Ngày '+ day +' tháng '+ month + ' năm ' + year,
        font=('Calibri', 19),
        bg= '#F8C8DC',
    )
    time = Label(
        bigWin,
        text= minute + ':' + hour,
        font=('Calibri', 19),
        bg= '#F8C8DC',
    )
    date.grid(row=0, column=0, columnspan=2, sticky=W, padx=10)
    time.grid(row=0, column=2, sticky=E, padx=10)
#phần nội dung
    #dòng xin chào các kiểu các thứ
    bigGreeting = Label(
        bigWin,
        text= 'Xin chào, ' + user +'!',
        font=('Calibri', 28, 'bold'),
        bg= '#F8C8DC',
    )
    bigGreeting.grid(row=1, column=1)
    commOne = Label(
        bigWin,
        text= 'Đây là các deadline sắp đến hạn của bạn: ',
        font=('Calibri', 24,),
        bg= '#F8C8DC',
    )
    commOne.grid(row=2, column=0, columnspan=3, sticky=W, padx=15)
    #3 cái deadline gần nhất
    for i in range (3):
        urgentDeadline = Frame(
            bigWin,
            bg='#8bd8cc',
        )
        urgentDeadline.config(width=450, height=350,)

        urgentDeadline.grid(row=3, column=i, sticky=W, padx=15, pady= 10)
        deadlineName = Label(
            urgentDeadline,
            text='Hoàn thành bài tập giải tích 1',
            font=('Arial', 16),
            bg ='#8dd8cc',
        )
        comm2 = Label(
            urgentDeadline,
            text= 'Thời gian đến hạn',
            font=('Arial', 12),
            bg ='#8dd8cc',
        )
        dlineTime = Label(
            urgentDeadline,
            text= '15:45, ngày 15 tháng 1 năm 2023',
            font=('Arial', 12),
            bg ='#8dd8cc',
        )
        deadlineName.pack(anchor=W)
        comm2.pack(anchor=W)
        dlineTime.pack(anchor=W)
    bigWin.mainloop()
createBigWin()