#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 20:12:04 2018

@author: anna
"""

import cv2
import numpy as np

myimg = cv2.imread('/Users/anna/Desktop/comparisonoutput3.jpg')
avg_color_per_row = np.average(myimg, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
avgimghist = int(avg_color[0])

meimg = cv2.imread('/Users/anna/Desktop/comparisonoutput4.jpg')
avg_color_per_row = np.average(meimg, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
avgimghisto = int(avg_color[0])


myimg = cv2.imread('/Users/anna/Desktop/comparisonoutput3.jpg',0)
rows,cols = myimg.shape


meimg = cv2.imread('/Users/anna/Desktop/comparisonoutput4.jpg',0)
rows,cols = meimg.shape

thisimg = cv2.imread('/Users/anna/Desktop/comparisonoutput3.jpg')



k = []
l = []


for i in range(rows):
    for j in range(cols):
        k = myimg[i,j]
        l = meimg[i,j]
        pixelvalue = (100*((k/avgimghist)/(l/avgimghisto)))
        print(pixelvalue)
        if pixelvalue <= 70:
            thisimg.itemset((i,j,0),pixelvalue)
        if pixelvalue >70 < 140:    
            thisimg.itemset((i,j,1),pixelvalue)
        if pixelvalue >= 140:
            thisimg.itemset((i,j,2),pixelvalue)

cv2.putText(thisimg,"Anna Du ROV V1.0", (20,20), cv2.FONT_HERSHEY_SIMPLEX, .6,5,2)
        
cv2.imwrite('/Users/anna/Desktop/cnot-b.jpg',thisimg)
 
print("done")    


cv2.putText(myimg,"Anna Du ROV V1.0", (20,20), cv2.FONT_HERSHEY_SIMPLEX, .6,5,2)

print("Anna Du ROV V1.0 IR Absorption Analysis Done")  
print("average image intensities:")
print(avgimghist)
print(avgimghisto)    

