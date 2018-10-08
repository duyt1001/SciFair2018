import cv2
import numpy as np
import argparse, sys

# The color range to be detected. Format:
# color: (lower_hsv, upper_hsv)
colors = {
    'blue': ([100,60,60], [135,255,255]),
    'green': ([40,70,70], [80,200,200]),
    'orange': ([10,20,60], [25,255,255]),
    'purple': ([130,20,60], [160,255,255])
}

# Get the color from command line
ap = argparse.ArgumentParser()
ap.add_argument('-c', '--color', required=True, help='The designated color to be detected')
ap.add_argument('--camera', type=int, default=0, help='The camera to use. 0: Internal')
args = ap.parse_args()
color = args.color

if color not in colors.keys():
    print("The color is not supporte: " + args.color, file=sys.stderr)
    sys.exit(1)


try:
    cap = cv2.VideoCapture(args.camera)
except:
    print ("Did the camera configure correctly?", file=sys.stderr)
    sys.exit(1)


while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    try:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    # define range of color in HSV
    lower_hsv = np.array(colors[color][0])
    upper_hsv = np.array(colors[color][1])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    cv2.namedWindow('res', cv2.WINDOW_NORMAL)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    # press ESC or SPACE to exit
    if k == 27 or k == 32:
        break
    

cap.release()
cv2.destroyAllWindows()

