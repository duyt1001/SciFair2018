#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 12:00:42 2018

@author: anna
"""

import cv2
import numpy as np

WINDOW_NAME = 'GreenBall' 

def track(image):

    blur = cv2.GaussianBlur(image, (5,5),0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower_green = np.array([40,70,70])
    upper_green = np.array([80,200,200])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    bmask = cv2.GaussianBlur(mask, (5,5),0)

    moments = cv2.moments(bmask)
    m00 = moments['m00']
    centroid_x, centroid_y = None, None
    
    if m00 != 0:
        centroid_x = int(moments['m10']/m00)
        centroid_y = int(moments['m01']/m00)

    ctr = (-1,-1)

    if centroid_x != None and centroid_y != None:
        ctr = (centroid_x, centroid_y)
        cv2.circle(image, ctr, 8, (0,0,255), thickness = -1)

    cv2.imshow(WINDOW_NAME, image)

    if cv2.waitKey(1) & 0xFF == 27:
        ctr = None
    
    return ctr

if __name__ == '__main__':
    capture = cv2.VideoCapture(0)
    while True:
        okay, image = capture.read()
        if okay:
            if not track(image):
                break    
            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
           print('Capture failed')
           break