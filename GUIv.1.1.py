from tkinter import Tk, Label, Button, Entry, RIDGE, SUNKEN
import os
import sys
from tkinter.ttk import Separator, Style
from PIL import ImageTk, Image


pyexec = sys.executable


def open():
    PathPy = 'annabluedetectorFIXED.py'
    os.system('%s %s' % (pyexec, PathPy))
def open1():
    PathPy = '/annagreenballdetector.py'
    os.system('%s %s' % (pyexec, PathPy))
def open2():
    PathPy = 'comparison850and950nma.py'
    os.system('%s %s' % (pyexec, PathPy))
def open3():
    PathPy = 'annaorangedetectorFIXED.py'
    os.system('%s %s' % (pyexec, PathPy))
def open4():
    PathPy = 'annapurpledetectorFIXED.py'
    os.system('%s %s' % (pyexec, PathPy))
def open5():
    PathPy = 'annachartreusedetectorFIXED.py'
    os.system('%s %s' % (pyexec, PathPy))
def open6():
    PathPy = 'visible850950.jpg'
    os.system('%s %s' % (pyexec, PathPy))

window = Tk()
window.title("Anna Du ROV V1.0 Microplastics Image Recognition System")

lbl = Label(window, text="Anna Du ROV V1.0 Microplastics Image Recognition System", font=("Arial Bold", 50), bg="cyan")
lbl.grid(column=10, row=20)

lbls = Label(window, text="Choose An Option Below", font=("Arial Bold", 40), bg="medium orchid")
lbls.grid(column=10, row=25, sticky="w")

sep = Separator(window, orient="horizontal")
sep.grid(column=5, row=23, columnspan=20, sticky="ew")
sty = Style(window)
sty.configure("TSeparator", background="red")

btn = Button(window, command=open2, text="Infrared Comparison Color Mapper", font=("Arial Bold",25), height=2)
btn.grid(column=10, row=30, sticky="w")

lblss = Label(window, text="Unnatural Colors", font=("Arial Bold", 40), bg="medium orchid")
lblss.grid(column=10, row=35, sticky="w")

btn3 = Button(window, command=open, text="Blue", font=("Arial Bold",25), height=2)
btn3.grid(column=10, row=40, sticky="w")

btn4 = Button(window, command=open5, text="Chartreuse", font=("Arial Bold",25), height=2)
btn4.grid(column=10, row=45, sticky="w")

btn5 = Button(window, command=open4, text="Purple", font=("Arial Bold",25), height=2)
btn5.grid(column=10, row=50, sticky="w")

btn6 = Button(window, command=open3, text="Orange", font=("Arial Bold",25), height=2)
btn6.grid(column=10, row=55, sticky="w")

btn7 = Button(window, command=open1, text="Morphology/Structural Differentiator Detector", font=("Arial Bold",20), height=2)
btn7.grid(column=10, row=60, sticky="w")

sepa = Separator(window, orient="vertical")
sepa.grid(column=10, row=20, rowspan=80, sticky="ns")
styl = Style(window)
styl.configure("ThSeparator", background="red")

lblssS = Label(window, text="Color maps", font=("Arial Bold", 40), bg="medium orchid")
lblssS.grid(column=10, row=25, sticky="e")

btn8 = Button(window, command=open6, text="Color map1", font=("Arial Bold",25), height=2)
btn8.grid(column=10, row=30, sticky="e")

lbl1 = Label(window, text="Blog Post link", font=("Arial Bold", 40), bg="medium orchid")
lbl1.grid(column=10, row=35, sticky="e")

lbl2 = Label(window, text="https://www.youngscientistlab.com/entry/1669", font=("Arial Bold", 20))
lbl2.grid(column=10, row=40, sticky="e")



r = 0

window.mainloop()

