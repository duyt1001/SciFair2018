import cv2
img = cv2.imread('/Users/anna/Desktop/sandwithseafish.jpg',0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
avgHist = sum(hist) / len(hist)
print(hist)