#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:28:35 2018

@author: anna
"""

import cv2
import numpy as np


img2 = cv2.imread('/Users/anna/Desktop/greypicture.jpeg')

img2.itemset((150,150,0),0)
img2.itemset((151,151,2),0)
img2.itemset((152,152,1),0)

cv2.imwrite('/Users/anna/Desktop/greypicture2.jpeg',img2)

# accessing RED value
# img.item(10,10,2)


# modifying RED value
# img.itemset((10,10,2),100)
# img.item(10,10,2)



#cv2.imshow('Test', img2)