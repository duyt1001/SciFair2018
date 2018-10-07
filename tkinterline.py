#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 17:16:08 2018

@author: anna
"""

from tkinter import Tk, Canvas

master = Tk()

w = Canvas(master, width=200, height=100,bd=0,highlightthickness=0)
w.configure(bg="purple")
w.pack()

w.create_line(100, 100, 0, 0, fill="pink")
w.create_line(100, 0, 0, 0, fill="red")
master.mainloop()