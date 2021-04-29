from tkinter import *
from Tabulirovanie_transtsendentnykh_funktsiy import *
import matplotlib.pyplot as plt

root = Tk()
root['bg'] = '#EDF2F4'
root.geometry('900x900+400+100')
root.title('Вычислительные методы')
x, f = FirstTask()
ls = Label(root, text='Семестровая работа по предмету "Вычислительные методы"', fg='#D90429', bg='#EDF2F4',
      font="Helvetica 14 bold italic")
ls.grid(row=0,column=0,columnspan=len(x))
ls = Label(root, text='x', bg='#EDF2F4', font="Helvetica 14")
ls.grid(row=1,column=0)
root.mainloop()
