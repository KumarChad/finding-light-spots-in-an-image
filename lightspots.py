import cv2 as cv
import numpy as np

pic = input("enter image you want to check")
img = cv.imread(pic)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


blur = cv.GaussianBlur(gray, (11,11), cv.BORDER_DEFAULT)

ret, thresh = cv.threshold(blur, 150, 255, cv.THRESH_BINARY)

countours, hierarchies = cv.findContours(thresh, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

blank = np.zeros(img.shape, dtype = 'uint8')

cv.drawContours(blank, countours, -1, (255,255,255), 1)

for i in countours:
    M = cv.moments(i)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        if 10000 > cv.contourArea(i) > 200:
            cv.circle(img, (cx, cy), 40, (0,0,255), 3)

cv.imshow('light spots', img)
cv.waitKey(0)