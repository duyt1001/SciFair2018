#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:28:35 2018

@author: anna
"""

import cv2

img2 = cv2.imread('/Users/anna/Desktop/greypicture.jpeg')

img2.itemset((140,140,0),0)
img2.itemset((141,141,2),0)
img2.itemset((142,142,1),0)

cv2.imwrite('/Users/anna/Desktop/greypicture3.jpeg',img2)

