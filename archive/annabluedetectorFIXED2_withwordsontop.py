import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# The mask returned from InRange only has 2 values: 0 means not in range, 255 means in range
# So count of 255 means the blue area (or any color) in the range
def get_mask_pct(mask):
    #total_area = len(mask)
    unique, counts = np.unique(mask, return_counts=True)
    count_dict = dict(zip(unique, counts))
    return 100 * (count_dict[255] / sum(counts))
#print "{:.0%}".format(1/3)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([100,60,60])
    upper_blue = np.array([140,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # print percent of blue area
   # print("\nOriginal Number: ", x)
#    print (int(get_mask_pct(mask)), "% area color")
    thingy = ((get_mask_pct(mask)), "% area color")
    print (thingy)
    #print (get_mask_pct(mask))  
#    newthingy = str(thingy)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
     
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,400)
    fontScale              = 1
    fontColor              = (255,255,255)
    lineType               = 2

    cv2.putText(res, "thingy", 
                bottomLeftCornerOfText, 
                font, 
                fontScale,
                fontColor,
                lineType)   

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    


cv2.destroyAllWindows()

