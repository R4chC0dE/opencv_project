import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow("Dog", img)

cv.waitKey(0)

cv.destroyAllWindows()