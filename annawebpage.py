

#facedetectv3.py
# import the necessary packages
import argparse
import os

import numpy as np
import cv2



cap = cv2.VideoCapture(0)




#    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
#    for (ex,ey,ew,eh) in hands:
#	rod_col = img[y:y+h, x:x+w]
#       cv2.rectangle(rod_col,(ex,ey),(ex+ew,ey+eh),(255,0,255),2)

font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (x,y)
fontScale = 1
fontColor = (255,255,255)
lineType = 2

    cv2.putText(img,'Hi, I am a Person!', bottomLeftCornerOfText, font, fontScale,fontColor,lineType)

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
facedetectv3.py
