#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 19:16:00 2018

@author: anna
"""

from tkinter import *
import tkinter.filedialog
import os
import sys

root = Tk()
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


B = Button(root, text="Unnatural Colors", command=open).pack()
    
B2 = Button(root, text="Morphology", command=open1).pack()

B3 = Button(root, text="Chemical Analysis", command=open2).pack()

root.mainloop()

