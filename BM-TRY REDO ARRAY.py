#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 15:00:33 2018

@author: anna
"""


import cv2
import numpy as np


myimg = cv2.imread('/Users/anna/Desktop/gobidesertsand.jpg')
avg_color_per_row = np.average(myimg, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)

avgimghist = int(avg_color[0])

print("start")



img = cv2.imread('/Users/anna/Desktop/gobidesertsand.jpg',0)
rows,cols = img.shape

k = []


print("start")

for i in range(rows):
    for j in range(cols):
       # k.append(img[i,j])  this is wrong, comingup with scalar
        k = img[i,j]
        #print(k)
        pixelvalue = (int(100*(k/avgimghist)))
        print (pixelvalue)
        if pixelvalue <= 100:
            myimg.itemset((i,j,0),pixelvalue)
        if pixelvalue >100 < 200:    
            myimg.itemset((i,j,1),pixelvalue)
        if pixelvalue > 199:
            myimg.itemset((i,j,2),pixelvalue)

cv2.imwrite('/Users/anna/Desktop/sandredo6.jpeg',myimg)

print("done")  
print("average image intensity:")
print(avgimghist)
    


