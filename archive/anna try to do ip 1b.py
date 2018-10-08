import cv2
import numpy as np


image = cv2.imread('/Users/anna/Desktop/sandwithseafish.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('/Users/anna/Desktop/gray_image_sand_with_seafish.png',gray_image)

p = gray_image.shape
print(p)
rows,cols = gray_image.shape

for i in range(rows):
  for j in range(cols):
     k = gray_image[i,j]
     print("Anna's Pixel Value is:")
     print(k)
 
cv2.imshow('color_image',image)
cv2.imshow('gray_image',gray_image) 
cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()        # Closes displayed windows
