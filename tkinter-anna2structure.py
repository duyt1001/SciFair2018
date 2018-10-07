#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:57:57 2018

@author: anna
"""

# This program prints Hello, world!

from tkinter import *

window = Tk()
 
window.title("Welcome to Anna Du ROV V1.0 Microplastics Image Recognition System")
 
#lbl = Label(window, text="Hello")
 

lbl = Label(window, text="Choose An Option Above", font=("Arial Bold", 50))
lbl.grid(column=10, row=10)

colours = ['red','green','purple','white','yellow','blue']

btn = Button(window, text="Infrared Comparison Color Mapper")
 
btn.grid(column=10, row=15)

btn2 = Button(window, text="Unnatural/False Color Detector")
 
btn2.grid(column=10, row=20)

btn3 = Button(window, text="Morphology/Structural Differentiator Detector")
 
btn3.grid(column=10, row=25)

r = 0
for c in colours:
    Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
    Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1)
    r = r + 1

mainloop()