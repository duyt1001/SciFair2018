#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:28:35 2018

@author: anna
"""

import cv2
import numpy as np


myimg = cv2.imread('/Users/anna/Desktop/gray_image_sand_with_seafish.png')
avg_color_per_row = np.average(myimg, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
print(avg_color)    
