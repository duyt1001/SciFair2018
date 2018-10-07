#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:28:35 2018

@author: anna
"""

import cv2
import numpy as np

def scaling(x,minimum,maximum):
    y = x + 99 * maximum * (x-minimum)/(maximum-minimum)
    return y

myimg = cv2.imread('/Users/anna/Desktop/gobidesertsand.jpg')
avg_color_per_row = np.average(myimg, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)

avgimghist = avg_color[0]

img = cv2.imread('/Users/anna/Desktop/gobidesertsand.jpg',0)
rows,cols = img.shape

k = []

for i in range(rows):
    for j in range(cols):
        k.append(img[i,j])
        pixelvalue = (k/avgimghist)
        print(pixelvalue)

scaled = []

for i in range(rows):
    for j in range(cols):
        newval = int(scaling(img[i,j],min(k), max(k)) /avgimghist)
        if i == j:          
            scaled.append(newval)
            


cv2.imwrite('/Users/anna/Desktop/gobidesertsand1.jpg',img)





