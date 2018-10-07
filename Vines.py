#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:45:39 2018

@author: anna
"""

#!/usr/bin/env thon3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:57:57 2018

@author: anna
"""

# This program prints Hello, world!

from tkinter import *
import tkinter.filedialog
import os
import sys

window = Tk()
pyexec = sys.executable

def open():
    PathPy = '/users/anna/Desktop/annabluedetectorFIXED.py'
    os.system('%s %s' % (pyexec, PathPy))

    
def open1():
    PathPy = '/users/anna/Desktop/greenballtracker.py'
    os.system('%s %s' % (pyexec, PathPy))
    
def open2():
    PathPy = '/users/anna/Desktop/comparison850and950nma.py'
    os.system('%s %s' % (pyexec, PathPy))

window = Tk()

window.title("Mah name is Jared, I'm 19, and I can't read")
 

lbl = Label(window, text="Choose An Option Below", font=("Arial Bold", 50))

lbl.grid(column=10, row=10)

colours = ['red','yellow','green','blue','purple','white']

btn = Button(window, command=open2, text="da ting goes skraaaa")

btn.grid(column=10, row=15)

btn2 = Button(window, command=open, text="Ah fuzulmywuzzle you've done it now")
 
btn2.grid(column=10, row=20)

btn3 = Button(window, command=open1, text="Road work ahead? Sure hope it does!")
 
btn3.grid(column=10, row=25)

r = 0
for c in colours:
    Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
    Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1)
    r = r + 1

mainloop()

