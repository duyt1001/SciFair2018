#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 20:12:04 2018

@author: anna
"""

import cv2
import numpy as np

img_visible = '/Users/anna/SciFair2018/P2visible.jpg'
img_850 = '/Users/anna/SciFair2018/P2850.jpg'
img_output = '/Users/anna/SciFair2018/P2visible850.jpg'

myimg = cv2.imread(img_visible)
avg_color_per_row = np.average(myimg, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
avgimghist = int(avg_color[0])

meimg = cv2.imread(img_850)
avg_color_per_row = np.average(meimg, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
avgimghisto = int(avg_color[0])


myimg = cv2.imread(img_visible,0)
rows,cols = myimg.shape


meimg = cv2.imread(img_850,0)
rows,cols = meimg.shape

thisimg = cv2.imread(img_visible)



k = []
l = []


for i in range(rows):
    for j in range(cols):
        k = myimg[i,j]
        l = meimg[i,j]
        if l == 0 :
            l = 1
        pixelvalue = int(100*((k/avgimghist)/(l/avgimghisto)))
        print(pixelvalue)
        if pixelvalue <= 70:
            thisimg.itemset((i,j,0),pixelvalue)
        if pixelvalue >70 < 140:    
            thisimg.itemset((i,j,1),pixelvalue)
        if pixelvalue >= 140:
            thisimg.itemset((i,j,2),pixelvalue)
      
cv2.imwrite(img_output,thisimg)
    
print("done")    


cv2.putText(myimg,"Anna Du ROV V1.0", (20,20), cv2.FONT_HERSHEY_SIMPLEX, .6,5,2)

print("Anna Du ROV V1.0 IR Absorption Analysis Done")  
print("average image intensities:")
print(avgimghist)
print(avgimghisto)    

