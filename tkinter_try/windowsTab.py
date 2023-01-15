from tkinter import *
from tkinter import ttk

window = Tk()
#khai báo notebook: phần khung chứa các tabs
notebook = ttk.Notebook(window)

#khai báo các tabs
tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1)
notebook.add(tab2)
notebook.pack(expand=True, fill='both')
#expand: nở ra chiếm toàn bộ chỗ, fill: chiếm theo chiều x/y/cả 2

