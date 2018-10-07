#facedetectv3.py
# import the necessary packages
import argparse
import os

import numpy as np
import cv2

watermark = cv2.imread('pyimagesearch_watermark.png', cv2.IMREAD_UNCHANGED)
(wH, wW) = watermark.shape[:2]
(B, G, R, A) = cv2.split(watermark)
B = cv2.bitwise_and(B, B, mask=A)
G = cv2.bitwise_and(G, G, mask=A)
R = cv2.bitwise_and(R, R, mask=A)
watermark = cv2.merge([B, G, R, A])

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#hand_cascade = cv2.CascadeClassifier('aGest.xml')
img2 = cv2.imread("smalllogo.png")

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
#    for (ex,ey,ew,eh) in hands:
#	rod_col = img[y:y+h, x:x+w]
#       cv2.rectangle(rod_col,(ex,ey),(ex+ew,ey+eh),(255,0,255),2)



    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	font                   = cv2.FONT_HERSHEY_SIMPLEX
	bottomLeftCornerOfText = (x,y)
	fontScale              = 1
	fontColor              = (255,255,255)
	lineType               = 2

	cv2.putText(img,'Hi, I am a Person!', 
    		bottomLeftCornerOfText, 
    		font, 
    		fontScale,
    		fontColor,
    		lineType)

#	y1, y2 = y, y + s_img.shape[0]
#	x1, x2 = x, x + s_img.shape[1]
#	alpha_s = s_img[:, :, 3] / 255.0
#	alpha_l = 1.0 - alpha_s

    (h, w) = img.shape[:2]
    img = np.dstack([img, np.ones((h, w), dtype="uint8") * 255])
 
	# construct an overlay that is the same size as the input
	# image, (using an extra dimension for the alpha transparency),
	# then add the watermark to the overlay in the bottom-right
	# corner
    overlay = np.zeros((h, w, 4), dtype="uint8")
    overlay[h - wH - 10:h - 10, w - wW - 10:w - 10] = watermark
 
    output = img.copy()
    cv2.addWeighted(overlay, 0.25, output, 1.0, 0, output) 
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()