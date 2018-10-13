#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 15:28:45 2018

@author: anna
"""

import numpy as np
import cv2
import argparse, sys

# Using Argument Parser to get the location of image
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to image')
ap.add_argument('--shape', default='all', help='Shapes to be tagged')
ap.add_argument('--sigma', type=float, default=0.33, help='Sigma of edge detection')
ap.add_argument('--count', type=int, default=50, help='Count of tagged objects')
ap.add_argument('--low', type=int, help='Low of Canny detection')
ap.add_argument('--high', type=int, help='High of Canny detection')
ap.add_argument('--no-tagging', action='store_true', help='Draw the contour without tagging')
args = ap.parse_args()

# load the image on disk and then display it
image = cv2.imread(args.image)
cv2.imshow("Original", image)

# convert the color image into grayscale
grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find edges in the image using canny edge detection method
# Calculate lower threshold and upper threshold using sigma = 0.33
sigma = args.sigma
v = np.median(grayScale)
low = int(max(0, (1.0 - sigma) * v))
high = int(min(255, (1.0 + sigma) * v))
if args.low:
    low = args.low
if args.high:
    high = args.high

edged = cv2.Canny(grayScale, low, high)

(_, cnts, _) = cv2.findContours(edged,
                                cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)



def detectShape(cnt):
    shape = 'unknown'
    peri = cv2.arcLength(c, True)
    vertices = cv2.approxPolyDP(c, 0.04 * peri, True)

    if len(vertices) == 3:
        shape = 'triangle'

    # if the shape has 4 vertices, it is either a square or
    # a rectangle
    elif len(vertices) == 4:
        # using the boundingRect method calculate the width and height
        # of enclosing rectange and then calculte aspect ratio

        x, y, width, height = cv2.boundingRect(vertices)
        aspectRatio = float(width) / height

        # a square will have an aspect ratio that is approximately
        # equal to one, otherwise, the shape is a rectangle
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            shape = "square"
        else:
            shape = "rectangle"

    # if the shape is a pentagon, it will have 5 vertices
    elif len(vertices) == 5:
        shape = "pentagon"

    # otherwise, we assume the shape is a circle
    else:
        shape = "circle"

    # return the name of the shape
    return shape

# Sort the contours by their area
areas = [ cv2.contourArea(c) for c in cnts]
#sorted_cnts = [x for _,x in sorted(zip(areas, cnts), reverse=True)]
inds = list(range(len(cnts)))
sorted_inds = [x for _,x in sorted(zip(areas, inds), reverse=True)]
sorted_cnts = [ cnts[i] for i in sorted_inds]

# Now we will loop over every contour
# call detectShape() for it and
# write the name of shape in the center of image

# loop over the contours
for c in sorted_cnts[:args.count]:
    # compute the moment of contour
    M = cv2.moments(c)
    if M['m00'] == 0 :
        continue;
    # From moment we can calculte area, centroid etc
    # The center or centroid can be calculated as follows
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])

    # call detectShape for contour c
    shape = detectShape(c)

    # Outline the contours
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

    # Write the name of shape on the center of shapes
    if not args.no_tagging:
        if args.shape == 'all' or args.shape == shape:
            cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 255, 255), 2)

    # show the output image
    cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
