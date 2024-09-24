import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. make image a certain colour
blank[200:300, 300:400] = 255, 0, 0
cv.imshow('Green', blank)

# 2. draw a rectangle
# just border of rectangle
cv.rectangle(blank, (0,0), (250, 500), (0, 255, 0), thickness=2)
# filled rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=cv.FILLED)
# also fills rectangle
# cv.rectangle(blank, (0,0), (250, 500), (0, 255, 0), thickness=-1)
cv.imshow('Rectangle', blank)


# 3. draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=cv.FILLED)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=5)
cv.imshow('Line', blank)

# 5. write text 
cv.putText(blank, 'Hello there', (225, 255), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
