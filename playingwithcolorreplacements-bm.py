#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:28:35 2018

@author: anna
"""

import cv2
import numpy as np

img2 = cv2.imread('/Users/anna/Desktop/greypicture.jpeg')

img2.itemset((140,140,1),255)
img2.itemset((141,141,1),255)
img2.itemset((142,142,1),255)
img2.itemset((185,137,1),255)

img2.itemset((150,150,0),255)
img2.itemset((151,151,0),255)
img2.itemset((152,152,0),255)


img2.itemset((160,160,2),255)
img2.itemset((161,161,2),255)
img2.itemset((162,162,2),255)


cv2.imwrite('/Users/anna/Desktop/greypicture5.jpeg',img2)

# accessing RED value
# img.item(10,10,2)


# modifying RED value
# img.itemset((10,10,2),100)
# img.item(10,10,2)



#cv2.imshow('Test', img2)