from я2 import *
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
import matplotlib.pyplot as plt


def f1():
    n = int(e3.get())
    h = int(e4.get())
    nmin = int(e5.get())

    emax = []
    x = [i for i in range(nmin, n, h)]

    for i in range(nmin, n, h):
        _, _, _, difference = SecondTask(i)
        emax.append(max(difference))
    Label(text='Максимальное значение погрешности интерполирования = ' + "%.3e" % max(emax),
          font="Arial 14", bg='#EACDC2').grid(row=4, column=0, columnspan=5)
    frame = Frame(root)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_ylabel('f(x)')
    ax.set_xlabel('x')
    ax.grid(True)
    fig.autofmt_xdate()
    ax.plot(x, emax, color='#8f4b31')
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=5, column=0, columnspan=n + 1, pady=6, rowspan=5)
    frame.grid(row=5, column=4, rowspan=5)
    Label(text='Титов Сергей, 09 - 831', font="Helvetica 14", bg='#EACDC2').grid(row=n + 5, column=0, columnspan=n + 1)


root = Tk()
root.title("Вычислительные методы")
root.geometry('650x700+300+200')
root['bg'] = '#EACDC2'
Label(text='Семестровая работа по предмету "Вычислительные методы"', fg='#8f4b31', bg='#EACDC2',
      font="Helvetica 14 bold italic").grid(row=0, column=0, columnspan=5, pady=6)
Label(text="a=0", font="Helvetica 14", bg='#EACDC2').grid(row=1, column=0)
Label(text="b=2", font="Helvetica 14", bg='#EACDC2').grid(row=1, column=1)
Label(text="Максимальный n", font="Helvetica 14", bg='#EACDC2').grid(row=1, column=4)
Label(text="Шаг", font="Helvetica 14", bg='#EACDC2').grid(row=1, column=3)
Label(text="Минимальный n", font="Helvetica 14", bg='#EACDC2').grid(row=1, column=2)

e5 = Entry(root, width=8)

e5.grid(row=2, column=2)

e4 = Entry(root, width=8)

e4.grid(row=2, column=3)
e3 = Entry(root, width=8)

e3.grid(row=2, column=4)
b2 = Button(text='Провести эксперимент', font="Helvetica 14", command=f1, bg='#8f4b31', fg='#ffffff')
b2.grid(row=2, column=0, columnspan=2)

root.mainloop()
