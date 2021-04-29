
from Tabulirovanie_transtsendentnykh_funktsiy import *
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
import matplotlib.pyplot as plt


root = Tk()
root['bg'] = '#EACDC2'
root.title("Вычислительные методы")
root.geometry('1100x650+300+200')
x, f = FirstTask()
n = len(x)
Label(text='Семестровая работа по предмету "Вычислительные методы"', fg='#8f4b31',bg='#EACDC2',
      font="Helvetica 14 bold italic").grid(row=0, column=0, columnspan=n+1,pady=6)
Label(text="x",  font="Helvetica 14", bg='#EACDC2',width=9).grid(row=1, column=0)
Label(text='f(x)', font="Helvetica 14", bg='#EACDC2',width=9).grid(row=2, column=0)
for i in range(n):
    Label(text="%.2f" % x[i], bg='#EACDC2',  font="Helvetica 12",width=9).grid(row=1, column=i + 1)
    Label(text='{}'.format(round(f[i], 6)), bg='#EACDC2',  font="Helvetica 12",width=9).grid(row=2, column=i + 1,pady=6)
# fig = plt.figure(figsize=(8, 6))
# ax2 = fig.add_subplot()
# ax2.set_title("График")
# ax2.plot(x, f, 'red')
# ax2.grid(True)
# plt.show()
frame = Frame(root)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylabel('f(x)')
ax.set_xlabel('x')
ax.grid(True)
fig.autofmt_xdate()
ax.plot(x,f, color='#8f4b31')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=4, column=0,  columnspan=n + 1,pady=6)
frame.grid(row=4, column=4)
Label(text='Титов Сергей, 09 - 831', font="Helvetica 14", bg='#EACDC2').grid(row=n+5, column=0,columnspan=n+1)
root.mainloop()
