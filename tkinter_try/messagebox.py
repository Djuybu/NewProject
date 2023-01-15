from tkinter import messagebox
from tkinter import *

def click():


    #askquestionyesno:
    answer = messagebox.askyesnocancel(title='ask question', message='ang nhang nhang hong???', icon = 'info')
    if(answer == True):
        print('lmaoo')
    elif(answer == False):
        print('nooo')
    else:
        print('huhu')


window = Tk()
button = Button(window, command= click, text='click here')
button.pack()
window.mainloop()