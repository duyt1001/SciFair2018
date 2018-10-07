#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 20:12:04 2018

@author: anna
"""

import cv2
import numpy as np

myimg = cv2.imread('/Users/anna/Desktop/irpic3 (1).jpg')
avg_color_per_row = np.average(myimg, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
avgimghist = avg_color[0]

meimg = cv2.imread('/Users/anna/Desktop/irpic4 (1).jpg')
avg_color_per_row = np.average(meimg, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
avgimghisto = avg_color[1]


myimg = cv2.imread('/Users/anna/Desktop/irpic30.jpg',0)
rows,cols = myimg.shape

meimg = cv2.imread('/Users/anna/Desktop/irpic40.jpg',0)
rows,cols = meimg.shape

k = []
l = []


for i in range(rows):
    for j in range(cols):
        k.append(myimg[i,j])
        l.append(meimg[i,j])
        print(k/l)
        


